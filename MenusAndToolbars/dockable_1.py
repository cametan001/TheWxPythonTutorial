#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# dockable_1.py

import wx

class Dockable(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        d = {}

        menubar = wx.MenuBar(wx.MB_DOCKABLE)
        keys = [['file', '&File'], ['edit', '&Edit'], ['view', '&View'], \
                ['insr', '&Insert'], ['form', '&Format'], ['tool', '&Tools'], ['help', '&Help']]
        for key in keys:
            d[key[0]] = wx.Menu()
            menubar.Append(d[key[0]], key[1])

        self.SetMenuBar(menubar)

        self.Center()
        self.Show(True)
            
if __name__ == '__main__':
    app = wx.App()
    Dockable(None, -1, 'Dockable menubar')
    app.MainLoop()
