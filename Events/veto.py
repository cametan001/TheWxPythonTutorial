#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# veto.py

import wx

class Veto(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 200))

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.Center()
        self.Show(True)

    def OnClose(self, event):

        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Quiestion', \
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.Destroy()
        else:
            event.Veto()

if __name__ == '__main__':
    app = wx.App()
    Veto(None, -1, 'Veto')
    app.MainLoop()
