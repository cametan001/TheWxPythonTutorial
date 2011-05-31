#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# gradients.py

import wx

class Gradients(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (220, 260))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        dc.GradientFillLinear((20, 20, 180, 40), '#ffec00', '#000000', wx.NORTH)
        dc.GradientFillLinear((20, 80, 180, 40), '#ffec00', '#000000', wx.SOUTH)
        dc.GradientFillLinear((20, 140, 180, 40), '#ffec00', '#000000', wx.EAST)
        dc.GradientFillLinear((20, 200, 180, 40), '#ffec00', '#000000', wx.WEST)

if __name__ == '__main__':
    app = wx.App()
    Gradients(None, -1, 'Gradients')
    app.MainLoop()
