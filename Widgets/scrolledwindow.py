#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# scrolledwindow.py

import wx, os.path

class ScrolledWindow(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (500, 400))

        sw = wx.ScrolledWindow(self)
        bmp = wx.Image(os.path.join(os.path.dirname(__file__), 'images/aliens.jpg'), \
                       wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        wx.StaticBitmap(sw, -1, bmp)
        sw.SetScrollbars(20, 20, 55, 40)
        sw.Scroll(50, 10)
        self.Center()
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    ScrolledWindow(None, -1, 'Aliens')
    app.MainLoop()
