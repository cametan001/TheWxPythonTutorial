#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# statictext.py

import wx

class StaticText(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        lyrics1 = """
        I'm giving up the ghost of love
        in the shadows cast on devotion
        She is the one that I adore
        creed of my silent suffocation
        Break this bittersweet spell on me
        lost in the arms of destiny
        """

        lyrics2 = """
        There is something in the way
        You're always somewhere else
        Feelings have deserted me
        To a point of no return
        I don't believe in God
        But I pray for you
        """

        vbox = wx.BoxSizer(wx.VERTICAL)
        panel = wx.Panel(self, -1)
        st1 = wx.StaticText(panel, -1, lyrics1, style = wx.ALIGN_CENTER)
        st2 = wx.StaticText(panel, -1, lyrics2, style = wx.ALIGN_CENTER)
        vbox.Add(st1, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 15)
        vbox.Add(st2, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 15)
        panel.SetSizer(vbox)
        self.Center()
        self.Show(True)



if __name__ == '__main__':
    app = wx.App()
    StaticText(None, -1, 'statixtext.py')
    app.MainLoop()
