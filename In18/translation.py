#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# translation.py

import wx

class Translation(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (220, 100))

        panel = wx.Panel(self, -1)

        mylocale = wx.Locale()
        mylocale.AddCatalogLookupPathPrefix('.')
        mylocale.AddCatalog('simple_de')

        _ = wx.GetTranslation

        wx.StaticText(panel, -1, _("hello"), (10, 10))
        # wx.StaticText(panel, -1, wx.GetTranslation('hello'), (10, 10))

        self.Centre()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App()
    Translation(None, -1, 'Translation')
    app.MainLoop()
