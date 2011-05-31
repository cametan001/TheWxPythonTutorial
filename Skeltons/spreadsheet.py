#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# spreadsheet.py

from wx.lib import sheet
import wx, os.path

class MySheet(sheet.CSheet):
    def __init__(self, parent):
        sheet.CSheet.__init__(self, parent)
        self.row = self.col = 0
        self.SetNumberRows(55)
        self.SetNumberCols(25)

        for i in range(55):
            self.SetRowSize(i, 20)

    def OnGridSelectCell(self, event):
        self.row, self.col = event.GetRow(), event.GetCol()
        control = self.GetParent().GetParent().position
        value = self.GetColLabelValue(self.col) + self.GetRowLabelValue(self.row)
        control.SetValue(value)
        event.Skip()

class Newt(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, -1, title, size = (550, 500))

        fonts = ['Times New Roman', 'Times', 'Courier', 'Courier New', 'Helvetica', \
                 'Sans', 'verdana', 'utkal', 'aakar', 'Arial']
        font_sizes = ['10', '11', '12', '14', '16']

        box = wx.BoxSizer(wx.VERTICAL)
        menuBar = wx.MenuBar()

        menu1 = wx.Menu()
        menuBar.Append(menu1, '&File')
        menu2 = wx.Menu()
        menuBar.Append(menu2, '&Edit')
        menu3 = wx.Menu()
        menuBar.Append(menu3, '&Edit')
        menu4 = wx.Menu()
        menuBar.Append(menu4, '&Insert')
        menu5 = wx.Menu()
        menuBar.Append(menu5, 'F&omat')
        menu6 = wx.Menu()
        menuBar.Append(menu6, '&Tools')
        menu7 = wx.Menu()
        menuBar.Append(menu7, '&Data')
        menu8 = wx.Menu()
        menuBar.Append(menu8, '&Help')

        self.SetMenuBar(menuBar)

        toolbar1 = wx.ToolBar(self, -1, style = wx.TB_HORIZONTAL)
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_new.jpg')))
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_open.jpg')))
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_save.jpg')))
        toolbar1.AddSeparator()
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_cut.png')))
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_copy.png')))
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_paste.png')))
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_delete.png')))
        toolbar1.AddSeparator()
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_undo.png')))
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_redo.png')))
        toolbar1.AddSeparator()
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/incr22.jpg')))
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/decr22.jpg')))
        toolbar1.AddSeparator()
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/chart.jpg')))
        toolbar1.AddSeparator()
        toolbar1.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_exit.png')))

        toolbar1.Realize()

        toolbar2 = wx.ToolBar(self, wx.TB_HORIZONTAL | wx.TB_TEXT)

        self.position = wx.TextCtrl(toolbar2)
        font = wx.ComboBox(toolbar2, -1, value = 'Times', choices = fonts, size = (100, -1), \
                           style = wx.CB_DROPDOWN)
        font_height = wx.ComboBox(toolbar2, -1, value = '10', choices = font_sizes, \
                                  size = (50, -1), style = wx.CB_DROPDOWN)
        
        toolbar2.AddControl(self.position)
        toolbar2.AddControl(font)
        toolbar2.AddControl(font_height)
        toolbar2.AddSeparator()
        bold = wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_text_bold.png'))
        toolbar2.AddCheckTool(-1, bold)
        italic = wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_text_italic.png'))
        toolbar2.AddCheckTool(-1, italic)
        under = wx.Bitmap(os.path.join(os.path.dirname(__file__), 'icons/stock_text_bold.png'))
        toolbar2.AddCheckTool(-1, under)
        toolbar2.AddSeparator()
        toolbar2.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                             'icons/text_align_left.jpg')))
        toolbar2.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                             'icons/text_align_center.jpg')))
        toolbar2.AddLabelTool(-1, '', wx.Bitmap(os.path.join(os.path.dirname(__file__), \
                                                             'icons/text_align_right.jpg')))

        box.Add(toolbar1, border = 5)
        box.Add((5, 5), 0)
        box.Add(toolbar2)
        box.Add((5, 10), 0)

        toolbar2.Realize()
        self.SetSizer(box)
        notebook = wx.Notebook(self, -1, style = wx.RIGHT)

        sheet1 = MySheet(notebook)
        sheet2 = MySheet(notebook)
        sheet3 = MySheet(notebook)
        sheet1.SetFocus()

        notebook.AddPage(sheet1, 'Sheet1')
        notebook.AddPage(sheet2, 'Sheet2')
        notebook.AddPage(sheet3, 'Sheet3')

        box.Add(notebook, 1, wx.EXPAND)

        self.CreateStatusBar()
        self.Center()
        self.Show(True)

if __name__ == '__main__':
    app = wx.App()
    Newt(None, -1, 'SpreadSheet')
    app.MainLoop()
