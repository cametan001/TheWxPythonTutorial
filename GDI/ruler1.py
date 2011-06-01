#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# ruler1.py

import wx, os.path

RW = 701                                # ruler width
RM = 10                                 # ruler margin
RH = 60                                 # ruler height

class Ruler1(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (RW + 2 * RM, 60), \
                          style = wx.FRAME_NO_TASKBAR | wx.NO_BORDER | wx.STAY_ON_TOP)
        self.font = wx.Font(7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, \
                            wx.FONTWEIGHT_BOLD, False, 'Courier 10 Pitch')

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)

        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        brush = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/granite.jpg')))
        dc.SetBrush(brush)
        dc.DrawRectangle(0, 0, RW + 2 * RM, RH)
        dc.SetFont(self.font)

        dc.SetPen(wx.Pen('#F8FF25'))
        dc.SetTextForeground('#F8ff25')

        for i in range(RW):
            if not (i % 100):
                dc.DrawLine(i + RM, 0, i + RM, 10)
                w, h = dc.GetTextExtent(str(i))
                dc.DrawText(str(i), i + RM - w / 2, 11)
            elif not (i % 20):
                dc.DrawLine(i + RM, 0, i + RM, 8)
            elif not (i % 2): dc.DrawLine(i + RM, 0, i + RM, 4)

    def OnLeftDown(self, event):
        pos = event.GetPosition()
        x, y = self.ClientToScreen(event.GetPosition())
        ox, oy = self.GetPosition()
        dx = x - ox
        dy = y - oy
        self.delta = ((dx, dy))

    def OnMouseMove(self, event):
        if event.Dragging() and event.LeftIsDown():
            x, y = self.ClientToScreen(event.GetPosition())
            fp = (x - self.delta[0], y - self.delta[1])
            self.Move(fp)

    def OnRightDown(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    Ruler1(None, -1, '')
    app.MainLoop()
