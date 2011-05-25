#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# message.py

import wx

class Messages(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 150))

        panel = wx.Panel(self, -1)

        hbox = wx.BoxSizer()
        sizer = wx.GridSizer(2, 2, 2, 2)

        btn1 = wx.Button(panel, -1, 'Info')
        btn2 = wx.Button(panel, -1, 'Error')
        btn3 = wx.Button(panel, -1, 'Question')
        btn4 = wx.Button(panel, -1, 'Alert')

        sizer.AddMany([btn1, btn2, btn3, btn4])

        hbox.Add(sizer, 0, wx.ALL, 15)
        panel.SetSizer(hbox)

        btn1.Bind(wx.EVT_BUTTON, self.ShowMessage1)
        btn2.Bind(wx.EVT_BUTTON, self.ShowMessage2)
        btn3.Bind(wx.EVT_BUTTON, self.ShowMessage3)
        btn4.Bind(wx.EVT_BUTTON, self.ShowMessage4)

        self.Center()
        self.Show(True)

    def ShowMessage1(self, event):
        dial = wx.MessageDialog(None, 'Download completed', 'Info', wx.OK)
        dial.ShowModal()

    def ShowMessage2(self, event):
        dial = wx.MessageDialog(None, 'Error loading file', 'Error', wx.OK | \
                                wx.ICON_ERROR)
        dial.ShowModal()

    def ShowMessage3(self, event):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question', \
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        dial.ShowModal()

    def ShowMessage4(self, event):
        dial = wx.MessageDialog(None, 'Unallowed operation', 'Exclamation', wx.OK | \
                                wx.ICON_EXCLAMATION)
        dial.ShowModal()

if __name__ == '__main__':
    app = wx.App()
    Messages(None, -1, 'Messages')
    app.MainLoop()
