#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import wx

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title = title, \
                                      size = (250, 150))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Center()
        self.Show()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawLine(50, 60, 190, 60)

if __name__ == '__main__':
    app = wx.App()
    Example(None, 'Line')
    app.MainLoop()
