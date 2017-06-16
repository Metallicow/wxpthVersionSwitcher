#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description
===========

Quickly edit your wx.pth file in site-packages

License: wxPython/wxWidgets
"""

#-Imports---------------------------------------------------------------------

#--Python Imports.
import os
import sys
import platform
from collections import OrderedDict

#--wxPython Imports.
import wx
from wx.lib.embeddedimage import PyEmbeddedImage

#-Globals---------------------------------------------------------------------

wxpth = os.path.join('C:\\', 'Python27', 'Lib', 'site-packages', 'wx.pth')
# wxpth = os.path.join('C:\\', 'Python33', 'Lib', 'site-packages', 'wx.pth')

versioninfos = (
    '\n' +
    '    python version = ' + str(platform.python_version()) + '    \n' +
    '    wxpython version = ' + str(wx.version()) + '    \n' +
    '    sys.executable = ' + str(sys.executable) + '    \n' +
    '    sys.prefix = ' + str(sys.prefix) + '    \n'
                )

wxpython16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAADoklEQVQYGY3Ae1ATBBwH8B8Z"
    "1BESpq3qSDDqSrvTOLsTICJUT495AgyIt3XENg2dAxgbGw5gDBgMBhtESAgwaOLgYCitQ4OD"
    "U5SXikozuaPiFA1ORFfEAL5td3LX9ZcfsjldW6toaGlZERcqVn/q+Rmd5zqndDqdIz0PZVEp"
    "49rlawsdvYNw9N0L/aAJI30jK0plqTP9j9FodBKJRGH0Xzz+sS5RKWc182woQtsckFARgLRT"
    "h5bqvm8UkZVer3fIz893IyuhUNjq6ur6j1Qq7aA1fFXoxDd/EMQLBAUIIjPh6A1CfHz8fIZQ"
    "fD07O3sgPT19iMNmDzGZzHkXFxdzSEjIvEQiaRAIBF2Udz6iV7JMYA8ROMOEk0sE6cON2LM3"
    "YGnTa68jLjbyUaZYMPzx9q1PwsKCx729fX4zGAw+ERERZhaLNUclDZJ6/n0HJP9J4JkIKXME"
    "1dWYqXJFdZFMrrhz+Ihsmp1SbjqcVGJKE+VOVVRUMsmKzz8xkZOT3UgyiVyTmn5ghde7xXLk"
    "JiGy1hkadY2WrMZ+meYmyfrgtq9+leFfj6zK6530zDGeYEirbfIkrUpV1SAuUydxucVf9q5D"
    "cN27q601zXFkNWro48pqhsHwq8YbvhUoq6q5ax47xJkbOsDvOiv1IZuqLKlJI8rNLPtOrAq9"
    "YAc39fuLdzXlanNc5JWxNMnvJypG4eRdj/2xhZgdjoDl0kdYurQdTwYCDGSj0zXz9fXnAkrb"
    "Y+8dfUAIL/GandFUD1r8vXDD6VWwAzPh9mndYjCn0rI0KQH6t2DG4IZJ455uWtPW2PZZ7pXN"
    "2NVNiCuK7l/UtRrNQfuxYEf4y/kVRO0MS5TkclIxLcFyjzsen38TjerEEe0ZowfZyPO+1srv"
    "vww/I0FSfPzUcqXGsOznjx/dCTHh62DPsrckp2679/cttgUjviu4vXPlYnPCTTY3WUE2BcWB"
    "xpxZe6TN2CFUefBOy3Hu1SSmCxhVhOgHhN0DBGb7i2DlHhzTNfE+HO2Te+rbKtuCI5ndZKOU"
    "ZZTIxteDN01wLHTA5w0bEHWbkDBJKBhfj5x+ZySaCG8rHcASBvUkK4oEX6m8FvPkMgHZXDCM"
    "MIpPBz3Ne0xImiCkPCIULdqBXc5Y3rV1W80HG90zotI2z5SYX0D0r4QNWQTpt1EPL3ZcdqQ1"
    "6oKyQK5gx3zymZeQ3umIfTGbZjzf2xFOz3zi4ftOwBdv3Qr/gRAs9Hja3tThRVb/AuDb4Oow"
    "/S8iAAAAAElFTkSuQmCC")



class GradientPanel(wx.Panel):
    """"""
    def __init__(self, parent, id=wx.ID_ANY,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=0, name='panel'):
        """"""
        wx.Panel.__init__(self, parent, id, pos, size, style, name)

        wxRAISED_BORDER = wx.RAISED_BORDER

        staticwxversion = wx.StaticText(self, -1, versioninfos, style=wxRAISED_BORDER)
        staticwxversion.SetBackgroundColour(wx.BLACK)
        staticwxversion.SetForegroundColour(wx.WHITE)

        self.btnsDict = OrderedDict([
            (101, ['wx-2.8-msw-unicode'    , 'Switch to wxPython 2.8 Classic'  ]),
            (102, ['wx-2.9.5-msw'          , 'Switch to wxPython 2.9.5 Classic']),
            (103, ['wx-3.0-msw'            , 'Switch to wxPython 3.0.0 Classic']),
            (104, ['wx-4.0.0-msw-phoenix'  , 'Switch to wxPython 4.0.0 Phoenix']),
            ])

        wxBoxSizer = wx.BoxSizer
        wxVERTICAL = wx.VERTICAL
        wxHORIZONTAL = wx.HORIZONTAL
        wxEXPAND = wx.EXPAND
        wxALL = wx.ALL
        wxCENTER = wx.CENTER

        vbSizer = wxBoxSizer(wxVERTICAL)
        hbSizer = wxBoxSizer(wxHORIZONTAL)
        vbSizer.Add(staticwxversion, 0, wxEXPAND | wxALL | wxCENTER, 6)

        wxEVT_BUTTON = wx.EVT_BUTTON
        self_OnSwitch_wxpth = self.OnSwitch_wxpth

        for key, value in list(self.btnsDict.items()):
            btn = wx.Button(self, key, label=value[0], style=wxRAISED_BORDER)
            btn.SetToolTip(wx.ToolTip(value[1]))
            btn.Bind(wxEVT_BUTTON, self_OnSwitch_wxpth)
            vbSizer.Add(btn, 0, wxEXPAND | wxALL | wxCENTER, 8)

        hbSizer.Add(vbSizer, 1, wxEXPAND | wxALL | wxCENTER, 0)
        self.SetSizer(hbSizer)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def Draw(self, dc):
        """"""
        dc.GradientFillLinear(self.GetClientRect(), '#062129', '#83F682')

    def OnPaint(self, event):
        """"""
        dc = wx.PaintDC(self)
        self.Draw(dc)

        event.Skip()

    def OnSize(self, event):
        """"""
        event.Skip()
        self.Refresh()

    def OnSwitch_wxpth(self, event):
        """"""
        if not os.path.exists(wxpth):
            wx.MessageBox('%s\ncannot be found!' % wxpth, 'Error')
        else:
            text_file = open(wxpth, 'w')
            text_file.write(self.btnsDict[event.GetId()][0])
            text_file.close()
        print(sys._getframe(0).f_code.co_name,
              self.btnsDict[event.GetId()][0])


class MainWindow(wx.Frame):
    """"""
    def __init__(self, parent=None, id=wx.ID_ANY, title='wx.pth switcher',
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        """"""
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)

        self.SetBackgroundColour(wx.BLACK)
        self.gradpanel = GradientPanel(self)

        vbSizer = wx.BoxSizer(wx.VERTICAL)
        vbSizer.Add(self.gradpanel, 1, wx.EXPAND | wx.ALL, 8)

        self.SetSizer(vbSizer)
        self.SetAutoLayout(True)
        self.Fit()

        sz = self.GetSize()
        self.SetSizeHints(sz[0], sz[1])

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)

    def OnSize(self, event):
        """"""
        event.Skip()
        self.Refresh()

    def Draw(self, dc):
        """"""
        dc.GradientFillLinear(self.GetClientRect(), '#83F682', '#062129')

    def OnPaint(self, event):
        """"""
        dc = wx.PaintDC(self)
        self.Draw(dc)

        event.Skip()

#=============================================================================


class wxpthSwitcherApp(wx.App):
    """"""
    def OnInit(self):
        """"""
        gMainWin = MainWindow()
        gMainWin.SetDoubleBuffered(True)
        gMainWin.SetIcon(wxpython16.GetIcon())
        gMainWin.Centre()
        gMainWin.Show(True)

        return True


def LaunchTheApp():
    app = wxpthSwitcherApp(0)
    app.MainLoop()


if __name__ == "__main__":
    LaunchTheApp()
