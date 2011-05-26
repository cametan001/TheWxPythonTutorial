#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# staticbox.py

import wx

class StaticBox(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size = (250, 230))

        wx.StaticBox(self, -1, 'Personal Info', (5, 5), size = (240, 170))
        wx.CheckBox(self, -1, 'Male', (15, 30))
        wx.CheckBox(self, -1, 'Married', (15, 55))
        wx.StaticText(self, -1, 'Age', (15, 95))
        wx.SpinCtrl(self, -1, '1', (55, 90), (60, -1), min = 1, max = 120)
        wx.Button(self, 1, 'Ok', (90, 185), (60, -1))

        self.Bind(wx.EVT_BUTTON, self.OnClose, id = 1)

        self.Center()
        self.ShowModal()
        self.Destroy()

    def OnClose(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    StaticBox(None, -1, 'staticbox.py')
    app.MainLoop()
