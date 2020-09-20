import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import resources


class MainWindow(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor"""
        super().__init__()

        #########################
        # Create widget objects #
        #########################
        self.setWindowTitle('Fight Fighter Game Lobby')
        cx_form = qtw.QWidget()
        self.setCentralWidget(cx_form)
        cx_form.setLayout(qtw.QFormLayout())
        heading = qtw.QLabel('Fight Fighter!')
        cx_form.layout().addRow(heading)
        inputs = {
            'Server' : qtw.QLineEdit(),
            'Name' : qtw.QLineEdit(),
            'Password': qtw.QLineEdit(
                echoMode = qtw.QLineEdit.Password
            ),
            'Team': qtw.QComboBox(),
            'Ready': qtw.QCheckBox('Check when ready')
        }
        teams = ('Crimson Sharks', 'Shawo Hawks', 'Night Terrors', 'Blue Crew')

        inputs['Team'].addItems(teams)

        for label, widget in inputs.items():
            cx_form.layout().addRow(label, widget)

        self.submit = qtw.QPushButton(
            'Connect',
            clicked = lambda: qtw.QMessageBox.information(
                None, 'Connecting', 'Prepare for Battele!'
            )
        )
        self.reset = qtw.QPushButton('Cancel', clicked = self.close)
        cx_form.layout().addRow(self.submit, self.reset)

        #setting a font
        heading_font = qtg.QFont('Impact', 32, qtg.QFont.Bold)
        heading_font.setStretch(qtg.QFont.ExtraExpanded)
        heading.setFont(heading_font)

        label_font = qtg.QFont()
        label_font.setFamily('Impact')
        label_font.setPointSize(14)
        label_font.setWeight(qtg.QFont.DemiBold)
        label_font.setStyle(qtg.QFont.StyleNormal)

        for inp in inputs.values():
            cx_form.layout().labelForField(inp).setFont(label_font)

        #dealing with missing fonts
        button_font = qtg.QFont(
            'Font Family XYZ', 15
        )

        button_font.setWeight(qtg.QFont.DemiBold)

        button_font.setStyleHint(qtg.QFont.Fantasy)
        button_font.setStyleStrategy(
            qtg.QFont.PreferAntialias |
            qtg.QFont.PreferQuality
        )
        actual_font = qtg.QFontInfo(button_font)
        print(f'Actual font used is {actual_font.family()}, {actual_font.pointSize()}')

        self.submit.setFont(button_font)
        self.reset.setFont(button_font)

        #adding images
        logo = qtg.QPixmap('logo.png')
        heading.setPixmap(logo)

        if logo.width() > 400:
            logo = logo.scaledToWidth(400, qtc.Qt.SmoothTransformation)

        go_pixmap = qtg.QPixmap(qtc.QSize(32, 32))
        stop_pixmap = qtg.QPixmap(qtc.QSize(32, 32))
        go_pixmap.fill(qtg.QColor('green'))
        stop_pixmap.fill(qtg.QColor('red'))

        #using icons
        connect_icon = qtg.QIcon()
        connect_icon.addPixmap(go_pixmap, qtg.QIcon.Active)
        connect_icon.addPixmap(stop_pixmap, qtg.QIcon.Disabled)
        self.submit.setIcon(connect_icon)
        self.submit.setDisabled(True)
        inputs['Server'].textChanged.connect(lambda x: self.submit.setDisabled(x == ''))

        inputs['Team'].setItemIcon(0, qtg.QIcon(':/teams/crimson_sharks.png'))
        inputs['Team'].setItemIcon(1, qtg.QIcon(':/teams/shadow_hawks.png'))
        inputs['Team'].setItemIcon(2, qtg.QIcon(':/teams/night_terrors.png'))
        inputs['Team'].setItemIcon(3, qtg.QIcon(':/teams/blue_crew.png'))

        libsans_id = qtg.QFontDatabase.addApplicationFont(':/fonts/LiberationSans-Regular.ttf')

        family = qtg.QFontDatabase.applicationFontFamilies(libsans_id)[0]
        libsans = qtg.QFont(family)
        inputs['Team'].setFont(libsans)





        
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())
