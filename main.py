import sys
import os

import numpy as np
import pydicom
from PIL import Image
import math

from PySide6.QtWidgets import (QMainWindow, QFileDialog, QApplication, QVBoxLayout, QProgressDialog,
                               QLabel, QFrame)
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap
from PySide6 import QtCore, QtWidgets

import matplotlib
matplotlib.use('qtagg')
os.environ['QT_API'] = 'pyside6'

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolBar
)
from matplotlib.figure import Figure
from mainwindow_new import Ui_MainWindow
from ui_stats import statsUI
from colorsettingsdialog import ColorSettingsDialog
import pandas as pd


class MPLCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        # Create plots
        axes_histPlot = fig.add_subplot(121)
        axes_cumFreqPlot = fig.add_subplot(122)

        # Add labels
        axes_histPlot.set_title("Image Histogram")
        axes_histPlot.set_ylabel("Number of Pixels")
        axes_histPlot.set_xlabel("Intensity")

        axes_cumFreqPlot.set_title("Cumulative Frequency")
        axes_cumFreqPlot.set_ylabel("Cumulative Number of Pixels")
        axes_cumFreqPlot.set_xlabel("Intensity")
        fig.tight_layout()
        super(MPLCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Variables
        self.isDICOM = True
        self.canceledLoading = None
        self.polygon = None
        self.barContainer = None
        self.gainLeft = None
        self.gainRight = None
        self.scroll = None
        self.axes_cumFreqPlot = None
        self.axes_histPlot = None
        self.plotted = False
        self.statsWindow = None

        # Setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Image Histogram")
        self.setWindowIcon(QPixmap("logo.ico"))

        # Create canvas on QWidget
        self.canvas = MPLCanvas(self, width=10, height=5, dpi=100)
        self.ui.widget.setLayout(QVBoxLayout())
        self.ui.widget.layout().addWidget(self.canvas)

        # Variables
        self.graphBarColor = '#8b8b8b'

        # Add toolbar
        self.toolbar = NavigationToolBar(self.canvas, self)
        self.ui.toolbox_layout.addWidget(self.toolbar, stretch=100)

        # Add import options
        self.ui.importTypeComboBox.addItems(["Image", "DICOM", "CSV"])

        # Connect signals to slots
        self.ui.importCSVButton.clicked.connect(self.importButton_Clicked)

        self.ui.scrollSlider.valueChanged.connect(self.scrollValueChanged)
        self.ui.gainSlider.valueChanged.connect(self.gainValueChanged)

        self.ui.actionSettings.triggered.connect(self.colorSettingsActionClicked)
        self.ui.clearButton.clicked.connect(self.clearPlots)

    @Slot()
    def clearPlots(self):
        # Clear
        self.canvas.figure.clf()

        # Add plots
        self.axes_histPlot = self.canvas.figure.add_subplot(121)
        self.axes_cumFreqPlot = self.canvas.figure.add_subplot(122)
        self.scroll = self.axes_histPlot.axvline(10, color='#FF0000')
        self.gainLeft = self.axes_histPlot.axvline(0, color='#0072DC')
        self.gainRight = self.axes_histPlot.axvline(20, color='#0072DC')

        # Add labels
        self.axes_histPlot.set_title("Image Histogram")
        self.axes_histPlot.set_ylabel("Number of Pixels")
        self.axes_histPlot.set_xlabel("Intensity")

        self.axes_cumFreqPlot.set_title("Cumulative Frequency")
        self.axes_cumFreqPlot.set_ylabel("Cumulative Number of Pixels")
        self.axes_cumFreqPlot.set_xlabel("Intensity")

        self.scroll.set_label("Scroll")
        self.gainLeft.set_label("GainLeft")
        self.gainRight.set_label("GainRight")

        self.canvas.figure.tight_layout()
        self.canvas.draw()
        self.plotted = True

    @Slot()
    def importButton_Clicked(self):
        importType = self.ui.importTypeComboBox.currentText()
        if importType.upper() == "CSV":
            self.importCSV()
        elif importType.upper() == "IMAGE":
            self.importImage()
        elif importType.upper() == "DICOM":
            self.importDICOM()

    @Slot(float)
    def scrollValueChanged(self, newval):
        if self.plotted:
            self.scroll.set_xdata([newval])

            # Change the position of the gain to be relative to the scroll
            self.gainLeft.set_xdata([newval + self.ui.gainSlider.value()])
            self.gainRight.set_xdata([newval - self.ui.gainSlider.value()])

            self.canvas.draw()

    @Slot(float)
    def gainValueChanged(self, newval):
        if self.plotted:
            self.gainLeft.set_xdata([self.ui.scrollSlider.value() - newval])
            self.gainRight.set_xdata([self.ui.scrollSlider.value() + newval])
            self.canvas.draw()

    @Slot()
    def colorSettingsActionClicked(self):
        if self.plotted:
            settingsDialog = ColorSettingsDialog(self, self.graphBarColor)
            settingsDialog.dataReady.connect(self.graphColorChanged)
            settingsDialog.exec()

    @Slot(str)
    def graphColorChanged(self, new_color):
        if self.plotted:
            if self.ui.importTypeComboBox.currentText().upper() != "IMAGE":
                for i in range(len(self.barContainer[0])):
                    self.barContainer[2][i].set_color(new_color)
                self.polygon[0].set_color(new_color)
                self.graphBarColor = new_color
                self.canvas.draw()
            else:
                for i in range(len(self.barContainer)):
                    self.barContainer[i].set_color(new_color)
                self.polygon[0].set_color(new_color)
                self.graphBarColor = new_color
                self.canvas.draw()

    # Non-slot member functions
    def importCSV(self):
        # Clear
        self.clearPlots()

        # Open and display csv
        filename = QFileDialog.getOpenFileName(self, "Select CSV", os.getcwd(), "CSV(*.csv)")
        if filename != ('', ''):
            # Get plot data in csv
            frame = pd.read_csv(filename[0])
            data = frame['Value']
            self.drawHistAndFreq(data)
        else:
            self.plotted = False

    def importImage(self):
        # Clear
        self.clearPlots()

        # Open and display image
        filename = QFileDialog.getOpenFileName(self, "Select image", os.getcwd(),
                                               "Images(*.jpg *.png *.bmp)")
        if filename != ('', ''):
            # Open the image
            image = Image.open(filename[0])

            # Convert it to grayscale
            image = image.convert("L")

            # Get the intensities in a list
            data = image.histogram()

            # Plot histogram
            self.barContainer = self.axes_histPlot.bar(x=range(256), height=data, width=0.5,
                                   color=self.graphBarColor)

            # Plot cumulative frequency
            counts = np.cumsum(data)
            self.polygon = self.axes_cumFreqPlot.plot(counts, color=self.graphBarColor)

            # Reset the scroll and gain to the center
            self.scroll.set_xdata([117.5])
            self.gainLeft.set_xdata([97.5])
            self.gainRight.set_xdata([137.5])
            self.ui.gainSlider.setValue(20)
            self.ui.scrollSlider.setValue(117)
            self.ui.gainSlider.setMaximum(len(data))
            self.ui.scrollSlider.setMaximum(len(data))

            self.canvas.figure.tight_layout()
            self.canvas.draw()
            self.plotted = True

            # Show the stats
            self.showStatistics(data)

    def drawHistAndFreq(self, data, typeData="csv"):
        # Determine the bin size. 511 for DICOM images
        num_bins = 256
        if typeData == "DICOM":
            num_bins = 512
            self.ui.scrollSlider.setSingleStep(10)
            data = np.apply_along_axis(lambda x: (x / 16384) * 512, 0, data)

        # Histogram graph
        self.barContainer = self.axes_histPlot.hist(data, bins=num_bins, color=self.graphBarColor)

        # Cumulative frequency graph
        counts, bins = np.histogram(data, bins=num_bins)
        cumsum = np.cumsum(counts)
        self.polygon = self.axes_cumFreqPlot.plot(cumsum, color=self.graphBarColor)

        # Reset the scroll and gain to the center
        self.scroll.set_xdata([data.max() / 2])
        self.gainLeft.set_xdata([(data.max() / 2) - 10])
        self.gainRight.set_xdata([(data.max() / 2) + 10])
        self.ui.gainSlider.setMaximum(data.max())
        self.ui.gainSlider.setValue(10)
        self.ui.scrollSlider.setMaximum(data.max())
        self.ui.scrollSlider.setValue(data.max() / 2)

        self.canvas.figure.tight_layout()

        self.canvas.draw()
        self.plotted = True

        # Show the stats
        statsDict = {
            "max": int(bins[np.argmax(counts)]),
            "mean": np.mean(data).__round__(2),
            "std": np.std(data).__round__(2)
        }

        self.statsWindow = statsUI(self, statsDict)
        self.statsWindow.setWindowIcon(QPixmap("logo.ico"))
        self.statsWindow.show()

    def importDICOM(self):
        # Clear
        self.clearPlots()

        # Open and display image
        filename = QFileDialog.getOpenFileName(self, "Select image", os.getcwd(), "DICOM(*.dcm *.DCM)")
        if filename != ('', ''):
            image = pydicom.dcmread(filename[0])
            pixel_data = image.pixel_array.flatten()

            self.drawHistAndFreq(pixel_data, "DICOM")

    def showStatistics(self, counts, max=None):
        statsDict = {}
        if max is None:
            statsDict = {
                "max": self.getMax(list(counts)),
                "mean": self.getMean(list(counts)),
                "std": self.getSTD(list(counts))
            }
        else:
            statsDict = {
                "max": max,
                "mean": self.getMean(list(counts)),
                "std": self.getSTD(list(counts))
            }

        self.statsWindow = statsUI(self, statsDict)
        self.statsWindow.setWindowIcon(QPixmap("logo.ico"))
        self.statsWindow.show()

    def getMax(self, counts):
        maxNum = 0
        maxIndex = 0
        for i in range(len(counts)):
            if counts[i] > maxNum:
                maxNum = counts[i]
                maxIndex = i
        return maxIndex

    def getMean(self, counts):
        mean = 0
        numPixels = 0
        for i in range(len(counts)):
            mean += i * counts[i]
            numPixels += counts[i]
        mean /= numPixels
        return mean.__round__(2)

    def getSTD(self, counts):
        mean = self.getMean(counts)
        numerator = 0
        numPixels = 0
        for i in range(len(counts)):
            numerator += counts[i] * ((i - mean)**2)
            numPixels += counts[i]
        var = numerator / numPixels
        return math.sqrt(var).__round__(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
