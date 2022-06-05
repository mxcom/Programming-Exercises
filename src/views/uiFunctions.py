from PySide6.QtCore import QPropertyAnimation
from ui.WndMain import Ui_MainWindow


class UIFunctions(Ui_MainWindow):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # Get Width
            width = self.leftMenu.width()
            maxExtend = maxWidth
            standard = 70

            # Set Width
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # Animation
            self.animation = QPropertyAnimation(self.leftMenu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()
