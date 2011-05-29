#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# unicode.py

import wx

text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043ba\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442o\u0439 \n\
\u0410\u043d\u043d\u0430\u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

class Unicode(wx.Frame):
    def __init__(self, parent, id,title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 150))

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.Center()
        self.Show(True)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.DrawText(text, 50, 50)

if __name__ == '__main__':
    app = wx.App()
    Unicode(None, -1, 'Unicode')
    app.MainLoop()
