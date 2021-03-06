#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.6.7 (standalone edition) on Tue Jan 07 22:25:09 2014
#

import wx
import funcionesSimu as f
import PrincipalAdmin as P
# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Ingrese la altura (mtrs):"))
        self.txtposinicial = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Simular"))
        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.principal = wx.MenuItem(wxglade_tmp_menu, wx.ID_ANY, _("Principal"), _("Principal"), wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.principal)
        self.frame_1_menubar.Append(wxglade_tmp_menu, _("Archivo"))
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end

        self.__set_properties()
        self.txtposinicial.SetValidator(ContieneDatos())#activa la validacion
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.OnLetras, self.txtposinicial)
        self.Bind(wx.EVT_BUTTON, self.OnSimulador, self.button_1)
        self.Bind(wx.EVT_MENU, self.OnPrincipal, self.principal)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Caida Libre"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_1.Add(self.label_1, 0, 0, 0)
        grid_sizer_1.Add(self.txtposinicial, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnLetras(self, event):  # wxGlade: Principal.<event_handler>
        frm=self
        Campo=frm.txtposinicial.GetValue()
        if len(Campo)> 3:
            dlg=wx.MessageDialog(self,'No puede tener mas de 3 caracteres numericos', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            #self.txtposinicial.Clear()
        else:
            if Campo.isdigit():
                pass
            else:
                dlg=wx.MessageDialog(self,'No puede Tener Letras', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()     
                #self.txtposinicial.Clear()

    def OnSimulador(self, event):  # wxGlade: Principal.<event_handler>
        
        if self.Validate():
            frm=self
            #Can=float(self.txtposinicial.GetValue())
            Valor=frm.txtposinicial.GetValue()
            
            
            if Valor.isdigit()and len(Valor)<4:
                self.Close
                f.pelota(self)
            else:
                dlg=wx.MessageDialog(self,'No puede tener mas de 3 caracteres numericos ni letras', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()

    def OnPrincipal(self, event):  # wxGlade: Principal.<event_handler>
        
        Ventana=P.Principal(self)
        Ventana.Show()
        self.Hide()
         

    
# end of class Principal
class ContieneDatos(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)

    def Clone(self):
        """
        Note que todo validador debe implementar
        # el m�todo Clone().
        """
        return ContieneDatos()

    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        if len(text) == 0:
            wx.MessageBox("Este campo debe contener alg�n texto!",
                          "Error")
            textCtrl.SetBackgroundColour("red")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(
                               wx.SystemSettings_GetColour(
                               wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True

    def TransferToWindow(self):
        return True

    def TransferFromWindow(self):
        return True
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.App()
    #wx.InitAllImageHandlers()
    frame_1 = Principal(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
