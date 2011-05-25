#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# buttons.py

import wx, random

APP_SIZE_X = 300
APP_SIZE_Y = 200

class MyButtons(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size = (APP_SIZE_X, APP_SIZE_Y))

        wx.Button(self, 1, 'Close', (50, 130))
        wx.Button(self, 2, 'Random Move', (150, 130), (110, -1))

        self.Bind(wx.EVT_BUTTON, self.OnClose, id = 1)
        self.Bind(wx.EVT_BUTTON, self.OnRandomMove, id = 2)

        self.Center()
        self.ShowModal()
        self.Destroy()

    def OnClose(self, event):
        self.Close(True)

    def OnRandomMove(self, event):
        screensize = wx.GetDisplaySize()
        randx = random.randrange(0, screensize.x - APP_SIZE_X)
        randy = random.randrange(0, screensize.y - APP_SIZE_Y)
        self.Move((randx, randy))


if __name__ == '__main__':
    app = wx.App(0)
    MyButtons(None, -1, 'buttons.py')
    app.MainLoop()
