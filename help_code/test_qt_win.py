from PyQt5.QtCore import Qt
window = objreg.get('main-window', scope='window', window=0)
window.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
window.hide()
window.show()