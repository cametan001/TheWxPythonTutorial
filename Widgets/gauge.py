#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# gauge.py

import wx

class Gauge(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (300, 200))

        self.timer = wx.Timer(self, 1)
        self.count = 0

        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        self.gauge = wx.Gauge(panel, -1, 50, size = (250, 25))
        self.btn1 = wx.Button(panel, wx.ID_OK)
        self.btn2 = wx.Button(panel, wx.ID_STOP)
        self.text = wx.StaticText(panel, -1, 'Task to be done')

        self.Bind(wx.EVT_BUTTON, self.OnOk, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.btn2)

        hbox1.Add(self.gauge, 1, wx.ALIGN_CENTRE)
        hbox2.Add(self.btn1, 1, wx.RIGHT, 10)
        hbox2.Add(self.btn2, 1)
        hbox3.Add(self.text, 1)
        vbox.Add((0, 30), 0)
        vbox.Add(hbox1, 0, wx.ALIGN_CENTRE)
        vbox.Add((0, 20), 0)
        vbox.Add(hbox2, 1, wx.ALIGN_CENTRE)
        vbox.Add(hbox3, 1, wx.ALIGN_CENTRE)

        panel.SetSizer(vbox)
        self.Center()
        self.Show(True)

    def OnOk(self, event):
        if self.count >= 50:
            return
        self.timer.Start(100)
        self.text.SetLabel('Task in Progress')

    def OnStop(self, event):
        if self.count == 0 or self.count >= 50 or not self.timer.IsRunning():
            return
        self.timer.Stop()
        self.text.SetLabel('Task Interrupted')
        wx.Bell()

    def OnTimer(self, event):
        self.count += 1
        self.gauge.SetValue(self.count)
        if self.count == 50:
            self.timer.Stop()
            self.text.SetLabel('Task Completed')
        
if __name__ == '__main__':
    app = wx.App()
    Gauge(None, -1, 'gauge.py')
    app.MainLoop()
