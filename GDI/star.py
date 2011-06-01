#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# star.py

import wx
from math import hypot, sin, cos, pi

class Star(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (350, 300))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen('#424242'))
        size_x, size_y = self.GetClientSizeTuple()
        dc.SetDeviceOrigin(size_x / 2, size_y / 2)

        points = (((0, 85), (75, 75), (100, 10), (125, 75), (200, 85), \
                   (150, 125), (160, 190), (100, 150), (40, 190), (50, 125)))

        region = wx.RegionFromPoints(points)
        dc.SetClippingRegionAsRegion(region)

        radius = hypot(size_x / 2, size_y / 2)
        angle = 0

        while (angle < 2 * pi):
            x = radius * cos(angle)
            y = radius * sin(angle)
            dc.DrawLinePoint((0, 0), (x, y))
            angle += 2 * pi / 360

        dc.DestroyClippingRegion()

    

if __name__ == '__main__':
    app = wx.App()
    Star(None, -1, 'Star')
    app.MainLoop()
