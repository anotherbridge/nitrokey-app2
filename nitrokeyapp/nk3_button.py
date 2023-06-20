from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QSize

from nitrokeyapp.device_data import DeviceData
from PyQt5 import QtWidgets
from qt_material import apply_stylesheet


class Nk3Button(QtWidgets.QPushButton):
    def __init__(
        self,
        data: DeviceData,
    ) -> None:
        super().__init__(
            QtGui.QIcon(":/images/icon/usb_new.png"),
            "Nitrokey 3: " f"{str(data.uuid)[:5]}",
        )
        self.data = data
        # needs to create button in the vertical navigation with the nitrokey type and serial number as text
        apply_stylesheet(self, theme='light_red.xml')
        
