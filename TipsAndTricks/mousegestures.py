#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# mousegestures.py

import wx
import wx.lib.gestures as gest

class MyMouseGestures(wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (300, 200))

        panel = wx.Panel(self, -1)
        mg = gest.MouseGestures(panel, True, wx.MOUSE_BTN_LEFT)
        mg.SetGesturePen(wx.Colour(255, 0, 0), 2)
        mg.SetGesturesVisible(True)
        mg.AddGesture('DR', self.OnDownRight)

        self.Center()
        self.Show(True)

    def OnDownRight(self):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    MyMouseGestures(None, -1, 'mousegestures.py')
    app.MainLoop()
