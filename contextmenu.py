#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# contextmenu.py

import wx

class MyPopupMenu(wx.Menu):
    def __init__(self, parent):
        wx.Menu.__init__(self)

        self.parent = parent

        minimize = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.AppendItem(minimize)
        self.Bind(wx.EVT_MENU, self.OnMinimize, id = minimize.GetId())

        close = wx.MenuItem(self, wx.NewId(), 'Close')
        self.AppendItem(close)
        self.Bind(wx.EVT_MENU, self.OnClose, id = close.GetId())

    def OnMinimize(self, event):
        self.parent.Iconize()

    def OnClose(self, event):
        self.parent.Close()

class ContextMenu(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 150))

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.Center()
        self.Show()

    def OnRightDown(self, event):
        self.PopupMenu(MyPopupMenu(self), event.GetPosition())

if __name__ == '__main__':
    app = wx.App()
    frame = ContextMenu(None, -1, 'context menu')
    app.MainLoop()
