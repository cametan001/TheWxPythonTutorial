#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# identifiers.py

import wx

class Identifiers(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (200, 150))

        panel = wx.Panel(self, -1)
        grid = wx.GridSizer(3, 2)

        grid.AddMany([(wx.Button(panel, wx.ID_CANCEL), 0, wx.TOP | wx.LEFT, 9), \
                      (wx.Button(panel, wx.ID_DELETE), 0, wx.TOP, 9), \
                      (wx.Button(panel, wx.ID_SAVE), 0, wx.LEFT, 9), \
                      (wx.Button(panel, wx.ID_EXIT)), \
                      (wx.Button(panel, wx.ID_STOP), 0, wx.LEFT, 9), \
                      (wx.Button(panel, wx.ID_NEW))])

        self.Bind(wx.EVT_BUTTON, self.OnQuit, id = wx.ID_EXIT)

        panel.SetSizer(grid)
        self.Center()
        self.Show(True)

    def OnQuit(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    Identifiers(None, -1, '')
    app.MainLoop()
