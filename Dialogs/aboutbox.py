#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# aboutbox.py

import wx, os.path

ID_ABOUT = 1

class AboutDialogBox(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (260, 200))

        menubar = wx.MenuBar()
        _help = wx.Menu()
        _help.Append(ID_ABOUT, '&About')
        self.Bind(wx.EVT_MENU, self.OnAboutBox, id = ID_ABOUT)
        menubar.Append(_help, '&Help')
        self.SetMenuBar(menubar)

        self.Center()
        self.Show(True)

    def OnAboutBox(self, event):
        description = """
        File Hunter is an advanced file manager for the Unix operating
        system. Features include powerful built-in editor, advanced search capabilities,
        powerful batch renaming, file comparison, extensive archive handling and more.
        """

        licence = """
        File Hunter is free software; you can redistribute it and/or modify it
        under the terms of the GNU General Public License as published by the Free Software Foundation;
        either version 2 of the License, or (at your option) any later version.

        File Hunter is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
        without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
        See the GNU General Public License for more details. You should have received a copy of
        the GNU General Public License along with File Hunter; if not, write to
        the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
        """

        info = wx.AboutDialogInfo()

        info.SetIcon(wx.Icon(os.path.join(os.path.dirname(__file__), 'icons/hunter.jpg'), wx.BITMAP_TYPE_JPEG))
        info.SetName('File Hunter')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('http://www.zetcode.com')
        info.SetLicence(licence)
        info.AddDeveloper('jan hodnar')
        info.AddDocWriter('jan bodnar')
        info.AddArtist('The Tango crew')
        info.AddTranslator('jan bodnar')

        wx.AboutBox(info)
        

if __name__ == '__main__':
    app = wx.App()
    AboutDialogBox(None, -1, 'About dialog box')
    app.MainLoop()
