#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# move.py

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title = title, \
                                      size = (300, 200))

        self.Move((800, 250))
        self.Show()

if __name__ == '__main__':

    app = wx.App()
    Example(None, title = 'Move')
    app.MainLoop()
