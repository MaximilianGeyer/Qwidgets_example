from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit, QRadioButton, QCheckBox, QButtonGroup


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        # Text einblenden (Beschriftung)
        # 1.0 Kennzeichenerkennung
        label_edit = QLabel(":Stückzahl")

        label_username = QLabel("Benutzername:")
        label_password = QLabel("Kennwort:")
        label_password.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_mac = QLabel("MAC-Adresse:")



        #Instanzenerzeugt, die Texteingabe ermöglichen
        #1.1 Kennzeichenerkennung:
        line_edit = QLineEdit()
        line_edit1 = QLineEdit()
        line_edit2 = QLineEdit()
        line_edit3 = QLineEdit()

        lineedit_username = QLineEdit()
        lineedit_password = QLineEdit()
        lineedit_password.setEchoMode(QLineEdit.EchoMode.Password)


        # Eingabemasken definiert
        #1.2 Kennzeichenerkennung:
        input_mask = "D00;_"  # Zahlen bis 999    ;_ spezifiziert, dass das Füllzeichen ein Unterstrich (_) ist.
        input_user = ">A!A>A!AAaaa0;_"
        input_kennzeichen = ">A!Aa:>Aa:D000>a;_"  # Autokennzeichen
        input_age = "0D.0D.000D;_"  # Geburtsdatum


        # zuvor definierten Eingabemasken den jeweiligen QLineEdit-Widgets zugewiesen.
        # 1.3 Kennzeichenerkennung:
        line_edit.setInputMask(input_mask)
        line_edit1.setInputMask(input_user)
        line_edit2.setInputMask(input_kennzeichen)
        line_edit3.setInputMask(input_age)

        # mac Adresse Eingabefeld
        lineedit_mac = QLineEdit()
        lineedit_mac.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        # eine Auswahl Button
        radio_button_IP = QRadioButton("IP-Adresse")
        radio_button_MAC = QRadioButton("MAC-Adresse")
        radio_button_group = QButtonGroup()
        radio_button_group.addButton(radio_button_IP)
        radio_button_group.addButton(radio_button_MAC)
        # mehrere abhaken Button
        check_box_no_echo = QCheckBox("Kennwort im Klartext")
        check_box_length = QCheckBox("Mindestlänge des Kennworts")

        layout = QGridLayout()
        layout.addWidget(label_username, 1, 1)
        layout.addWidget(lineedit_username, 1, 2)
        layout.addWidget(label_password, 2, 1)
        layout.addWidget(lineedit_password, 2, 2)
        # mac Adresse Eingabefeld
        layout.addWidget(label_mac, 3, 1)
        layout.addWidget(lineedit_mac, 3, 2)
        # eine Auswahl Button
        layout.addWidget(radio_button_IP, 4, 1)
        layout.addWidget(radio_button_MAC, 5, 1)
        # mehrere abhaken Button
        layout.addWidget(check_box_no_echo, 4, 2)
        layout.addWidget(check_box_length, 5, 2)

        #zu einem Layout hinzugefügt
        #line_edit wird zur Position (9, 1) hinzugefügt und nimmt 1 Zeile und 1 Spalte ein.
        #1.4 Kennzeichenerkennung:
        layout.addWidget(line_edit, 9, 1, 1, 1)
        layout.addWidget(label_edit, 9, 2, 1, 1)
        layout.addWidget(line_edit1, 10, 1, 1, 1)
        layout.addWidget(line_edit2, 11, 1, 1, 1)
        layout.addWidget(line_edit3, 12, 1, 1, 1)


        self.setLayout(layout)