﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
from gtk import glade

from extend import get_
from constantes import XMLF, XMLF_

#importe aqui los Form que utilizara su App, por ejemplo:
import frm_clock


class MiApp:
    def __init__(self):
        #parse referente al XML remplace ".glade" por el nombre
        #del archivo generado por glade que usara
        self.xml = glade.XML(get_(XMLF, XMLF_))

        #Aplicacion principal
        #llame aqui a todas las ventanas que utilizara por ejemplo:
        self.frm_main = frm_clock.Form(self.xml)
        self.frm_main.show()

    def main(self):
        #pasar el control principal a GTK
        gtk.main()

    def destroy(self):
        #detener la ejecucion de la aplicacion
        gtk.main_quit()

if __name__ == "__main__":
    app = MiApp()
    app.main()
