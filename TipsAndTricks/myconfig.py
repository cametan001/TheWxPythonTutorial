#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# myconfig.py

import wx

class MyConfig(wx.Frame):
    def __init__(self, parent, id, title):
        self.cfg = wx.Config('myconfig')
        if self.cfg.Exists('width'):
            w, h = self.cfg.ReadInt('width'), self.cfg.ReadInt('height')
        else:
            (w, h) = (250, 250)
        wx.Frame.__init__(self, parent, id, title, size = (w, h))

        wx.StaticText(self, -1, 'Width:', (20, 20))
        wx.StaticText(self, -1, 'Height:', (20, 70))
        self.sc1 = wx.SpinCtrl(self, -1, str(w), (80, 15), (60, -1), min = 200, max = 500)
        self.sc2 = wx.SpinCtrl(self, -1, str(h), (80, 65), (60, -1), min = 200, max = 500)
        wx.Button(self, 1, 'Save', (20, 120))

        self.Bind(wx.EVT_BUTTON, self.OnSave, id = 1)
        self.statusbar = self.CreateStatusBar()
        self.Center()
        self.Show(True)

    def OnSave(self, event):
        self.cfg.WriteInt("width", self.sc1.GetValue())
        self.cfg.WriteInt("height", self.sc2.GetValue())
        self.statusbar.SetStatusText('Configuration saved, %s ' % wx.Now())

if __name__ == '__main__':
    app = wx.App()
    MyConfig(None, -1, 'myconfig.py')
    app.MainLoop()
