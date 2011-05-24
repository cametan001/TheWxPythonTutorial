#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# menuexample.py

import wx, os.path

class MenuExample(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 150))

        menubar = wx.MenuBar()
        file = wx.Menu()
        Quit = wx.MenuItem(file, 1, '&Quit/tCtrl+Q')
        Quit.SetBitmap(wx.Bitmap('icons/exit.png'))
        file.AppendItem(Quit)

        self.Bind(wx.EVT_MENU, self.OnQuit, id = 1)

        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)

        self.Center()
        self.Show(True)

    def OnQuit(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    MenuExample(None, -1, '')
    app.MainLoop()
