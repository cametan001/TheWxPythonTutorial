#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# toolbars.py

import wx, os.path

class Toolbars(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (300, 200))

        vbox = wx.BoxSizer(wx.VERTICAL)

        toolbar1 = wx.ToolBar(self, -1)
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/new.png')))
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/open.png')))
        toolbar1.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/save.png')))
        toolbar1.Realize

        toolbar2 = wx.ToolBar(self, -1)
        toolbar2.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/exit.png')))
        toolbar2.Realize()

        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.Add(toolbar2, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnExit, id = wx.ID_EXIT)

        self.SetSizer(vbox)
        self.Center()
        self.Show(True)

    def OnExit(self, event):
        self.Close()
        
if __name__ == '__main__':
    app = wx.App()
    Toolbars(None, -1, 'toolbars')
    app.MainLoop()
