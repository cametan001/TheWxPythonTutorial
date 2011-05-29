#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# filedrop.py

import wx

class FileDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):

        for name in filenames:
            try:
                file = open(name, 'r')
                text = file.read()
                self.window.WriteText(text)
                file.close()
            except IOError, error:
                dlg = wx.MessageDialog(None, 'Error opening file\n' + str(error))
                dlg.ShowModal()
            except UnicodeDecodeError, error:
                dlg = wx.MessageDialog(None, 'Cannot open non ascii files\n' + str(error))
                dlg.ShowModal()

class DropFile(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (450, 400))

        self.text = wx.TextCtrl(self, -1, style = wx.TE_MULTILINE)
        dt = FileDrop(self.text)
        self.text.SetDropTarget(dt)
        self.Center()
        self.Show(True)
                
if __name__ == '__main__':
    app = wx.App()
    DropFile(None, -1, 'filedrop.py')
    app.MainLoop()
                
