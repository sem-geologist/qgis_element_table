# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ElementTableDockWidget
                                 A QGIS plugin
 This plugin alows to set/unset visibility of layer with chemical data with help of element table widget
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-12-07
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Petras Jokubauskas
        email                : p.jokubauskas@uw.edu.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import QtGui, QtWidgets 
from qgis.PyQt.QtCore import pyqtSignal
from .qpet.element_table import ElementTableGUI


class ElementTableDockWidget(QtWidgets.QDockWidget):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        super(ElementTableDockWidget, self).__init__(parent)
        self.et = ElementTableGUI(silent_disabled=True, disable_fancy=True)
        self.setWidget(self.et)
        self.setObjectName("dockWidgetChemicalSelector")
        self.setWindowTitle('Chemical table')
        
    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()