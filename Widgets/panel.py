#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# panels.py

import wx, os.path

class Panels(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        splitter = wx.SplitterWindow(self, -1)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        panel1 = wx.Panel(splitter, -1)
        panel11 = wx.Panel(panel1, -1, size = (-1, 40))
        panel11.SetBackgroundColour('#53728c')
        st1 = wx.StaticText(panel11, -1, 'Feeds', (5, 5))
        st1.SetBackgroundColour('WHITE')

        panel12 = wx.Panel(panel1, -1, style = wx.BORDER_SUNKEN)
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

        panel22.SetBackgroundColour('WHITE')
        vbox2.Add(panel21, 0, wx.EXPAND)
        vbox2.Add(panel22, 1, wx.EXPAND)

        panel2.SetSizer(vbox2)

        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(1, 'Exit', wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                               'icons/stock_exit.png')))
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
    Panels(None, -1, 'Panels')
    app.MainLoop()
