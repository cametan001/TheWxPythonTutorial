#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# radiobuttons.py

import wx

class RadioButtons(wx.Frame):
    def __init__(self, parent, id, title, size = (210, 150)):
        wx.Frame.__init__(self, parent, id, title)
        panel = wx.Panel(self, -1)
        self.rb1 = wx.RadioButton(panel, -1, 'Value A', (10, 10), style = wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel, -1, 'Value A', (10, 30))
        self.rb3 = wx.RadioButton(panel, -1, 'Value A', (10, 50))

        self.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id = self.rb1.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id = self.rb2.GetId())
        self.Bind(wx.EVT_RADIOBUTTON, self.SetVal, id = self.rb3.GetId())

        self.statusbar = self.CreateStatusBar(3)
        self.SetVal(True)
        self.Center()
        self.Show(True)

    def SetVal(self, event):
        state1 = str(self.rb1.GetValue())
        state2 = str(self.rb2.GetValue())
        state3 = str(self.rb3.GetValue())

        self.statusbar.SetStatusText(state1, 0)
        self.statusbar.SetStatusText(state2, 1)
        self.statusbar.SetStatusText(state3, 2)

if __name__ == '__main__':
    app = wx.App()
    RadioButtons(None, -1, 'radiobuttons.py')
    app.MainLoop()
