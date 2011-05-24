#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# sizer.py

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title = title, \
                                      size = (260, 180))

        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):

        menubar = wx.MenuBar()
        filem = wx.Menu()
        editm = wx.Menu()
        helpm = wx.Menu()

        menubar.Append(filem, '&File')
        menubar.Append(editm, '&Edit')
        menubar.Append(helpm, '&Help')
        self.SetMenuBar(menubar)

        wx.TextCtrl(self)

if __name__ == '__main__':
    app = wx.App()
    Example(None, title = '')
    app.MainLoop()
