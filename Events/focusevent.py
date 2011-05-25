#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# focusevent.py

import wx

class MyWindow(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        self.color = '#b3b3b3'

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen(self.color))
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)

    def OnSize(self, event):
        self.Refresh()

    def OnSetFocus(self, event):
        self.color = '#0099f7'
        self.Refresh()

    def OnKillFocus(self, event):
        self.color = '#b3b3b3'
        self.Refresh()

class FocusEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (350, 250))

        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([(MyWindow(self), 1, wx.EXPAND | wx.TOP | wx.LEFT, 9), \
                      (MyWindow(self), 1, wx.EXPAND | wx.TOP | wx.RIGHT, 9), \
                      (MyWindow(self), 1, wx.EXPAND | wx.BOTTOM | wx.LEFT, 9), \
                      (MyWindow(self), 1, wx.EXPAND | wx.BOTTOM | wx.RIGHT, 9)])

        self.SetSizer(grid)
        self.Center()
        self.Show(True)
        
if __name__ == '__main__':
    app = wx.App()
    FocusEvent(None, -1, 'focus event')
    app.MainLoop()
