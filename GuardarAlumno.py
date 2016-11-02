#!/usr/bin/env python
# -*- coding: UTF8 -*-
#
# generated by wxGlade 0.6.7 (standalone edition) on Mon Dec 09 21:57:34 2013
#

import wx
import funciones as f
import PrincipalAdmin as PA
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
        
        # Menu Bar
        self.vntPpal_BarraMenu = wx.MenuBar()
        self.archivo = wx.Menu()
        self.principal = wx.MenuItem(self.archivo, wx.ID_ANY, _("Principal"), _("Principal"), wx.ITEM_NORMAL)
        self.archivo.AppendItem(self.principal)
        self.vntPpal_BarraMenu.Append(self.archivo, _("Archivo"))
        self.registros = wx.Menu()
        self.guardar = wx.MenuItem(self.registros, wx.ID_ANY, _("Guardar"), _("Guardar"), wx.ITEM_NORMAL)
        self.registros.AppendItem(self.guardar)
        self.registros.AppendSeparator()
        self.cancelar = wx.MenuItem(self.registros, wx.ID_ANY, _("Cancelar"), _("Cancelar"), wx.ITEM_NORMAL)
        self.registros.AppendItem(self.cancelar)
        self.vntPpal_BarraMenu.Append(self.registros, _("Registros"))
        self.ayuda = wx.Menu()
        self.vntPpal_BarraMenu.Append(self.ayuda, _("Ayuda"))
        self.SetMenuBar(self.vntPpal_BarraMenu)
        # Menu Bar end
        self.vntPpal_BarraEstado = self.CreateStatusBar(1, 0)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Guardar Alumno"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, _("Datos Personales"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, _(u"Datos Académicos"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, _("Nombres:"))
        self.txtNombre = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_9 = wx.StaticText(self, wx.ID_ANY, _(u"Sección:"))
        self.cobSeccion = wx.ComboBox(self, wx.ID_ANY, choices=[_("1"), _("2"), _("3"), _("4"), _("5"), _("6"), _("7"), _("8"), _("9"), _("10")], style=wx.CB_DROPDOWN)
        self.label_5 = wx.StaticText(self, wx.ID_ANY, _("Apellidos:"))
        self.txtApellido = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_10 = wx.StaticText(self, wx.ID_ANY, _("Carrera:"))
        self.cobCarrera = wx.ComboBox(self, wx.ID_ANY, choices=[_("Mantenimiento Naval"), _("Mecanica y Construccion Naval"), _("Ingenieria Mecanica")], style=wx.CB_DROPDOWN)
        self.label_6 = wx.StaticText(self, wx.ID_ANY, _(u"Cédula:"))
        self.txtCedula = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_7 = wx.StaticText(self, wx.ID_ANY, _("Sexo:"))
        self.cobSexo = wx.ComboBox(self, wx.ID_ANY, choices=[_("M"), _("F")], style=wx.CB_DROPDOWN)
        self.label_11 = wx.StaticText(self, wx.ID_ANY, _("Estado:"))
        self.cobEstado = wx.ComboBox(self, wx.ID_ANY, choices=[_("Amazonas"), _("Anzoategui"), _("Apure"), _("Aragua"), _("Barinas"), _("Bolivar"), _("Carabobo"), _("Cojedes"), _("Delta Amacuro"), _("Distrito Capital"), _("Falcon"), _("Guarico"), _("Lara"), _("Merida"), _("Miranda"), _("Monagas"), _("Nueva Esparta"), _("Portuguesa"), _("Sucre"), _("Tachira"), _("Trujillo"), _("Vargas"), _("Yaracuy"), _("Zulia")], style=wx.CB_DROPDOWN)
        self.label_11_copy = wx.StaticText(self, wx.ID_ANY, _("Municipio:"))
        self.cobMunicipio = wx.ComboBox(self, wx.ID_ANY, choices=["", "", "", "", ""], style=wx.CB_DROPDOWN)
        self.label_11_copy_1 = wx.StaticText(self, wx.ID_ANY, _("Parroquia:"))
        self.cobParroquia = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.label_8 = wx.StaticText(self, wx.ID_ANY, _(u"Dirección:"))
        self.cobDireccion = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.button_1 = wx.Button(self, wx.ID_ANY, _("Guardar"))
        self.button_2 = wx.Button(self, wx.ID_ANY, _("Limpiar"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnPrincipal, self.principal)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnApe, self.txtNombre)
        self.Bind(wx.EVT_TEXT, self.OnLetras, self.txtNombre)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnCed, self.txtApellido)
        self.Bind(wx.EVT_TEXT, self.OnLetras, self.txtApellido)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnSex, self.txtCedula)
        self.Bind(wx.EVT_TEXT, self.OnCedula, self.txtCedula)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEst, self.cobSexo)
        self.Bind(wx.EVT_TEXT, self.OnEstado, self.cobEstado)
        self.Bind(wx.EVT_TEXT, self.OnMunicipio, self.cobMunicipio)
        self.Bind(wx.EVT_TEXT, self.OnParroquia, self.cobParroquia)
        self.Bind(wx.EVT_BUTTON, self.OnGuardar, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnLimpiar, self.button_2)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Guardar Alumnos"))
        self.SetSize((604, 400))
        self.vntPpal_BarraEstado.SetStatusWidths([-1])
        # statusbar fields
        vntPpal_BarraEstado_fields = [_("Listo")]
        for i in range(len(vntPpal_BarraEstado_fields)):
            self.vntPpal_BarraEstado.SetStatusText(vntPpal_BarraEstado_fields[i], i)
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.cobSeccion.SetSelection(-1)
        self.cobCarrera.SetSelection(-1)
        self.cobSexo.SetSelection(-1)
        self.cobEstado.SetSelection(-1)
        self.cobMunicipio.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        vntPrincipal = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(12, 4, 0, 0)
        sizer_1.Add(self.label_1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 20)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_3, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.label_4, 0, 0, 0)
        grid_sizer_1.Add(self.txtNombre, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_9, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.cobSeccion, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_5, 0, 0, 0)
        grid_sizer_1.Add(self.txtApellido, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_10, 0, 0, 0)
        grid_sizer_1.Add(self.cobCarrera, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_6, 0, 0, 0)
        grid_sizer_1.Add(self.txtCedula, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_7, 0, 0, 0)
        grid_sizer_1.Add(self.cobSexo, 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_11, 0, 0, 0)
        grid_sizer_1.Add(self.cobEstado, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_11_copy, 0, 0, 0)
        grid_sizer_1.Add(self.cobMunicipio, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_11_copy_1, 0, 0, 0)
        grid_sizer_1.Add(self.cobParroquia, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.label_8, 0, 0, 0)
        grid_sizer_1.Add(self.cobDireccion, 0, wx.EXPAND, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add((20, 20), 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(3)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        vntPrincipal.Add(sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(vntPrincipal)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnPrincipal(self, event):  # wxGlade: Principal.<event_handler>
        dlg = wx.MessageDialog(None, '¿Desea Salir?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            Ventana=PA.Principal(self)
            Ventana.Show()
            self.Hide()
        dlg.Destroy()   

    def OnApe(self, event):  # wxGlade: Principal.<event_handler>
        self.txtApellido.SetFocus()

    def OnCed(self, event):  # wxGlade: Principal.<event_handler>
        self.txtCedula.SetFocus()

    def OnSex(self, event):  # wxGlade: Principal.<event_handler>
        self.cobSexo.SetFocus()

    def OnEst(self, event):  # wxGlade: Principal.<event_handler>
        self.cobEstado.SetFocus()

    def OnEstado(self, event):  # wxGlade: Principal.<event_handler>
        f.BuscarM(self)

    def OnMunicipio(self, event):  # wxGlade: Principal.<event_handler>
        f.BuscarP(self)

    def OnGuardar(self, event):  # wxGlade: Principal.<event_handler>
        if self.Validate():
            f.conexion()
            f.GuardarAlumno(self)
    def OnLimpiar(self, event):  # wxGlade: Principal.<event_handler>
        #self.txtNombre.Clear()
        #self.txtApellido.Clear()
        self.txtCedula.Clear()
        self.cobSexo.Clear()
        self.cobEstado.Clear()
        self.cobMunicipio.Clear()
        self.cobParroquia.Clear()
        self.cobDireccion.Clear()
    def OnLetras(self, event):  # wxGlade: Principal.<event_handler>
        frm=self
        Campo=frm.txtNombre.GetValue()
        Campo2=frm.txtApellido.GetValue()
        for i in Campo:
            if chr(33)==i or chr(34)==i or chr(35)==i or chr(36)==i or chr(37)==i or chr(38)==i or chr(39)==i or chr(40)==i or chr(41)==i or chr(42)==i or chr(43)==i or chr(44)==i or chr(45)==i or chr(46)==i or chr(47)==i or chr(48)==i or chr(49)==i or chr(50)==i or chr(51)==i or chr(52)==i or chr(53)==i or chr(54)==i or chr(55)==i or chr(56)==i or chr(57)==i or chr(58)==i or chr(59)==i or chr(60)==i or chr(61)==i or chr(62)==i or chr(63)==i:
                dlg=wx.MessageDialog(self,'Debe Ingresar Solo Letras', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                pass
        for i in Campo2:
            if chr(33)==i or chr(34)==i or chr(35)==i or chr(36)==i or chr(37)==i or chr(38)==i or chr(39)==i or chr(40)==i or chr(41)==i or chr(42)==i or chr(43)==i or chr(44)==i or chr(45)==i or chr(46)==i or chr(47)==i or chr(48)==i or chr(49)==i or chr(50)==i or chr(51)==i or chr(52)==i or chr(53)==i or chr(54)==i or chr(55)==i or chr(56)==i or chr(57)==i or chr(58)==i or chr(59)==i or chr(60)==i or chr(61)==i or chr(62)==i or chr(63)==i:
                dlg=wx.MessageDialog(self,'Debe Ingresar Solo Letras', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                pass

    def OnCedula(self, event):  # wxGlade: Principal.<event_handler>
        frm=self
        Campo=frm.txtCedula.GetValue()
        if len(Campo)> 8:
            dlg=wx.MessageDialog(self,'La Cedula no debe ser mayor a 8 caracteres', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            if Campo.isdigit():
                pass
            else:
                dlg=wx.MessageDialog(self,'No puede Tener Letras', 'Atencion', wx.OK)
                dlg.ShowModal()
                dlg.Destroy() 
    def OnParroquia(self, event):  # wxGlade: Principal.<event_handler>
        f.BuscarD(self)

# end of class Principal
class ContieneDatos(wx.PyValidator):
    def __init__(self):
        wx.PyValidator.__init__(self)

    def Clone(self):
        """
        Note que todo validador debe implementar
        # el método Clone().
        """
        return ContieneDatos()

    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        if len(text) == 0:
            wx.MessageBox("Este campo debe contener algun texto!",
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
