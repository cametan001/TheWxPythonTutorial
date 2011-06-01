#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# Isabelle

import wx

ID_TIMER = 1
ID_EXIT = 2
ID_ABOUT = 3
ID_BUTTON = 4

class Isabelle(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.timer = wx.Timer(self, ID_TIMER)
        self.blick = 0

        file = wx.Menu()
        file.Append(ID_EXIT, '&Quit\tCtrl+Q', 'Quit Isabelle')

        help = wx.Menu()
        help.Append(ID_ABOUT, '&About', 'O Programe')

        menubar = wx.MenuBar()
        menubar.Append(file, '&File')
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)

        toolbar = wx.ToolBar(self, -1)
        self.tc = wx.TextCtrl(toolbar, -1, size = (100, -1))
        btn = wx.Button(toolbar, ID_BUTTON, 'Ok', size = (40, 28))

        toolbar.AddControl(self.tc)
        toolbar.AddSeparator()
        toolbar.AddControl(btn)
        toolbar.Realize()
        self.SetToolBar(toolbar)

        self.Bind(wx.EVT_BUTTON, self.OnLaunchCommandOk, id = ID_BUTTON)
        self.Bind(wx.EVT_MENU, self.OnAbout, id = ID_ABOUT)
        self.Bind(wx.EVT_MENU, self.OnExit, id = ID_EXIT)
        self.Bind(wx.EVT_TIMER, self.OnTimer, id = ID_TIMER)

        self.panel = wx.Panel(self, -1, (0, 0), (500, 300))
        self.panel.SetBackgroundColour('GRAY')
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Welcome to Isabelle')
        self.Center()
        self.Show(True)

    def OnExit(self, event):
        dlg = wx.MessageDialog(self, 'Are you sure to quit Isabelle?', \
                               'Please Confirm', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, 'Isabelle\t\n' '2004\t', 'About', \
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnLaunchCommandOk(self, event):
        input = self.tc.GetValue()
        if input == '/bye':
            self.OnExit(self)
        elif input == '/about':
            self.OnAbout(self)
        elif input == '/bell':
            wx.Bell()
        else:
            self.statusbar.SetBackgroundColour('RED')
            self.statusbar.SetStatusText('Unknown Command')
            self.statusbar.Refresh()
            self.timer.Start(50)

        self.tc.Clear()

    def OnTimer(self, event):
        self.blick += 1
        if self.blick == 25:
            self.statusbar.SetBackgroundColour('#E0E2EB')
            self.statusbar.Refresh()
            self.timer.Stop()
            self.blick = 0

if __name__ == '__main__':
    app = wx.App()
    Isabelle(None, -1, 'Isabelle')
    app.MainLoop()
