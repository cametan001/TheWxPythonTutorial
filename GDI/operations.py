#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# operations.py

import wx

class Operations(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (270, 220))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen('#d4d4d4'))

        dc.DrawRectangle(20, 20, 50, 50)
        dc.DrawRectangle(30, 40, 50, 50)

        dc.SetBrush(wx.Brush('#ffffff'))
        dc.DrawRectangle(100, 20, 50, 50)
        dc.DrawRectangle(110, 40, 50, 50)
        region1 = wx.Region(100, 20, 50, 50)
        region2 = wx.Region(110, 40, 50, 50)
        region1.IntersectRegion(region2)
        rect = region1.GetBox()
        dc.SetClippingRegionAsRegion(region1)
        dc.SetBrush(wx.Brush('#ff0000'))
        dc.DrawRectangleRect(rect)
        dc.DestroyClippingRegion()

        dc.SetBrush(wx.Brush('#ffffff'))
        dc.DrawRectangle(180, 20, 50, 50)
        dc.DrawRectangle(190, 40, 50, 50)
        region1 = wx.Region(180, 20, 50, 50)
        region2 = wx.Region(190, 40, 50, 50)
        region1.UnionRegion(region2)
        dc.SetClippingRegionAsRegion(region1)
        rect = region1.GetBox()
        dc.SetBrush(wx.Brush('#fa8e00'))
        dc.DrawRectangleRect(rect)
        dc.DestroyClippingRegion()

        dc.SetBrush(wx.Brush('#ffffff'))
        dc.DrawRectangle(20, 120, 50, 50)
        dc.DrawRectangle(30, 140, 50, 50)
        region1 = wx.Region(20, 120, 50, 50)
        region2 = wx.Region(30, 140, 50, 50)
        region1.XorRegion(region2)
        rect = region1.GetBox()
        dc.SetClippingRegionAsRegion(region1)
        dc.SetBrush(wx.Brush('#619e1b'))
        dc.DrawRectangleRect(rect)
        dc.DestroyClippingRegion()

        dc.SetBrush(wx.Brush('#ffffff'))
        dc.DrawRectangle(100, 120, 50, 50)
        dc.DrawRectangle(110, 140, 50, 50)
        region1 = wx.Region(100, 120, 50, 50)
        region2 = wx.Region(110, 140, 50, 50)
        region1.SubtractRegion(region2)
        rect = region1.GetBox()
        dc.SetClippingRegionAsRegion(region1)
        dc.SetBrush(wx.Brush('#715b33'))
        dc.DrawRectangleRect(rect)
        dc.DestroyClippingRegion()

        dc.SetBrush(wx.Brush('#ffffff'))
        dc.DrawRectangle(180, 120, 50, 50)
        dc.DrawRectangle(190, 140, 50, 50)
        region1 = wx.Region(180, 120, 50, 50)
        region2 = wx.Region(190, 140, 50, 50)
        region1.SubtractRegion(region1)
        rect = region2.GetBox()
        dc.SetClippingRegionAsRegion(region2)
        dc.SetBrush(wx.Brush('#0d0060'))
        dc.DrawRectangleRect(rect)
        dc.DestroyClippingRegion()
        

if __name__ == '__main__':
    app = wx.App()
    Operations(None, -1, 'Operations')
    app.MainLoop()
