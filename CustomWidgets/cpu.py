#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# cpu.py

import wx

class CPU(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, size = (80, 110))

        self.parent = parent

        self.SetBackgroundColour('#000000')

        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        dc.SetDeviceOrigin(0, 100)
        dc.SetAxisOrientation(True, True)

        pos = self.parent.GetParent().GetParent().sel
        rect = pos / 5

        for i in range(1, 21):
            if i > rect:
                dc.SetBrush(wx.Brush('#075100'))
                dc.DrawRectangle(10, i * 4, 30, 5)
                dc.DrawRectangle(41, i * 4, 30, 5)
            else:
                dc.SetBrush(wx.Brush('#36ff27'))
                dc.DrawRectangle(10, i * 4, 30, 5)
                dc.DrawRectangle(41, i * 4, 30, 5)

class CPUWidget(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (190, 140))

        self.sel = 0

        panel = wx.Panel(self, -1)
        centerPanel = wx.Panel(panel, -1)

        self.cpu = CPU(centerPanel, -1)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.slider = wx.Slider(panel, -1, self.sel, 0, 100, (-1, -1), (25, 90), \
                                wx.VERTICAL | wx.SL_LABELS | wx.SL_INVERSE)
        self.slider.SetFocus()

        hbox.Add(centerPanel, 0, wx.LEFT | wx.TOP, 20)
        hbox.Add(self.slider, 0, wx.LEFT | wx.TOP, 23)

        self.Bind(wx.EVT_SCROLL, self.OnScroll)

        panel.SetSizer(hbox)

        self.Center()
        self.Show(True)

    def OnScroll(self, event):
        self.sel = event.GetInt()
        self.cpu.Refresh()

if __name__ == '__main__':
    app = wx.App()
    CPUWidget(None, -1, 'cpu')
    app.MainLoop()
