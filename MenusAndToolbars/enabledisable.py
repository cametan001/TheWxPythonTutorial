#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# enabledisable.py

import wx, os.path

class EnableDisable(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 150))

        self.count = 5

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddLabelTool(wx.ID_UNDO, '', \
                                  wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/undo.png')))
        self.toolbar.AddLabelTool(wx.ID_REDO, '', \
                                  wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/redo.png')))
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()
        self.toolbar.AddLabelTool(wx.ID_EXIT, '', \
                                  wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/exit.png')))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnExit, id = wx.ID_EXIT)
        self.Bind(wx.EVT_TOOL, self.OnUndo, id = wx.ID_UNDO)
        self.Bind(wx.EVT_TOOL, self.OnRedo, id = wx.ID_REDO)

        self.Center()
        self.Show(True)

    def OnUndo(self, event):
        if self.count > 1 and self.count <= 5:
            self.count -= 1

        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)

        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)

    def OnRedo(self, event):
        if self.count < 5 and self.count >= 1:
            self.count += 1

        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)

        if self.count == 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)

    def OnExit(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    EnableDisable(None, -1, 'enable disable')
    app.MainLoop()
