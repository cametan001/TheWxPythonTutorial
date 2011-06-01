#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# interactivebutton.py

import wx
from wx.lib.buttons import GenButton

class InteractiveButton(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        panel = wx.Panel(self, -1)

        self.btn = GenButton(panel, -1, 'button', pos = (100, 100), size = (-1, -1))
        self.btn.SetBezelWidth(1)
        self.btn.SetBackgroundColour('DARKGREY')

        wx.EVT_ENTER_WINDOW(self.btn, self.func)
        wx.EVT_LEAVE_WINDOW(self.btn, self.func1)

        self.Center()
        self.Show(True)

    def func(self, event):
        self.btn.SetBackgroundColour('GREY79')
        self.btn.Refresh()

    def func1(self, event):
        self.btn.SetBackgroundColour('DARKGREY')
        self.btn.Refresh()

if __name__ == '__main__':
    app = wx.App()
    InteractiveButton(None, -1, 'interactivebutton.py')
    app.MainLoop()
