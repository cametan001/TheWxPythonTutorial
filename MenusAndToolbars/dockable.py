#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# dockable.py

import wx

class Dockable(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        menubar = wx.MenuBar(wx.MB_DOCKABLE)
        file = wx.Menu()
        edit = wx.Menu()
        view = wx.Menu()
        insr = wx.Menu()
        form = wx.Menu()
        tool = wx.Menu()
        help = wx.Menu()

        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(view, '&View')
        menubar.Append(insr, '&Insert')
        menubar.Append(form, '&Format')
        menubar.Append(tool, '&Tools')
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)

        self.Center()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App()
    Dockable(None, -1, 'Dockable menubar')
    app.MainLoop()
