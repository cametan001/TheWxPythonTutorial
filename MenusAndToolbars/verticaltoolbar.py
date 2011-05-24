#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# verticaltoolbar.py

import wx, os.path

class VerticalToolbar(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (240, 300))

        toolbar = self.CreateToolBar(wx.TB_VERTICAL)
        toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/select.png')))
        toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/freehand.png')))
        toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/shapeed.png')))
        toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/pen.png')))
        toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/rectangle.png')))
        toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/ellipse.png')))
        toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/qs.png')))
        toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/text.png')))

        toolbar.Realize()

        self.Center()
        self.Show(True)

    def OnExit(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    VerticalToolbar(None, -1, 'vertical toolbar')
    app.MainLoop()
