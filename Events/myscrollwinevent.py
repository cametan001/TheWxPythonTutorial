#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# myscrollwinevent.py

import wx

class ScrollWinEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        panel = wx.Panel(self, -1)
        self.st = wx.StaticText(panel, -1, '0', (30, 0))
        panel.Bind(wx.EVT_SCROLLWIN, self.OnScroll)
        panel.SetScrollbar(wx.VERTICAL, 0, 6, 50)
        self.Center()
        self.Show(True)

    def OnScroll(self, event):
        y = event.GetPosition()
        self.st.SetLabel(str(y))

if __name__ == '__main__':
    app = wx.App()
    ScrollWinEvent(None, -1, 'scrollwinevent.py')
    app.MainLoop()
