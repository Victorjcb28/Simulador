#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.6.7 (standalone edition) on Mon Dec 08 14:25:32 2014
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
from Principal import Principal

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = Principal(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()