#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# browser.py

import wx, os.path
from wx.lib.buttons import GenBitmapTextButton

class Browser(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (450, 400))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('WHITE')

        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(1, '&Quit', '')
        edit = wx.Menu()
        view = wx.Menu()
        go = wx.Menu()
        bookmarks = wx.Menu()
        tools = wx.Menu()
        help = wx.Menu()

        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(view, '&View')
        menubar.Append(go, '&Go')
        menubar.Append(bookmarks, '&Bookmarks')
        menubar.Append(tools, '&Tools')
        menubar.Append(help, '&Help')

        self.SetMenuBar(menubar)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        toolbar1 = wx.Panel(panel, -1, size = (-1, 40))
        back = wx.BitmapButton(toolbar1, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                    'icons/back.png')), \
                                                                    style = wx.NO_BORDER)
        forward = wx.BitmapButton(toolbar1, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                    'icons/forward.png')), \
                                                                    style = wx.NO_BORDER)
        refresh = wx.BitmapButton(toolbar1, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                    'icons/refresh.png')), \
                                                                    style = wx.NO_BORDER)
        stop = wx.BitmapButton(toolbar1, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                    'icons/stop.png')), \
                                                                    style = wx.NO_BORDER)
        home = wx.BitmapButton(toolbar1, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                    'icons/home.png')), \
                                                                    style = wx.NO_BORDER)
        address = wx.ComboBox(toolbar1, -1, size = (50, -1))
        go = wx.BitmapButton(toolbar1, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                    'icons/go.png')), \
                                                                    style = wx.NO_BORDER)
        text = wx.TextCtrl(toolbar1, -1, size = (150, -1))

        hbox1.Add(back)
        hbox1.Add(forward)
        hbox1.Add(refresh)
        hbox1.Add(stop)
        hbox1.Add(home)
        hbox1.Add(address, 1, wx.TOP, 4)
        hbox1.Add(go, 0, wx.TOP | wx.LEFT, 4)
        hbox1.Add(text, 0, wx.TOP | wx.RIGHT, 4)

        vbox.Add(toolbar1, 0, wx.EXPAND)
        line = wx.StaticLine(panel)
        vbox.Add(line, 0, wx.EXPAND)
        
        toolbar2 = wx.Panel(panel, -1, size = (-1, 30))
        bookmark1 = wx.BitmapButton(toolbar2, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                         'icons/love.png')), \
                                    style = wx.NO_BORDER)
        bookmark2 = wx.BitmapButton(toolbar2, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                         'icons/books.png')), \
                                    style = wx.NO_BORDER)
        bookmark3 = wx.BitmapButton(toolbar2, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                         'icons/sound.png')), \
                                    style = wx.NO_BORDER)
        hbox2.Add(bookmark1, flag = wx.RIGHT, border = 5)
        hbox2.Add(bookmark2, flag = wx.RIGHT, border = 5)
        hbox2.Add(bookmark3)
        toolbar2.SetSizer(hbox2)
        vbox.Add(toolbar2, 0, wx.EXPAND)
        line = wx.StaticLine(panel)
        vbox.Add(line, 0, wx.EXPAND)

        panel.SetSizer(vbox)

        self.CreateStatusBar()
        self.Center()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App(0)
    Browser(None, -1, 'Browser')
    app.MainLoop()
