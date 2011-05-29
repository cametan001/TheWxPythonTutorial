#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# reader.py

import wx, os.path

articles = [['Mozilla rocks', 'The year of the Mozilla', 'Earth on Fire'], \
            ['Gnome pretty, Gnome Slow', 'Gnome, KDE, Icewn, XFCE', 'Where is Gnome heading?'], \
            ['Java number one language', 'Compiled languages, interpreted Lnaguages', 'Java on Desktop']]

class ListCtrlLeft(wx.ListCtrl):
    def __init__(self, parent, id):
        wx.ListCtrl.__init__(self, parent, id, style = wx.LC_REPORT | wx.LC_HRULES | \
                             wx.LC_NO_HEADER | wx.LC_SINGLE_SEL)
        images = [os.path.join(os.path.dirname(__file__), i) for i in \
                  ['icons/java.png', 'icons/gnome.png', 'icons/mozilla.png']]

        self.parent = parent

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelect)

        self.il = wx.ImageList(32, 32)
        for i in images:
            self.il.Add(wx.Bitmap(i))

        self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        self.InsertColumn(0, '')

        for i in range(3):
            self.InsertStringItem(0, '')
            self.SetItemImage(0, i)

    def OnSize(self, event):
        size = self.parent.GetSize()
        self.SetColumnWidth(0, size.x - 5)
        event.Skip()

    def OnSelect(self, event):
        window = self.parent.GetGrandParent().FindWindowByName('ListControlOnRight')
        index = event.GetIndex()
        window.LoadData(index)

    def OnDeSelect(self, event):
        index = event.GetIndex()
        self.SetItemBackgroundColour(0, 'red')

class ListCtrlRight(wx.ListCtrl):
    def __init__(self, parent, id):
        wx.ListCtrl.__init__(self, parent, id, style = wx.LC_REPORT | wx.LC_HRULES | \
                             wx.LC_NO_HEADER | wx.LC_SINGLE_SEL)

        self.parent = parent

        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.InsertColumn(0, '')

    def OnSize(self, event):
        size = self.parent.GetSize()
        self.SetColumnWidth(0, size.x - 5)
        event.Skip()

    def LoadData(self, index):
        self.DeleteAllItems()
        for i in range(3):
            self.InsertStringItem(0, articles[index][i])

class Reader(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        splitter = wx.SplitterWindow(self, -1, style = wx.SP_LIVE_UPDATE | wx.SP_NOBORDER)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        panel1 = wx.Panel(splitter, -1)
        panel11 = wx.Panel(panel1, -1, size = (-1, 40))
        panel11.SetBackgroundColour('#53728c')
        st1 = wx.StaticText(panel11, -1, 'Feeds', (5, 5))
        st1.SetBackgroundColour('WHITE')

        panel12 = wx.Panel(panel1, -1, style = wx.BORDER_SUNKEN)
        vbox = wx.BoxSizer(wx.VERTICAL)
        list1 = ListCtrlLeft(panel12, -1)

        vbox.Add(list1, 1, wx.EXPAND)
        panel12.SetSizer(vbox)
        panel12.SetBackgroundColour('WHITE')

        vbox1.Add(panel11, 0, wx.EXPAND)
        vbox1.Add(panel12, 1, wx.EXPAND)

        panel1.SetSizer(vbox1)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        panel2 = wx.Panel(splitter, -1)
        panel21 = wx.Panel(panel2, -1, size = (-1, 40), style = wx.NO_BORDER)
        st2 = wx.StaticText(panel21, -1, 'Articles', (5, 5))
        st2.SetForegroundColour('WHITE')

        panel21.SetBackgroundColour('#53728c')
        panel22 = wx.Panel(panel2, -1, style = wx.BORDER_RAISED)
        vbox3 = wx.BoxSizer(wx.VERTICAL)
        list2 = ListCtrlRight(panel22, -1)
        list2.SetName('ListControlOnRight')
        vbox3.Add(list2, 1, wx.EXPAND)
        panel22.SetSizer(vbox3)

        panel22.SetBackgroundColour('WHITE')
        vbox2.Add(panel21, 0, wx.EXPAND)
        vbox2.Add(panel22, 1, wx.EXPAND)

        panel2.SetSizer(vbox2)

        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(1, 'Exit', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/exit.png')))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.ExitApp, id = 1)

        hbox.Add(splitter, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        self.SetSizer(hbox)
        self.CreateStatusBar()
        splitter.SplitVertically(panel1, panel2)
        self.Center()
        self.Show(True)

    def ExitApp(self, event):
        self.Close()

        
if __name__ == '__main__':
    app = wx.App()
    Reader(None, -1, 'Reader')
    app.MainLoop()
