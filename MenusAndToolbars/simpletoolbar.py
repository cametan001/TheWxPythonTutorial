#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# simpletoolbar.py

import wx, os.path

class SimpleToolbar(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (300, 200))

        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/exit.png')))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnExit, id = wx.ID_EXIT)

        self.Center()
        self.Show(True)

    def OnExit(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    SimpleToolbar(None, -1, 'simple toolbar')
    app.MainLoop()
