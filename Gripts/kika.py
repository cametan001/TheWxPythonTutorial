#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# kika.py

from ftplib import FTP, all_errors
import wx, os.path

class MyStatusBar(wx.StatusBar):
    def __init__(self, parent):
        wx.StatusBar.__init__(self, parent)

        self.SetFieldsCount(2)
        self.SetStatusText('Welcome to Kika', 0)
        self.SetStatusWidths([-5, 2])
        self.icon = wx.StaticBitmap(self, -1, wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                     'icons/disconnected.png')))
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.PlaceIcon()

    def PlaceIcon(self):
        rect = self.GetFieldRect(1)
        self.icon.SetPosition((rect.x + 3, rect.y + 3))

    def OnSize(self, event):
        self.PlaceIcon()

class Kika(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 270))

        wx.StaticText(self, -1, 'Ftp site', (10, 20))
        wx.StaticText(self, -1, 'Login', (10, 60))
        wx.StaticText(self, -1, 'Password', (10, 100))

        self.ftpsite = wx.TextCtrl(self, -1, '', (110, 15), (120, -1))
        self.login = wx.TextCtrl(self, -1, '', (110, 55), (120, -1))
        self.password = wx.TextCtrl(self, -1, '', (110, 95), (120, -1), style = wx.TE_PASSWORD)

        self.ftp = None

        con = wx.Button(self, 1, 'Connect', (10, 160))
        discon = wx.Button(self, 2, 'DisConnect', (120, 160))

        self.Bind(wx.EVT_BUTTON, self.OnConnect, id = 1)
        self.Bind(wx.EVT_BUTTON, self.OnDisConnect, id = 2)

        self.statusbar = MyStatusBar(self)
        self.SetStatusBar(self.statusbar)
        self.Center()
        self.Show()

    def OnConnect(self, event):
        if not self.ftp:
            ftpsite = self.ftpsite.GetValue()
            login = self.login.GetValue()
            password = self.password.GetValue()

            try:
                self.ftp = FTP(ftpsite)
                var = self.ftp.login(login, password)
                self.statusbar.SetStatusText('User connected')
                self.statusbar.icon.SetBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                     'icons/connected.png')))
            except AttributeError:
                self.statusbar.SetForegroundColour(wx.RED)
                self.statusbar.SetStatusText('Incorrect params')
                self.ftp = None

            except all_errors, err:
                self.statusbar.SetStatusText(str(err))
                self.ftp = None

    def OnDisConnect(self, event):
        if self.ftp:
            self.ftp.quit()
            self.ftp = None
            self.statusbar.SetStatusText('User disconnected')
            self.statusbar.icon.SetBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                                 'icons/discnnecter.png')))

if __name__ == '__main__':
    app = wx.App()
    Kika(None, -1, 'Kika')
    app.MainLoop()
