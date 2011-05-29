#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# helpwindow.py

import wx, os.path
import wx.html as html

class HelpWindow(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (570, 400))

        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(1, 'Exit', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/exit.png')))
        toolbar.AddLabelTool(2, 'help', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/help.png')))
        toolbar.Realize()

        self.splitter = wx.SplitterWindow(self, -1)
        self.panelLeft = wx.Panel(self.splitter, -1, style = wx.BORDER_SUNKEN)

        self.panelRight = wx.Panel(self.splitter, -1)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        header = wx.Panel(self.panelRight, -1, size = (-1, 20))
        header.SetBackgroundColour('#6f6a59')
        header.SetForegroundColour('WHITE')
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        st = wx.StaticText(header, -1, 'Help', (5, 5))
        font = st.GetFont()
        font.SetPointSize(9)
        st.SetFont(font)
        hbox.Add(st, 1, wx.TOP | wx.Bottom | wx.LEFT, 5)

        close = wx.BitmapButton(header, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                   'icons/fileclose.png'), \
                                                      wx.BITMAP_TYPE_PNG), style = wx.NO_BORDER)
        close.SetBackgroundColour('#6f6a59')
        hbox.Add(close, 0)
        header.SetSizer(hbox)

        vbox2.Add(header, 0, wx.EXPAND)

        _help = html.HtmlWindow(self.panelRight, -1, style = wx.NO_BORDER)
        _help.LoadPage(os.path.join(os.path.dirname(__file__), 'help.html'))
        vbox2.Add(_help, 1, wx.EXPAND)
        self.panelRight.SetSizer(vbox2)
        self.panelLeft.SetFocus()

        self.splitter.SplitVertically(self.panelLeft, self.panelRight)
        self.splitter.Unsplit()

        self.Bind(wx.EVT_BUTTON, self.CloseHelp, id = close.GetId())
        self.Bind(wx.EVT_TOOL, self.OnClose, id = 1)
        self.Bind(wx.EVT_TOOL, self.OnHelp, id = 2)

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)

        self.CreateStatusBar()

        self.Center()
        self.Show(True)

    def OnClose(self, event):
        self.Close()

    def OnHelp(self, event):
        self.splitter.SplitVertically(self.panelLeft, self.panelRight)
        self.panelLeft.SetFocus()

    def CloseHelp(self, event):
        self.splitter.Unsplit()
        self.panelLeft.SetFocus()

    def OnKeyPressed(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_F1:
            self.splitter.SplitVertically(self.panelLeft, self.panelRight)
            self.panelLeft.SetFocus()


if __name__ == '__main__':
    app = wx.App()
    HelpWindow(None, -1, 'HelpWindow')
    app.MainLoop()
