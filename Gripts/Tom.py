#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# Tom

import wx
import smtplib

class Tom(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size = (400, 420))

        panel = wx.Panel(self, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel, -1, 'From')
        st2 = wx.StaticText(panel, -1, 'To ')
        st3 = wx.StaticText(panel, -1, 'Subject')

        self.tc1 = wx.TextCtrl(panel, -1, size = (180, -1))
        self.tc2 = wx.TextCtrl(panel, -1, size = (180, -1))
        self.tc3 = wx.TextCtrl(panel, -1, size = (180, -1))

        self.write = wx.TextCtrl(panel, -1, style = wx.TE_MULTILINE)
        button_send = wx.Button(panel, 1, 'Send')

        hbox1.Add(st1, 0, wx.LEFT, 10)
        hbox1.Add(self.tc1, 0, wx.LEFT, 35)
        hbox2.Add(st2, 0, wx.LEFT, 10)
        hbox2.Add(self.tc2, 0, wx.LEFT, 50)
        hbox3.Add(st3, 0, wx.LEFT, 10)
        hbox3.Add(self.tc3, 0, wx.LEFT, 20)
        vbox.Add(hbox1, 0, wx.TOP, 10)
        vbox.Add(hbox2, 0, wx.TOP, 10)
        vbox.Add(hbox3, 0, wx.TOP, 10)
        vbox.Add(self.write, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 15)
        vbox.Add(button_send, 0, wx.ALIGN_CENTRE | wx.TOP | wx.BOTTOM, 20)

        self.Bind(wx.EVT_BUTTON, self.OnSend, id = 1)
        panel.SetSizer(vbox)

        self.Center()
        self.ShowModal()
        self.Destroy()

    def OnSend(self, event):
        sender = self.tc1.GetValue()
        recipient = self.tc2.GetValue()
        subject = self.tc3.GetValue()
        text = self.write.GetValue()
        header = 'From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n' % (sender, recipient, subject)
        message = header + text

        try:
            server = smtplib.SMTP('mail.chell.sk')
            server.sendmail(sender, recipient, message)
            server.quit()
            dlg = wx.MessageDialog(self, 'Email was successfully sent', 'Success', \
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        except smtplib.SMTPException, error:
            dlg = wx.MessageDialog(self, 'Failed to send email', 'Error', wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

if __name__ == '__main__':
    app = wx.App()
    Tom(None, -1, 'Tom')
    app.MainLoop()
