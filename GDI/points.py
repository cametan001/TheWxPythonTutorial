#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# points.py

import wx, random

class Points(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 150))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen('RED'))

        for i in range(1000):
            w, h = self.GetSize()
            x = random.randint(1, w - 1)
            y = random.randint(1, h - 1)
            dc.DrawPoint(x, y)
            

if __name__ == '__main__':
    app = wx.App()
    Points(None, -1, 'Points')
    app.MainLoop()
