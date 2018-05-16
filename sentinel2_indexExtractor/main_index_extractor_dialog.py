# -*- coding: utf-8 -*-
"""
/***************************************************************************
index_extractorDialog
							 A QGIS plugin
This plug-in extract several Vegetal Index from Sentinel-2 data
Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
						 -------------------
	begin                : 2018-03-08
	git sha              : $Format:%H$
	copyright            : (C) 2018 by Javier Balanzategui Sánchez
	email                : javier.balanzategui.sanchez@alumnos.upm.es
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

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem


FORM_CLASS, _ = uic.loadUiType(os.path.join(
	os.path.dirname(__file__), 'main_index_extractor_dialog_base.ui'))


class index_extractorDialog(QtWidgets.QDialog, FORM_CLASS):
	def __init__(self, parent=None):
		"""Constructor."""
		super(index_extractorDialog, self).__init__(parent)
		# Set up the user interface from Designer.
		# After setupUI you can access any designer object by doing
		# self.<objectname>, and you can use autoconnect slots - see
		# http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
		# #widgets-and-dialogs-with-auto-connect
		self.setupUi(self)


