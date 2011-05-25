#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# colordepth.py

import wx, os.path

ID_DEPTH = 1

class ChangeDepth(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size = (250, 210))

        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)

        wx.StaticBox(panel, -1, 'Colors', (5, 5), (240, 150))
        wx.RadioButton(panel, -1, '256 Colors', (15, 30), style = wx.RB_GROUP)
        wx.RadioButton(panel, -1, '16 Colors', (15, 55))
        wx.RadioButton(panel, -1, '2 Colors', (15, 80))
        wx.RadioButton(panel, -1, 'Custom', (15, 105))
        wx.TextCtrl(panel, -1, '', (95, 105))

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, -1, 'Ok', size = (70, 30))
        closeButton = wx.Button(self, -1, 'Close', size = (70, 30))
        hbox.Add(okButton, 1)
        hbox.Add(closeButton, 1, wx.LEFT, 5)

        vbox.Add(panel)
        vbox.Add(hbox, 1, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)

        self.SetSizer(vbox)

class ColorDepth(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (350, 220))

        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(ID_DEPTH, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/color.png')))

        self.Bind(wx.EVT_TOOL, self.OnChangeDepth, id = ID_DEPTH)

        self.Center()
        self.Show(True)

    def OnChangeDepth(self, event):
        chgdep = ChangeDepth(None, -1, 'Change Color Depth')
        chgdep.ShowModal()
        chgdep.Destroy()

if __name__ == '__main__':
    app = wx.App()
    ColorDepth(None, -1, '')
    app.MainLoop()
