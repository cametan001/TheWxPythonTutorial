#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# message.py

import wx

class MessageDialog(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        wx.FutureCall(5000, self.ShowMessage)

        self.Center()
        self.Show(True)

    def ShowMessage(self):
        wx.MessageBox('Download completed', 'Info')

if __name__ == '__main__':
    app = wx.App()
    MessageDialog(None, -1, 'MessageDialog')
    app.MainLoop()
