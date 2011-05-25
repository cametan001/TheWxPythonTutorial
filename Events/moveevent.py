#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# moveevent.py

import wx

class MoveEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 180))

        wx.StaticText(self, -1, 'x:', (10, 10))
        wx.StaticText(self, -1, 'y:', (10, 30))
        self.st1 = wx.StaticText(self, -1, '', (30, 10))
        self.st2 = wx.StaticText(self, -1, '', (30, 30))

        self.Bind(wx.EVT_MOVE, self.OnMove)

        self.Center()
        self.Show(True)

    def OnMove(self, event):
        x, y = event.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))

if __name__ == '__main__':
    app = wx.App()
    MoveEvent(None, -1, 'move event')
    app.MainLoop()
