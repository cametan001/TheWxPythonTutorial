#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# sizeevent.py

import wx

class SizeEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Center()
        self.Show(True)

    def OnSize(self, event):
        self.SetTitle(str(event.GetSize()))

if __name__ == '__main__':
    app = wx.App()
    SizeEvent(None, 1, 'sizeevent.py')
    app.MainLoop()
