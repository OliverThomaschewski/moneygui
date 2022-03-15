from dataclasses import replace
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import sys

"""
TODO

-Bestätigungsfenster bei speichern mit auflistung der daten
-Nicht alles bis zum Rand => formatieren
-executable mit datenbank draus machen

Dividenden
- Eintrag der alten dividenden (oder halt die mühe machen)


Assets

-Felder nach eingabe löschen
-Bei Tab im letzten eingabefeld auf " Speichern" springen
-Layout der labels und eingabefenster einheitlich machen
-hinzufügen neuer Assets

"""


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle("Vermögensverwaltung")
        self.initUI()

    def initUI(self):

        # Liste der Aktien

        aktien = ["Allianz", "Digital Realty", "Rational", "Unilever", "Microsoft", "NextEra Energy", "AbbVie", "Realty Income",
                  "Accenture", "Munich Re", "Waste Management", "Caterpillar", "Walt Disney", "BlackRock", "Johnson & Johnson",
                  "Taiwan Semiconductor", "3M", "Ecolab", "W.P. Carey", "Hexagon", "Texas Instrument", "Equinix", "Tencent",
                  "Linde", "Fastenal", "Canadian National Railway", "Walmart", "Home Depot", "UPS", "Cisco Systems", "NVIDIA",
                  "Mayr Melnhof Karton", "Fortescue Metals", "McDonald's"]

        # Registerkarten
        self.tabs = QTabWidget()
        self.tab_div = QWidget()
        self.tab_ass = QWidget()

        # Hinzufügen
        self.tabs.addTab(self.tab_div, "Dividenden")
        self.tabs.addTab(self.tab_ass, "Assets")
        self.tabs.setCurrentIndex(0)

        # Kalender
        self.cal_div = QCalendarWidget(self)

        # DIVIDENDEN TAB

        # Layout festlegen
        self.tab_div.layout = QVBoxLayout()
        self.tab_div.setLayout(self.tab_div.layout)

        # Aktienauswahl
        self.auswahl_layout = QHBoxLayout()
        self.stock_label = QLabel(self)
        self.stock_label.setText("Aktie")
        self.cb_aktien = QComboBox(self)
        self.cb_aktien.addItems(aktien)
        self.auswahl_layout.addWidget(self.stock_label)
        self.auswahl_layout.addWidget(self.cb_aktien)

        # Eingabefeld mit Label
        self.insert_field = QHBoxLayout()
        self.amt_label = QLabel(self)
        self.amt_label.setText("Betrag")
        self.amt_field = QLineEdit(self)

        self.insert_field.addWidget(self.amt_label)
        self.insert_field.addWidget(self.amt_field)

        # Speicherbutton Dividenden
        self.bt_savediv = QtWidgets.QPushButton(self)
        self.bt_savediv.setText("Speichern")
        self.bt_savediv.clicked.connect(self.save_div)
        self.amt_field.returnPressed.connect(self.save_div)

        # Dividenenfenster Zusammenpacken
        self.setCentralWidget(self.tabs)
        self.tab_div.layout.addWidget(self.cal_div)
        self.tab_div.layout.addLayout(self.auswahl_layout)
        self.tab_div.layout.addLayout(self.insert_field)
        self.tab_div.layout.addWidget(self.bt_savediv)

        # ASSETS TAB

        # Layout festlegen
        self.tab_ass.layout = QVBoxLayout()
        self.tab_ass.setLayout(self.tab_ass.layout)

        # Kalender
        self.cal_ass = QCalendarWidget(self)

        # Speicherbutton Assets
        self.bt_saveass = QtWidgets.QPushButton(self)
        self.bt_saveass.setText("Speichern")
        self.bt_saveass.clicked.connect(self.save_ass)

        # Großer Rahmen für Beträge
        self.eingabe_layout = QVBoxLayout()

        # Einzelne Felder
        self.not_layout = QHBoxLayout()
        self.not_label = QLabel(self)
        self.not_label.setText("Notgroschen")
        self.not_field = QLineEdit(self)
        self.not_layout.addWidget(self.not_label)
        self.not_layout.addWidget(self.not_field)

        self.rent_layout = QHBoxLayout()
        self.rent_label = QLabel(self)
        self.rent_label.setText("Rentenversicherung")
        self.rent_field = QLineEdit(self)
        self.rent_layout.addWidget(self.rent_label)
        self.rent_layout.addWidget(self.rent_field)

        self.comdirect_layout = QHBoxLayout()
        self.comdirect_label = QLabel(self)
        self.comdirect_label.setText("Comdirect")
        self.comdirect_field = QLineEdit(self)
        self.comdirect_layout.addWidget(self.comdirect_label)
        self.comdirect_layout.addWidget(self.comdirect_field)

        self.tr_layout = QHBoxLayout()
        self.tr_label = QLabel(self)
        self.tr_label.setText("Trade Republic")
        self.tr_field = QLineEdit(self)
        self.tr_layout.addWidget(self.tr_label)
        self.tr_layout.addWidget(self.tr_field)

        self.sc_layout = QHBoxLayout()
        self.sc_label = QLabel(self)
        self.sc_label.setText("Scalable Capital")
        self.sc_field = QLineEdit(self)
        self.sc_layout.addWidget(self.sc_label)
        self.sc_layout.addWidget(self.sc_field)

        self.mintos_layout = QHBoxLayout()
        self.mintos_label = QLabel(self)
        self.mintos_label.setText("Mintos")
        self.mintos_field = QLineEdit(self)
        self.mintos_layout.addWidget(self.mintos_label)
        self.mintos_layout.addWidget(self.mintos_field)

        self.ecologio_layout = QHBoxLayout()
        self.ecologio_label = QLabel(self)
        self.ecologio_label.setText("Ecologio")
        self.ecologio_field = QLineEdit(self)
        self.ecologio_layout.addWidget(self.ecologio_label)
        self.ecologio_layout.addWidget(self.ecologio_field)

        self.kredit_layout = QHBoxLayout()
        self.kredit_label = QLabel(self)
        self.kredit_label.setText("Kredit")
        self.kredit_field = QLineEdit(self)
        self.kredit_layout.addWidget(self.kredit_label)
        self.kredit_layout.addWidget(self.kredit_field)

        self.bar_layout = QHBoxLayout()
        self.bar_label = QLabel(self)
        self.bar_label.setText("Bargeld")
        self.bar_field = QLineEdit(self)
        self.bar_layout.addWidget(self.bar_label)
        self.bar_layout.addWidget(self.bar_field)

        # Eingabefenster zusammenbauen

        self.eingabe_layout.addLayout(self.not_layout)
        self.eingabe_layout.addLayout(self.rent_layout)
        self.eingabe_layout.addLayout(self.comdirect_layout)
        self.eingabe_layout.addLayout(self.tr_layout)
        self.eingabe_layout.addLayout(self.sc_layout)
        self.eingabe_layout.addLayout(self.mintos_layout)
        self.eingabe_layout.addLayout(self.ecologio_layout)
        self.eingabe_layout.addLayout(self.kredit_layout)
        self.eingabe_layout.addLayout(self.bar_layout)

        # Kalender und Eingabe zusammenfassen
        self.calentry_layout = QHBoxLayout()
        self.calentry_layout.addWidget(self.cal_ass)
        self.calentry_layout.addLayout(self.eingabe_layout)

        # kalendereingabe Layout und button zusammen

        self.tab_ass.layout.addLayout(self.calentry_layout)
        self.tab_ass.layout.addWidget(self.bt_saveass)

    # Onclick funktion zum speichern der Dividenden

    

    def save_div(self):
        betrag = self.convert_values(self.amt_field.text())
        datum = self.cal_div.selectedDate().toString("yyyy-MM-dd")
        stock = self.cb_aktien.currentText()
        conn = sqlite3.connect(".\\assets\\money.db")
        cur = conn.cursor()
        insert_string = f"""INSERT INTO dividenden VALUES ("{datum}", "{stock}", "{betrag}")"""

        cur.execute(insert_string)
        conn.commit()
        self.amt_field.setText("")

    # Onclick Funktion zum speichern der Assets
    def save_ass(self):
        datum = self.cal_ass.selectedDate().toString("yyyy-MM-dd")
        betr_not = self.convert_values(self.not_field.text())
        betr_rente = self.convert_values(self.rent_field.text())
        betr_comdirect = self.convert_values(self.comdirect_field.text())
        betr_tr = self.convert_values(self.tr_field.text())
        betr_sc = self.convert_values(self.sc_field.text())
        betr_mintos = self.convert_values(self.mintos_field.text())
        betr_ecologio = self.convert_values(self.ecologio_field.text())
        betr_kredit = self.convert_values(self.kredit_field.text())
        betr_bar = self.convert_values(self.bar_field.text())

        insert_string = f"""INSERT INTO assets VALUES ("{datum}", "{betr_not}", "{betr_rente}", "{betr_comdirect}", "{betr_tr}", "{betr_sc}", "{betr_mintos}", "{betr_ecologio}", "{betr_kredit}", "{betr_bar}")"""
        conn = sqlite3.connect(".\\assets\\money.db")
        cur = conn.cursor()

        cur.execute(insert_string)
        conn.commit()

        self.not_field.setText("")
        self.rent_field.setText("")
        self.comdirect_field.setText("")
        self.tr_field.setText("")
        self.sc_field.setText("")
        self.mintos_field.setText("")
        self.ecologio_field.setText("")
        self.kredit_field.setText("")
        self.bar_field.setText("")
       

    def convert_values(self, eingabe):
        """
        Konvertiert Eingabe in float
        """
        if not eingabe:
            return float(0)

        try:
            value = float(eingabe)
        except ValueError:
            value = float(eingabe.replace(",", "."))
        finally:
            return value


app = QApplication(sys.argv)
win = MyWindow()
win.show()
sys.exit(app.exec_())
