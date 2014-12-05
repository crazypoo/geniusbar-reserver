from PyQt4.QtGui import QValidator


class EmptyValidator(QValidator):
    def __init__(self, parent=None):
        super(EmptyValidator, self).__init__(parent)

    def validate(self, text, index):
        print(text)
