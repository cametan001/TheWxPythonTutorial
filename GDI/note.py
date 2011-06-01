#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# note.py

import wx, os.path

class Note(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, \
                          style = wx.FRAME_SHAPED | \
                          wx.SIMPLE_BORDER | \
                          wx.FRAME_NO_TASKBAR)

        self.font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, \
                            wx.FONTWEIGHT_BOLD, False, 'Comin Sans MS')
        self.bitmap = wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/note.jpg'), wx.BITMAP_TYPE_JPEG)
        self.cross = wx.Bitmap(os.path.join(os.path.dirname(__file__), 'images/cross.jpg'), wx.BITMAP_TYPE_JPEG)

        w = self.bitmap.GetWidth()
        h = self.bitmap.GetHeight()
        self.SetClientSize((w, h))

        if wx.Platform == '__WXGTK__':
            self.Bind(wx.EVT_WINDOW_CREATE, self.SetNoteShape)
        else: self.SetNoteShape()

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)

        self.bitmapRegion = wx.RegionFromBitmap(self.bitmap)
        self.crossRegion = wx.RegionFromBitmap(self.cross)

        self.bitmapRegion.IntersectRegion(self.crossRegion)
        self.bitmapRegion.Offset(170, 10)

        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bitmap, 0, 0, True)
        self.PositionTopRight()
        self.Show(True)

    def PositionTopRight(self):
        disx, disy = wx.GetDisplaySize()
        x, y = self.GetSize()
        self.Move((disx - x, 0))

    def SetNoteShape(self, *event):
        region = wx.RegionFromBitmap(self.bitmap)
        self.SetShape(region)

    def OnLeftDown(self, event):
        pos = event.GetPosition()
        if self.bitmapRegion.ContainsPoint(pos):
            self.Close()
        x, y = self.ClientToScreen(event.GetPosition())
        ox, oy = self.GetPosition()
        dx = x - ox
        dy = y - oy
        self.delta = ((dx, dy))

    def OnMouseMove(self, event):
        if event.Dragging() and event.LeftIsDown():
            x, y = self.ClientToScreen(event.GetPosition())
            fp = (x - self.delta[0], y - self.delta[1])
            self.Move(fp)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetFont(self.font)
        dc.SetTextForeground('WHITE')

        dc.DrawBitmap(self.bitmap, 0, 0, True)
        dc.DrawBitmap(self.cross, 170, 10, True)
        dc.DrawText(' - Go shopping', 20, 20)
        dc.DrawText(' - Make a phone call', 20, 50)
        dc.DrawText(' - Write an emeil', 20, 80)

if __name__ == '__main__':
    app = wx.App()
    Note(None, -1, '')
    app.MainLoop()
