#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# automaticids.py

import wx

class AuIds(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (170, 100))

        panel = wx.Panel(self, -1)
        exit = wx.Button(panel, -1, 'Exit', (10, 10))

        self.Bind(wx.EVT_BUTTON, self.OnExit, id = exit.GetId())

        self.Center()
        self.Show(True)

    def OnExit(self, event):
        self.Close()

        

if __name__ == '__main__':
    app = wx.App()
    AuIds(None, -1, '')
    app.MainLoop()
