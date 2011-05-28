#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# splitterwindow.py

import wx

class Splitterwindow(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (350, 300))

        quote = '''Whether you think that you can, or that you can\'t, you are \
                usually right'''

        splitter = wx.SplitterWindow(self, -1)
        panel1 = wx.Panel(splitter, -1)
        wx.StaticText(panel1, -1, quote, (100, 100), style = wx.ALIGN_CENTRE)

        panel1.SetBackgroundColour(wx.LIGHT_GREY)
        panel2 = wx.Panel(splitter, -1)
        panel2.SetBackgroundColour(wx.WHITE)
        splitter.SplitVertically(panel1, panel2)
        self.Center()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App()
    Splitterwindow(None, -1, 'splitterwindow.py')
    app.MainLoop()
