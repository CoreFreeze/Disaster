from PySide2.QtCore import QObject, Signal

class setMessageSig(QObject):
    DBmessageSig = Signal(int, list)
    socketStateSig = Signal(str)