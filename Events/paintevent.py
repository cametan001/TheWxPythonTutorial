#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# paintevent.py

import wx

class PaintEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.count = 0
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        self.count += 1
        print self.count

if __name__ == '__main__':
    app = wx.App()
    PaintEvent(None, -1, 'paintevent.py')
    app.MainLoop()
