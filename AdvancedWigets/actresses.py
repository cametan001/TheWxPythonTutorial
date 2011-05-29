#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# actresses.py

import wx, sys

packages = [('jessica alba', 'pomona', '1981'), ('sigourney weaver', 'new york', '1949'), \
            ('angelina jolie', 'los angeles', '1975'), ('natalie portman', 'jerusalem', '1981'), \
            ('rachel weiss', 'london', '1971'), ('scarltt johonsson', 'new york', '1984')]

class Actresses(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (380, 230))

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self, -1)

        self.list = wx.ListCtrl(panel, -1, style = wx.LC_REPORT)
        self.list.InsertColumn(0, 'name', width = 140)
        self.list.InsertColumn(1, 'place', width = 130)
        self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

        for i in packages:
            index = self.list.InsertStringItem(sys.maxint, i[0])
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.Center()
        self.Show(True)
        
if __name__ == '__main__':
    app = wx.App()
    Actresses(None, -1, 'actresses')
    app.MainLoop()
