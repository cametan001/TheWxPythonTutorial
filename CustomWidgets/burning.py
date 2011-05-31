#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# burning.py

import wx

class Widget(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, size = (-1, 30), style = wx.SUNKEN_BORDER)
        self.parent = parent
        self.font = wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, \
                            wx.FONTWEIGHT_NORMAL, False, 'Courier 10 Pitch')

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnPaint(self, event):
        num = range(75, 700, 75)
        dc = wx.PaintDC(self)
        dc.SetFont(self.font)
        w, h = self.GetSize()

        self.cw = self.parent.GetParent().cw

        step = int(round(w / 10.0))

        j = 0

        till = (w / 750.0) * self.cw
        full = (w / 750.0) * 700

        if self.cw >= 700:
            dc.SetPen(wx.Pen('#FFFFB8'))
            dc.SetBrush(wx.Brush('#FFFFB8'))
            dc.DrawRectangle(0, 0, full, 30)
            dc.SetPen(wx.Pen('#ffafaf'))
            dc.SetBrush(wx.Brush('#ffafaf'))
            dc.DrawRectangle(full, 0, till-full, 30)
        else:
            dc.SetPen(wx.Pen('#FFFFB8'))
            dc.SetBrush(wx.Brush('#FFFFB8'))
            dc.DrawRectangle(0, 0, till, 30)

        dc.SetPen(wx.Pen('#5c5142'))
        for i in range(step, 10 * step, step):
            width, height = dc.GetTextExtent(str(num[j]))
            dc.DrawText(str(num[j]), i - width/2, 8)
            j += 1

    def OnSize(self, event):
        self.Refresh()

class Burning(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (330, 200))

        self.cw = 75

        panel = wx.Panel(self, -1)
        CenterPanel = wx.Panel(panel, -1)
        self.sld = wx.Slider(CenterPanel, -1, 75, 0, 750, (-1, -1), (150, -1), wx.SL_LABELS)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        self.wid = Widget(panel, -1)
        hbox.Add(self.wid, 1, wx.EXPAND)

        hbox2.Add(CenterPanel, 1, wx.EXPAND)
        hbox3.Add(self.sld, 0, wx.TOP, 35)

        CenterPanel.SetSizer(hbox3)

        vbox.Add(hbox2, 1, wx.EXPAND)
        vbox.Add(hbox, 0, wx.EXPAND)

        self.Bind(wx.EVT_SCROLL, self.OnScroll)

        panel.SetSizer(vbox)

        self.sld.SetFocus()

        self.Center()
        self.Show(True)

    def OnScroll(self, event):
        self.cw = self.sld.GetValue()
        self.wid.Refresh()
        
if __name__ == '__main__':
    app = wx.App()
    Burning(None, -1, 'Burning widget')
    app.MainLoop()
