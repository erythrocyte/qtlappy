#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

import matplotlib
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.__base_scale = 1.0
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        self.__press = None
        super(MplCanvas, self).__init__(self.fig)

        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')

        self.connect()

    def connect(self):
        self.cidscroll = self.fig.canvas.mpl_connect(
            'scroll_event', self.on_scroll_event)
        self.cidpress = self.fig.canvas.mpl_connect('button_press_event',
                                                    self.on_button_press_event)
        self.cidrelease = self.fig.canvas.mpl_connect('button_release_event',
                                                      self.on_button_release_event)
        self.cidmotion = self.fig.canvas.mpl_connect('motion_notify_event',
                                                     self.on_motion_notify_event)

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
        if event.inaxes != self.axes:
            return

        if event.button == 3:  # right click
            self.__press = event.xdata, event.ydata

    def on_motion_notify_event(self, event):
        toolbar = self.axes.get_figure().canvas.toolbar
        toolbar.push_current()  # stay at home
        if self.__press is None:
            return
        if event.inaxes != self.axes:
            return

        xpress, ypress = self.__press
        dx = event.xdata - xpress
        dy = event.ydata - ypress

        cur_xlim = self.axes.get_xlim()
        cur_ylim = self.axes.get_ylim()

        new_xlim = cur_xlim[0] - dx, cur_xlim[1] - dx
        new_ylim = cur_ylim[0] - dy, cur_ylim[1] - dy

        # set new limits
        self.axes.set_xlim(new_xlim)
        self.axes.set_ylim(new_ylim)

        self.draw()

    def on_button_release_event(self, event):
        self.__press = None
        self.draw()
