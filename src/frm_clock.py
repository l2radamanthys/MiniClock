﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Plantilla creada por Ricardo D. Quiroga
# licencia: GPL2
# email: l2radamanthys@gmail.com, ricardoquiroga.dev@gmail.com
# http://www.l2radamanthys.tk

import pygtk
pygtk.require('2.0')
import gtk
import gobject #*
from gtk import glade

import time
import datetime

from pygame import mixer


def create(xml):
    return Form(xml)


ATRIB = 'font_desc="Alien Encounters 44"'
TAG_INI = "<span %s>" %ATRIB
TAG_END = "</span>"


#inicio el rep audio
mixer.init()
mixer.music.load('data/sounds/hello.wav')


def run_clock(mi_form):
    """
        muestra la hora del reloj
    """
    #lbl_hora.set_text("<span font_desc=\"Courier 44\">" + time.strftime("%H:%M:%S") + "</span>")
    #lbl_hora.set_markup('<span font_desc="Courier 44">hola</span>')
    hora = time.strftime("%H:%M:%S")
    mi_form.lbl_hora.set_markup(TAG_INI + hora + TAG_END)
    return True


def show_dialog():
    """
        Generarara un MensajeDialog que Dice Alarma
    """
    mi_dialog = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
    mi_dialog.set_markup(TAG_INI + "Alarma" + TAG_END)
    mi_dialog.run()
    mi_dialog.hide()


def ctlr_alarma(mi_form):
    """
        Lanza la alamarma si el boton esta activo
    """
    if mi_form.tbtn_alarma.get_active():
        t = datetime.datetime.today()
        #alarma
        a_hh = mi_form.spin_btn_hh.get_value()
        a_mm = mi_form.spin_btn_mm.get_value()
        if (a_hh == t.hour) and (a_mm == t.minute):
            mi_form.tbtn_alarma.set_active(False)
            mixer.music.play(-1)
            show_dialog()
            mixer.music.stop()
    return True


class Form:
    """
        Clase para manejar mas comodamente una ventana dentro de Gtk
    """
    def __init__(self, xml=None):
        self.xml = xml #parse referente al XML

        #extraemos el referente a la ventana
        #remplace frm_* por el nombre de la ventana que quiere manejar con esta clase
        self.ventana = self.xml.get_widget('window1')

        #------------------------------------Elementos --------------------------------------#
        #estraiga aqui los elementos con los cuales trabajara, por ejemplos cajas de texto
        #botones con eventos especiales, tablas, etc.
        self.lbl_hora = self.xml.get_widget('lbl_hora')
        self.tbtn_alarma = self.xml.get_widget('tbtn_alarma')
        self.spin_btn_hh = self.xml.get_widget('spin_btn_hh')
        self.spin_btn_mm = self.xml.get_widget('spin_btn_mm')
        self.spin_btn_ss = self.xml.get_widget('spin_btn_ss')

        #listado de seniales que se conetaran automaticamente
        #agregue aqui todas las seniales(eventos tales como click sobre un boton etc.)
        #que quiere conectar, por el momento esto se tiene que hacer a mano
        self.seniales = {
            'on_btn_salir_clicked': self.app_destroy,
            #'on_tbtn_alarma_toggled': self.tbtn_alarma_toggled,
        }

        #conectamos automaticamente el listado de eventos
        self.xml.signal_autoconnect(self.seniales)

        #Por defecto la ventana aparece como visible, en caso de no querer mostrar pasar False como
        #parametro a la funcion show() ,opcionalmente se puede llamar a la funcion ocultar
        self.show(False)

        #self.alarma_activa = True

        t = datetime.datetime.today()
        self.spin_btn_hh.set_value(t.hour)
        self.spin_btn_mm.set_value(t.minute)
        self.spin_btn_ss.set_value(t.second)


        self.lbl_hora.value = time.strftime("%H:%M:%S")
        self.timer = gobject.timeout_add(100, run_clock, self)
        self.timer2 = gobject.timeout_add(100, ctlr_alarma, self)






    def show(self, opc=True):
        """
            Mostrar o no la ventana, por defecto les True, se deve pasar
        false como parametro en caso de querer ocultarla, llamo este metodo
        en caso de que por defecto no se pueda mostrar todos los elementos
        de la ventana.
        """
        self.ventana.show_all()
        if opc:
            #mostrar la ventana
            self.ventana.show()
        else:
            #ocultarla
            self.ventana.hide()


    def ocultar(self, widget, *args):
        """
            Evento Ocultar, oculta todos los elementos de la ventana.
        """
        self.show(False)
        self.ventana.hide_all()


    def app_destroy(self, widget, *args):
        """
            Detiene la aplicacion por completo, y devuelve el mando
        """
        gtk.main_quit()

    #----------------------------- Metodos ---------------------------------#



    #----------------------------- Eventos ---------------------------------#
    #agregue aqui sus eventos
    def evt_mi_evento(self, widget, *args):
        pass

    #def tbtn_alarma_toggled(self, widget, *args):
    #    self.alarma_activa = not(self.alarma_activa)




