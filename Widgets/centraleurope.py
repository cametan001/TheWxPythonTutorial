#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# centraleurope.py

import wx

class CentralEurope(wx.Dialog):
    def __init__(self, parent, ID, title):
        wx.Dialog.__init__(self, parent, ID, title, size = (360, 370))

        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, -1, 'The Central Europe', (130, 15))
        heading.SetFont(font)

        wx.StaticLine(self, -1, (25, 50), (300, 1))

        wx.StaticText(self, -1, 'Slovakia', (25, 80))
        wx.StaticText(self, -1, 'Hungary', (25, 100))
        wx.StaticText(self, -1, 'Poland', (25, 120))
        wx.StaticText(self, -1, 'Czech Republic', (25, 140))
        wx.StaticText(self, -1, 'Germany', (25, 160))
        wx.StaticText(self, -1, 'Slovenia', (25, 180))
        wx.StaticText(self, -1, 'Austria', (25, 200))
        wx.StaticText(self, -1, 'Switzerland', (25, 220))

        wx.StaticText(self, -1, '5 379 000', (250, 80))
        wx.StaticText(self, -1, '10 084 000', (250, 100))
        wx.StaticText(self, -1, '38 635 000', (250, 120))
        wx.StaticText(self, -1, '10 240 000', (250, 140))
        wx.StaticText(self, -1, '82 443 000', (250, 160))
        wx.StaticText(self, -1, '2 001 000', (250, 180))
        wx.StaticText(self, -1, '8 032 000', (250, 200))
        wx.StaticText(self, -1, '7 288 000', (250, 220))

        wx.StaticLine(self, -1, (25, 260), (300, 1))

        sum = wx.StaticText(self, -1, '164 102 000', (240, 280))
        sum_font = sum.GetFont()
        sum_font.SetWeight(wx.BOLD)
        sum.SetFont(sum_font)

        wx.Button(self, 1, 'Ok', (140, 310), (60, 30))

        self.Bind(wx.EVT_BUTTON, self.OnOk, id = 1)

        self.Center()
        self.ShowModal()
        self.Destroy()

    def OnOk(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    CentralEurope(None, -1, 'centraleurope.py')
    app.MainLoop()
