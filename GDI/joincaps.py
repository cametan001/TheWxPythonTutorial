#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# joinscaps.py

import wx

class JoinsCaps(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (330, 300))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        pen = wx.Pen('#4c4c4c', 10, wx.SOLID)

        pen.SetJoin(wx.JOIN_MITER)
        dc.SetPen(pen)
        dc.DrawRectangle(15, 15, 80, 50)

        pen.SetJoin(wx.JOIN_BEVEL)
        dc.SetPen(pen)
        dc.DrawRectangle(125, 15, 80, 50)

        pen.SetJoin(wx.JOIN_ROUND)
        dc.SetPen(pen)
        dc.DrawRectangle(235, 15, 80, 50)

        pen.SetJoin(wx.CAP_BUTT)
        dc.SetPen(pen)
        dc.DrawRectangle(30, 150, 150, 150)

        pen.SetJoin(wx.CAP_PROJECTING)
        dc.SetPen(pen)
        dc.DrawRectangle(30, 190, 150, 190)

        pen.SetJoin(wx.CAP_ROUND)
        dc.SetPen(pen)
        dc.DrawRectangle(30, 230, 150, 230)

        pen2 = wx.Pen('#4c4c4c', 1, wx.SOLID)
        dc.SetPen(pen2)
        dc.DrawLine(30, 130, 30, 250)
        dc.DrawLine(150, 130, 150, 250)
        dc.DrawLine(155, 130, 155, 250)

if __name__ == '__main__':
    app = wx.App()
    JoinsCaps(None, -1, 'Joins and Caps')
    app.MainLoop()
