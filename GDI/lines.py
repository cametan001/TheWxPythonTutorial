#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# lines.py

import wx
from math import hypot, sin, cos, pi

class Lines(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (450, 400))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        size_x, size_y = self.GetClientSizeTuple()
        dc.SetDeviceOrigin(size_x / 2, size_y / 2)

        radius = hypot(size_x / 2, size_y / 2)
        angle = 0

        while (angle < 2 * pi):
            x = radius * cos(angle)
            y = radius * sin(angle)
            dc.DrawLinePoint((0, 0), (x, y))
            angle = angle + 2 * pi / 360

if __name__ == '__main__':
    app = wx.App()
    Lines(None, -1, 'Lines')
    app.MainLoop()
