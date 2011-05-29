#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# sorted.py

import wx, sys
from wx.lib.mixins.listctrl import ColumnSorterMixin

actresses = {
    1 : ('jessica alba', 'pomona', '1981'), \
    2 : ('sigourney weaver', 'new york', '1949'), \
    3 : ('angelina jolie', 'los angeles', '1975'), \
    4 : ('natalie portman', 'jerusalem', '1981'), \
    5 : ('rachel weiss', 'london', '1971'), \
    6 : ('scarltt johonsson', 'new york', '1984')
    }

class SortedListCtrl(wx.ListCtrl, ColumnSorterMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style = wx.LC_REPORT)
        ColumnSorterMixin.__init__(self, len(actresses))
        self.itemDataMap = actresses

    def GetListCtrl(self):
        return self

class Actresses(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (380, 230))

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self, -1)

        self.list = SortedListCtrl(panel)
        self.list.InsertColumn(0, 'name', width = 140)
        self.list.InsertColumn(1, 'place', width = 130)
        self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

        items = actresses.items()

        for key, data in items:
            index = self.list.InsertStringItem(sys.maxint, data[0])
            self.list.SetStringItem(index, 1, data[1])
            self.list.SetStringItem(index, 2, data[2])
            self.list.SetItemData(index, key)

        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

        self.Center()
        self.Show(True)

if __name__ == '__main__':
        app = wx.App()
        Actresses(None, -1, 'actresses')
        app.MainLoop()
