#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

import matplotlib
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.__base_scale = 1.2
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

        fig.subplots_adjust(left=0.0, bottom=0.0, right=0.99, top=1.0)
        fig.canvas.mpl_connect('scroll_event', self.on_scroll_event)
        fig.canvas.mpl_connect('button_press_event',
                               self.on_button_press_event)

    def on_scroll_event(self, event):
        toolbar = self.axes.get_figure().canvas.toolbar
        toolbar.push_current()  # stay at home

        # get the current x and y limits
        cur_xlim = self.axes.get_xlim()
        cur_ylim = self.axes.get_ylim()

        xdata = event.xdata  # get event x location
        ydata = event.ydata  # get event y location

        # Get distance from the cursor to the edge of the figure frame
        x_left = xdata - cur_xlim[0]
        x_right = cur_xlim[1] - xdata
        y_top = ydata - cur_ylim[0]
        y_bottom = cur_ylim[1] - ydata

        if event.button == 'up':
            # deal with zoom in
            scale_factor = 1. / self.__base_scale
        elif event.button == 'down':
            # deal with zoom out
            scale_factor = self.__base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1.
            print(event.button)

        # set new limits
        self.axes.set_xlim([xdata - x_left*scale_factor,
                            xdata + x_right*scale_factor])
        self.axes.set_ylim([ydata - y_top*scale_factor,
                            ydata + y_bottom*scale_factor])
        self.draw()  # force re-draw

    def on_button_press_event(self, event):
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))
