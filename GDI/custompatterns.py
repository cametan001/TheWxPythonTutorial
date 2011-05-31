#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# custompatterns.py

import wx, os.path

class CustomPatterns(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (350, 280))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen('#C7C3C3'))

        brush1 = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/pattern1.png')))
        dc.SetBrush(brush1)
        dc.DrawRectangle(10, 15, 90, 60)

        brush2 = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/pattern2.png')))
        dc.SetBrush(brush2)
        dc.DrawRectangle(130, 15, 90, 60)

        brush3 = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/pattern3.png')))
        dc.SetBrush(brush3)
        dc.DrawRectangle(250, 15, 90, 60)

        brush4 = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/pattern4.png')))
        dc.SetBrush(brush4)
        dc.DrawRectangle(10, 105, 90, 60)

        brush5 = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/pattern5.png')))
        dc.SetBrush(brush5)
        dc.DrawRectangle(130, 105, 90, 60)

        brush6 = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/pattern6.png')))
        dc.SetBrush(brush6)
        dc.DrawRectangle(250, 105, 90, 60)

        brush7 = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/pattern7.png')))
        dc.SetBrush(brush7)
        dc.DrawRectangle(10, 195, 90, 60)

        brush8 = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/pattern8.png')))
        dc.SetBrush(brush8)
        dc.DrawRectangle(130, 195, 90, 60)

        brush9 = wx.BrushFromBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/pattern9.png')))
        dc.SetBrush(brush9)
        dc.DrawRectangle(250, 195, 90, 60)
        
if __name__ == '__main__':
    app = wx.App()
    CustomPatterns(None, -1, 'Custom Patterns')
    app.MainLoop()
