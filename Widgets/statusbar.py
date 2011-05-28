#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# statusbar.py

import wx

class Statusbar(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 200), \
        style = wx.CAPTION | wx.SYSTEM_MENU | wx.CLOSE_BOX)

        panel = wx.Panel(self, 1)

        button = wx.Button(panel, 2, 'Button', (20, 20))
        text = wx.CheckBox(panel, 3, 'CheckBox', (20, 90))
        combo = wx.ComboBox(panel, 4, '', (120, 22))
        slider = wx.Slider(panel, 5, 6, 1, 10, (120, 90), (110, -1))

        panel.Bind(wx.EVT_ENTER_WINDOW, self.EnterPanel, id = 1)
        button.Bind(wx.EVT_ENTER_WINDOW, self.EnterButton, id = 2)
        text.Bind(wx.EVT_ENTER_WINDOW, self.EnterText, id = 3)
        combo.Bind(wx.EVT_ENTER_WINDOW, self.EnterCombo, id = 4)
        slider.Bind(wx.EVT_ENTER_WINDOW, self.EnterSlider, id = 5)

        self.sb = self.CreateStatusBar()
        self.SetMaxSize((250, 200))
        self.SetMinSize((250, 200))
        self.Show(True)
        self.Center()

    def EnterButton(self, event):
        self.sb.SetStatusText('Button widget')
        event.Skip()

    def EnterPanel(self, event):
        self.sb.SetStatusText('Panel widget')
        event.Skip()

    def EnterText(self, event):
        self.sb.SetStatusText('CheckBox widget')
        event.Skip()

    def EnterCombo(self, event):
        self.sb.SetStatusText('ComboBox widget')
        event.Skip()

    def EnterSlider(self, event):
        self.sb.SetStatusText('Slider widget')
        event.Skip()
        
if __name__ == '__main__':
    app = wx.App()
    Statusbar(None, -1, 'statusbar.py')
    app.MainLoop()
