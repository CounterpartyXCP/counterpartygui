from PyQt5.QtCore import QCoreApplication

APP_NAME = 'counterparty-gui'
APP_VERSION = '1.0.0'

def tr(string):
    return QCoreApplication.translate("@default", string)

