#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime
from pygame import mixer
import gtk
import os

from constantes import *


def get_(argv1, argv2):
    """
    """
    if 'src' in os.getcwd():
        return argv1
    else:
        return argv2


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
        a_ss = mi_form.spin_btn_ss.get_value()
        if (a_hh == t.hour) and (a_mm == t.minute) and (a_ss == t.second):
            mi_form.tbtn_alarma.set_active(False)
            mixer.music.play(-1)
            show_dialog()
            mixer.music.stop()
    return True


def init():
    """
        inicio el rep audio de PyGame
    """
    #try:
    #    mixer.music.load(SONG)
    #except:
    #    mixer.music.load(SONG_)
    mixer.init()
    mixer.music.load(get_(SONG, SONG_))


init()




