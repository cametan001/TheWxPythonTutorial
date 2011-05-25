#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# propagate.py

import wx

class MyPanel(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)

        self.Bind(wx.EVT_BUTTON, self.OnClicked)

    def OnClicked(self, event):
        print 'event reached panel class'
        event.Skip()

class MyButton(wx.Button):
    def __init__(self, parent, id, label, pos):
        wx.Button.__init__(self, parent, id, label, pos)

        self.Bind(wx.EVT_BUTTON, self.OnClicked)

    def OnClicked(self, event):
        print 'event reached button class'
        event.Skip()

class Propagete(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 150))

        panel = MyPanel(self, -1)

        MyButton(panel, -1, 'Ok', (15, 15))

        self.Bind(wx.EVT_BUTTON, self.OnClicked)

        self.Center()
        self.Show(True)

    def OnClicked(self, event):
        print 'event reached frame class'
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    Propagete(None, -1, 'Ptopagate')
    app.MainLoop()
