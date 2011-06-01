#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# undoredo.py

from wx.lib.sheet import *
import wx, os.path

stockUndo = []
stockRedo = []

ID_QUIT = 10
ID_UNDO = 11
ID_REDO = 12
ID_EXIT = 14

ID_COLSIZE = 80
ID_ROWSIZE = 20

class UndoText:
    def __init__(self, sheet, text1, text2, row, column):
        self.RedoText = text2
        self.row = row
        self.col = column
        self.UndoText = text1
        self.sheet = sheet

    def undo(self):
        self.RedoText = self.sheet.GetCellValue(self.row, self.col)
        if self.UndoText == None:
            self.sheetSetCellValue('')
        else: self.sheet.SetCellValue(self.row, self.col, self.UndoText)

    def redo(self):
        if self.RedoText == None:
            self.sheet.SetCellValue('')
        else: self.sheet.SetCellValue(self.row, self.col, self.UndoText)

class UndoColSize:
    def __init__(self, sheet, position, size):
        self.sheet = sheet
        self.pos = position
        self.RedoSize = size
        self.UndoSize = ID_COLSIZE

    def undo(self):
        self.RedoSize = self.sheet.GetColSize(self.pos)
        self.sheet.SetColSize(self.pao, self.UndoSize)
        self.sheet.ForceRefresh()

    def redo(self):
        self.UndoSize = ID_COLSIZE
        self.sheet.SetColSize(self.pos, self.RedoSize)
        self.sheet.ForceRefresh()

class UndoRowSize:
    def __init__(self, sheet, position, size):
        self.sheet = sheet
        self.pos = position
        self.RedoSize = size
        self.UndoSize = ID_ROWSIZE

    def undo(self):
        self.RedoSize = self.sheet.GetRowSize(self.pos)
        self.sheet.SetRowSize(self.pos, self.UndoSize)
        self.sheet.ForceRefresh()

    def redo(self):
        self.UndoSize = ID_ROWSIZE
        self.sheet.SetRowSize(self.pos, self.RedoSize)
        self.sheet.ForceRefresh()

class MySheet(CSheet):
    instance = 0
    def __init__(self, parent):
        CSheet.__init__(self, parent)
        self.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.text = ''
        
    def OnCellChange(self, event):
        toolbar = self.GetParent().toolbar
        if (toolbar.GetToolEnabled(ID_UNDO) == False):
            toolbar.EnableTool(ID_UNDO, True)
        r = event.GetRow()
        c = event.GetCol()
        text = self.GetCellValue(r, c)
        # self.text - text before change
        # text - text after change
        undo = UndoText(self, self.text, text, r, c)
        stockUndo.append(undo)

        if stockRedo:
            # thie might be surprising, but it is a standard behaviour
            # in all spreadsheets
            del stockRedo[:]
            toolbar.EnableTool(ID_REDO, False)

    def OnColSize(self, event):
        toolbar = self.GetParent().toolbar

        if (toolbar.GetToolEnabled(ID_UNDO) == False):
            toolbar.EnableTool(ID_UNDO, True)

        pos = event.GetRowOrCol()
        size = self.GetColSize(pos)
        undo = UndoColSize(self, pos, size)
        stockUndo.append(undo)

        if stockRedo:
            del stockRedo[:]
            toolbar.EnableTool(ID_REDO, False)

    def OnRowSize(self, event):
        toolbar = self.GetParent().toolbar
        if (toolbar.GetToolEnabled(ID_UNDO) == False):
            toolbar.EnableTool(ID_UNDO, True)

        pos = event.GetRowOrCol()
        size = self.GetRowSize(pos)
        undo = UndoRowSize(self, pos, size)

        stockUndo.append(undo)
        if stockRedo:
            del stockRedo[:]
            toolbar.EnableTool(ID_REDO, False)

class Newt(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, -1, title, size = (550, 500))

        box = wx.BoxSizer(wx.VERTICAL)
        menuBar = wx.MenuBar()
        menu= wx.Menu()
        _quit = wx.MenuItem(menu, ID_QUIT, '&Quit\tCtrl+Q', 'Quits Newt')
        _quit.SetBitmap(wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/exit16.png')))
        menu.AppendItem(_quit)
        menuBar.Append(menu, '&File')
        self.Bind(wx.EVT_MENU, self.OnQuitNewt, id = ID_QUIT)
        self.SetMenuBar(menuBar)

        self.toolbar = wx.ToolBar(self, id = 1, style = wx.TB_HORIZONTAL | wx.NO_BORDER | \
                                  wx.TB_FLAT | wx.TB_TEXT)
        self.toolbar.AddSimpleTool(ID_UNDO, wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/undo.png')), \
                                                      'Undo', '')
        self.toolbar.AddSimpleTool(ID_REDO, wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/redo.png')), \
                                   'Redo', '')
        self.toolbar.EnableTool(ID_UNDO, False)

        self.toolbar.EnableTool(ID_REDO, False)
        self.toolbar.AddSeparator()
        self.toolbar.AddSimpleTool(ID_EXIT, wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/exit.png')), \
                                   'Quit', '')
        self.toolbar.Realize()
        self.toolbar.Bind(wx.EVT_TOOL, self.OnUndo, id = ID_UNDO)
        self.toolbar.Bind(wx.EVT_TOOL, self.OnRedo, id = ID_REDO)
        self.toolbar.Bind(wx.EVT_TOOL, self.OnQuitNewt, id = ID_EXIT)

        box.Add(self.toolbar, border = 5)
        box.Add((5, 10), 0)

        self.SetSizer(box)
        self.sheet1 = MySheet(self)
        self.sheet1.SetNumberRows(55)
        self.sheet1.SetNumberCols(25)

        for i in range(self.sheet1.GetNumberRows()):
            self.sheet1.SetRowSize(i, ID_ROWSIZE)

        self.sheet1.SetFocus()
        box.Add(self.sheet1, 1, wx.EXPAND)
        self.CreateStatusBar()
        self.Center()
        self.Show(True)

    def OnUndo(self, event):
        if len(stockUndo) == 0:
            return

        a = stockUndo.pop()
        if len(stockUndo) == 0:
            self.toolbar.EnableTool(ID_UNDO, False)

        a.undo()
        stockRedo.append(a)
        self.toolbar.EnableTool(ID_REDO, True)

    def OnRedo(self, event):
        if len(stockRedo) == 0:
            return

        a = stockRedo.pop()
        if len(stockRedo) == 0:
            self.toolbar.EnableTool(ID_REDO, False)

        a.redo()
        stockUndo.append(a)

        self.toolbar.EnableTool(ID_UNDO, True)

    def OnQuitNewt(self, event):
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    Newt(None, -1, 'Newt')
    app.MainLoop()
