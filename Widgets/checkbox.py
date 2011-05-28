#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# checkbox.py

import wx

class CheckBox(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id,title, size = (250, 170))

        panel = wx.Panel(self, -1)
        self.cb = wx.CheckBox(panel, -1, 'Show Title', (10, 10))
        self.cb.SetValue(True)

        wx.EVT_CHECKBOX(self, self.cb.GetId(), self.ShowTitle)

        self.Show()
        self.Center()

    def ShowTitle(self, event):
        if self.cb.GetValue():
            self.SetTitle('checkbox.py')
        else: self.SetTitle('')

if __name__ == '__main__':
    app = wx.App()
    CheckBox(None, -1, 'checkbox.py')
    app.MainLoop()
