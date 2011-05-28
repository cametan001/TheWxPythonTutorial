#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# slider.py

import wx

class Slider(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (300, 150))

        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.sld = wx.Slider(panel, -1, 200, 150, 500, (-1, -1), (250, -1), \
                             wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_LABELS)
        btn1 = wx.Button(panel, 1, 'Adjust')
        btn2 = wx.Button(panel, 2, 'Close')

        wx.EVT_BUTTON(self, 1, self.OnOk)
        wx.EVT_BUTTON(self, 2, self.OnClose)

        vbox.Add(self.sld, 1, wx.ALIGN_CENTRE)
        hbox.Add(btn1, 1, wx.RIGHT, 10)
        hbox.Add(btn2, 1)
        vbox.Add(hbox, 0, wx.ALIGN_CENTRE | wx.ALL, 20)
        panel.SetSizer(vbox)
        self.Center()
        self.Show(True)

    def OnOk(self, event):
        val = self.sld.GetValue()
        self.SetSize((val * 2, val))

    def OnClose(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    Slider(None, -1, 'slider.py')
    app.MainLoop()
