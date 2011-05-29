#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# insertdata.py

import wx
import sqlite3 as lite

class InsertData(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (280, 200))

        panel = wx.Panel(self, -1)

        gs = wx.FlexGridSizer(3, 2, 9, 9)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        name = wx.StaticText(panel, -1, 'Name')
        remark = wx.StaticText(panel, -1, 'Remark')
        age = wx.StaticText(panel, -1, 'Age')
        self.sp = wx.SpinCtrl(panel, -1, '', size = (60, -1), min = 1, max = 125)
        self.tc1 = wx.TextCtrl(panel, -1, size = (150, -1))
        self.tc2 = wx.TextCtrl(panel, -1, size = (150, -1))

        gs.AddMany([(name), (self.tc1, 1, wx.LEFT, 10), \
                    (remark), (self.tc2, 1, wx.LEFT, 10), \
                    (age), (self.sp, 0, wx.LEFT, 10)])

        vbox.Add(gs, 0, wx.ALL, 10)
        vbox.Add((-1, 30))

        insert = wx.Button(panel, -1, 'Insert', size = (-1, 30))
        cancel = wx.Button(panel, -1, 'Cancel', size = (-1, 30))
        hbox.Add(insert)
        hbox.Add(cancel, 0, wx.LEFT, 5)
        vbox.Add(hbox, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)

        self.Bind(wx.EVT_BUTTON, self.OnInsert, id = insert.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = cancel.GetId())

        panel.SetSizer(vbox)

        self.Center()
        self.Show(True)

    def OnInsert(self, event):
        try:
            con = lite.connect('people')
            cur = con.cursor()
            name = self.tc1.GetValue()
            age = self.sp.GetValue()
            remark = self.tc2.GetValue()
            cur.execute('insert into neighbours values(?, ?, ?)', (name, age, remark))
            con.commit()
            cur.close()
            con.close()

        except lite.Error, error:
            dlg = wx.MessageDialog(self, str(error), 'Error occured')
            dlg.ShowModal()

    def OnCancel(self, event):
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    InsertData(None, -1, 'Insert Dialog')
    app.MainLoop()
