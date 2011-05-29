#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# listbox.py

import wx

ID_NEW = 1
ID_RENAME = 2
ID_CLEAR = 3
ID_DELETE = 4

class ListBox(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (350, 220))

        panel = wx.Panel(self, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel, -1)
        hbox.Add(self.listbox, 1, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        new = wx.Button(btnPanel, ID_NEW, 'New', size = (90, 30))
        ren = wx.Button(btnPanel, ID_RENAME, 'Rename', size = (90, 30))
        dlt = wx.Button(btnPanel, ID_DELETE, 'Delete', size = (90, 30))
        clr = wx.Button(btnPanel, ID_CLEAR, 'Clear', size = (90, 30))

        self.Bind(wx.EVT_BUTTON, self.NewItem, id = ID_NEW)
        self.Bind(wx.EVT_BUTTON, self.OnRename, id = ID_RENAME)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id = ID_DELETE)
        self.Bind(wx.EVT_BUTTON, self.OnClear, id = ID_CLEAR)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnClear)

        vbox.Add((-1, 20))
        vbox.Add(new)
        vbox.Add(ren, 0, wx.TOP, 5)
        vbox.Add(dlt, 0, wx.TOP, 5)
        vbox.Add(clr, 0, wx.TOP, 5)

        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.Center()
        self.Show(True)

    def NewItem(self, event):
        text = wx.GetTextFromUser('Enter a new item', 'Insert dialog')
        if text != '':
            self.listbox.Append(text)

    def OnRename(self, event):
        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser('Rename item', 'Rename dialog', text)
        if renamed != '':
            self.listbox.Delete(sel)
            self.listbox.Insert(renamed, sel)
            
    def OnDelete(self, event):
        sel = self.listbox.GetSelection()
        if sel != -1:
            self.listbox.Delete(sel)

    def OnClear(self, event):
        self.listbox.Clear()

if __name__ == '__main__':
    app = wx.App()
    ListBox(None, -1, 'ListBox')
    app.MainLoop()
