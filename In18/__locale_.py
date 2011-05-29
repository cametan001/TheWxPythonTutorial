#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# locale.py

import wx, time, locale

class Locale(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 420))

        panel = wx.Panel(self, -1)

        tm = time.localtime()

        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        us = wx.StaticText(self, -1, 'United States', (25, 20))
        us.SetFont(font)

        wx.StaticLine(self, -1, (35, 50), (200,1))

        locale.setlocale(locale.LC_ALL, '')
        date = time.strftime('%x', tm)
        time_ = time.strftime('%X', tm)
        curr = locale.currency(100000)

        wx.StaticText(self, -1, 'date: ', (25, 70))
        wx.StaticText(self, -1, 'time: ', (25, 90))
        wx.StaticText(self, -1, 'currency: ', (25, 110))

        wx.StaticText(self, -1, str(date), (125, 70))
        wx.StaticText(self, -1, str(time_), (125, 90))
        wx.StaticText(self, -1, str(curr), (125, 110))

        de = wx.StaticText(self, -1, 'Germany', (25, 150))
        de.SetFont(font)

        wx.StaticLine(self, -1, (25, 180), (200, 1))

        locale.setlocale(locale.LC_ALL, ('de_DE', 'UTF8'))
        date = time.strftime('%x', tm)
        time_ = time.strftime('%X', tm)
        curr = locale.currency(100000)

        wx.StaticText(self, -1, 'date: ', (25, 200))
        wx.StaticText(self, -1, 'time: ', (25, 220))
        wx.StaticText(self, -1, 'currency: ', (25, 240))

        wx.StaticText(self, -1, str(date), (125, 200))
        wx.StaticText(self, -1, str(time_), (125, 220))
        wx.StaticText(self, -1, str(curr), (125, 240))

        de = wx.StaticText(self, -1, 'Slovakia', (25, 280))
        de.SetFont(font)

        wx.StaticLine(self, -1, (25, 310), (200, 1))

        # locale.setlocale(locale.LC_ALL, ('sk_SK', 'UTF8'))
        date = time.strftime('%x', tm)
        time_ = time.strftime('%X', tm)
        curr = locale.currency(100000)

        wx.StaticText(self, -1, 'date: ', (25, 330))
        wx.StaticText(self, -1, 'time: ', (25, 350))
        wx.StaticText(self, -1, 'currency: ', (25, 370))

        wx.StaticText(self, -1, str(date), (125, 330))
        wx.StaticText(self, -1, str(time_), (125, 350))
        wx.StaticText(self, -1, str(curr), (125, 370))

        self.Center()
        self.Show(True)

if __name__ == '__main__':
	app = wx.App()
	Locale(None, -1, 'Locale')
	app.MainLoop()
