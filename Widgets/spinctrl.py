#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# spinctrl.py

import wx

class Converter(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size = (350, 310))

        wx.StaticText(self, -1, 'Convert Fahrenheit temperature to Celsius', (20, 20))
        wx.StaticText(self, -1, 'Fahrenheit: ', (20, 80))
        wx.StaticText(self, -1, 'Celsius: ', (20, 150))
        self.celsius = wx.StaticText(self, -1, '', (150, 150))
        self.sc = wx.SpinCtrl(self, -1, '', (150, 75), (60, -1))
        self.sc.SetRange(-459, 1000)
        self.sc.SetValue(0)
        compute_btn = wx.Button(self, 1, 'Compute', (70, 250))
        compute_btn.SetFocus()
        clear_btn = wx.Button(self, 2, 'Close', (185, 250))

        wx.EVT_BUTTON(self, 1, self.OnCompute)
        wx.EVT_BUTTON(self, 2, self.OnClose)
        wx.EVT_CLOSE(self, self.OnClose)

        self.Center()
        self.ShowModal()
        self.Destroy()

    def OnCompute(self, event):
        fahr = self.sc.GetValue()
        cels = round((fahr - 32) * 5/9.0, 2)
        self.celsius.SetLabel(str(cels))

    def OnClose(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.App()
    Converter(None, -1, 'Converter')
    app.MainLoop()
