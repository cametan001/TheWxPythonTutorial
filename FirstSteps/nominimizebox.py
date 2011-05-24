#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# nominimizebox.py

import wx

app = wx.App()
window = wx.Frame(None, style = wx.MAXIMIZE_BOX | wx.RESIZE_BORDER  \
                  | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
window.Show(True)

app.MainLoop()

# if __name__ == '__main__':
