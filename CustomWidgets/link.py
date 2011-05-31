#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# link.py

import wx
from wx.lib.stattext import GenStaticText
import webbrowser

class Link(GenStaticText):
    def __init__(self, parent, id = 1, label = '', pos = (-1, -1), \
                 size = (-1, -1), style = 0, name = 'Link', URL = ''):

        GenStaticText.__init__(self, parent, id, label, pos, size, style, name)

        self.url = URL

        self.font1 = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, True, 'Verdana')
        self.font2 = wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Verdana')

        self.SetFont(self.font2)
        self.SetForegroundColour('#0000ff')

        self.Bind(wx.EVT_MOUSE_EVENTS, self.OnMouseEvent)
        self.Bind(wx.EVT_MOTION, self.OnMouseEvent)

    def OnMouseEvent(self, event):
        if event.Moving():
            self.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
            self.SetFont(self.font1)

        elif event.LeftUp():
            webbrowser.open_new(self.url)
        else:
            self.SetCursor(wx.NullCursor)
            self.SetFont(self.font2)

        event.Skip()

class HyperLink(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (220, 150))

        panel = wx.Panel(self, -1)
        Link(panel, -1, 'ZetCode', pos = (10, 60), URL = 'http://www.zetcode.com')
        motto = GenStaticText(panel, -1, 'Knowledge only matters', pos = (10, 30))
        motto.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False, 'Verdana'))

        self.Center()
        self.Show(True)
            

if __name__ == '__main__':
    app = wx.App()
    HyperLink(None, -1, 'A Hyperlink')
    app.MainLoop()
