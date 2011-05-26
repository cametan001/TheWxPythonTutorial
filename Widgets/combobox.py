#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# combobox.py

import wx, os.path

class ComboBox(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size = (250, 270))
        panel = wx.Panel(self, -1, (75, 20), (100, 127), style = wx.SUNKEN_BORDER)
        self.picture = wx.StaticBitmap(panel)
        panel.SetBackgroundColour(wx.WHITE)

        self.images = ['tolstoy.jpg', 'feuchtwanger.jpg', 'balzac.jpg','pasternak.jpg', \
                       'galsworthy.jpg', 'wolfe.jpg', 'zweig.jpg', 'konatsu.jpg', \
                       'meguru.jpg', 'miku.jpg', 'nao.jpg', 'rei.jpg', \
                       'rumi.jpg', 'saori.jpg', 'yui.jpg', 'chiaki.jpg']
        authors = ['Leo Tolstoy', 'Lion Feuchtwanger', 'Honore de Balzac', 'Boris Pasternak', \
                   'John Galsworthy', 'Tom Wolfe', 'Stefan Zweig', u'黒川小夏', \
                   u'小坂めぐる', u'初音ミク', u'及川奈央', u'檸衣', \
                   u'白崎るみ', u'深海沙織', u'波多野結衣', u'小菅千晶']

        wx.ComboBox(self, -1, pos = (50, 170), size = (150, -1), choices = authors, \
                    style = wx.CB_READONLY)
        wx.Button(self, 1, 'Close', (80, 220))

        self.Bind(wx.EVT_BUTTON, self.OnClose, id = 1)
        self.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        self.Center()
        self.ShowModal()
        self.Destroy()

    def OnClose(self, event):
        self.Close()

    def OnSelect(self, event):
        item = event.GetSelection()
        self.picture.SetFocus()
        self.picture.SetBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/', self.images[item])))

if __name__ == '__main__':
    app = wx.App()
    ComboBox(None, -1, 'combobox.py')
    app.MainLoop()
