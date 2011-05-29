#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# worldtime.py

import wx, time

class WorldTime(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (270, 280))

        self.panel = wx.Panel(self, -1)
        self.panel.SetBackgroundColour('#000000')
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, \
                       wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, 'Georgia')

        self.dt = wx.DateTime()

        self.tokyo = wx.StaticText(self.panel, -1, \
                                   self.dt.FormatTime(), (20, 20))
        self.tokyo.SetForegroundColour('#23f002')
        self.tokyo.SetFont(font)

        self.moscow = wx.StaticText(self.panel, -1, \
                                   self.dt.FormatTime(), (20, 70))
        self.moscow.SetForegroundColour('#23f002')
        self.moscow.SetFont(font)

        self.budapest = wx.StaticText(self.panel, -1, \
                                   self.dt.FormatTime(), (20, 120))
        self.budapest.SetForegroundColour('#23f002')
        self.budapest.SetFont(font)

        self.london = wx.StaticText(self.panel, -1, \
                                   self.dt.FormatTime(), (20, 170))
        self.london.SetForegroundColour('#23f002')
        self.london.SetFont(font)

        self.newyork = wx.StaticText(self.panel, -1, \
                                   self.dt.FormatTime(), (20, 220))
        self.newyork.SetForegroundColour('#23f002')
        self.newyork.SetFont(font)

        self.OnTimer(None)

        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)

        self.Center()
        self.Show(True)

    def OnTimer(self, event):
        now = self.dt.Now()
        self.tokyo.SetLabel('Tokyo: ' + now.Format(('%a %T'), \
                                                   wx.DateTime.GMT9))
        self.moscow.SetLabel('Moscow: ' + now.Format(('%a %T'), \
                                                       wx.DateTime.MSD))
        self.budapest.SetLabel('Budapest: ' + now.Format(('%a %T'), \
                                                       wx.DateTime.CEST))
        self.london.SetLabel('London: ' + now.Format(('%a %T'), \
                                                       wx.DateTime.WEST))
        self.newyork.SetLabel('New York: ' + now.Format(('%a %T'), \
                                                       wx.DateTime.EDT))

if __name__ == '__main__':
    app = wx.App()
    WorldTime(None, -1, 'World Time')
    app.MainLoop()
