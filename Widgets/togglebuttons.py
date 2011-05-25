#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# togglebuttons.py

import wx

class ToggleButtons(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size = (300, 200))

        self.color = wx.Colour(0, 0, 0)

        wx.ToggleButton(self, 1, 'red', (20, 25))
        wx.ToggleButton(self, 2, 'green', (20, 60))
        wx.ToggleButton(self, 3, 'blue', (20, 100))

        self.panel = wx.Panel(self, -1, (150, 20), (110, 110), style = wx.SUNKEN_BORDER)
        self.panel.SetBackgroundColour(self.color)

        self.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleRed, id = 1)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleGreen, id = 2)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleBlue, id = 3)

        self.Center()
        self.ShowModal()
        self.Destroy()

    def ToggleRed(self, event):
        green = self.color.Green()
        blue = self.color.Blue()
        if self.color.Red():
            self.color.Set(0, green, blue)
        else:
            self.color.Set(255, green, blue)
        self.panel.SetBackgroundColour(self.color)

    def ToggleGreen(self, event):
        red = self.color.Red()
        blue = self.color.Blue()
        if self.color.Green():
            self.color.Set(red, 0, blue)
        else:
            self.color.Set(red, 255, blue)
        self.panel.SetBackgroundColour(self.color)

    def ToggleBlue(self, event):
        red = self.color.Red()
        green = self.color.Green()
        if self.color.Blue():
            self.color.Set(red, green, 0)
        else:
            self.color.Set(red, green, 255)
        self.panel.SetBackgroundColour(self.color)

if __name__ == '__main__':
    app = wx.App()
    ToggleButtons(None, -1, 'togglebuttons.py')
    app.MainLoop()
