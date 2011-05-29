#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# collate.py

import wx, locale

ID_SORT = 1

words = [u'Sund', u'S\xe4bel', u'S\xfcnde', u'Schl\xe4fe', u'Sabotage']

class Collate(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (300, 220))

        panel = wx.Panel(self, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel, -1)
        for i in words:
            self.listbox.Append(i)
        hbox.Add(self.listbox, 1, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        new = wx.Button(btnPanel, ID_SORT, 'Sort', size = (90, 30))

        self.Bind(wx.EVT_BUTTON, self.OnSort, id = ID_SORT)

        vbox.Add((-1, 20))
        vbox.Add(new)

        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        locale.setlocale(locale.LC_COLLATE, ('de_DE', 'UTF8'))

        self.Center()
        self.Show(True)

    def OnSort(self, event):
        self.listbox.Clear()
        words.sort(lambda a, b: locale.strcoll(a, b))
        for i in words:
            self.listbox.Append(i)

if __name__ == '__main__':
    app = wx.App()
    Collate(None, -1, 'Colalte')
    app.MainLoop()
