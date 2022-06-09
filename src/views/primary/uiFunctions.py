from PySide6.QtCore import QPropertyAnimation
from src.views.primary.WndMain import Ui_WndMain


class UIFunctions(Ui_WndMain):

    def toggleMenu(self, maxWidth, enable):
        if enable:

            # Get Width
            width = self.ui.leftMenu.width()
            maxExtend = maxWidth
            standard = 60

            # Set Width
            if width == 60:
                widthExtended = maxExtend

            else:
                widthExtended = standard

            # set new postioning for the icons


            # Animation
            self.animation = QPropertyAnimation(self.ui.leftMenu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()
