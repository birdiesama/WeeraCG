import hou

from PySide2.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import Qt

class PythonTools(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Python Tools')
        self.resize(250, 100)
        
        button_print = QPushButton("Print Awesome")
        button_print.clicked.connect(self.print_awesome)
        
        button_gnt = QPushButton("Get Node Type")
        button_gnt.clicked.connect(self.get_node_type)
        
        layout = QVBoxLayout()
        layout.addWidget(button_print)
        layout.addWidget(button_gnt)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
    
    def print_awesome(self):
        print("We are Awesome!")

    def get_node_type(self):
    
        sel = hou.selectedNodes()
        
        if sel:
            for each in sel:
                print(each.type().name())
        else:
            print('Nothing is beling selected')
        
window = PythonTools()
window.setParent(hou.qt.mainWindow(),Qt.WindowStaysOnTopHint | Qt.Dialog)
window.show()   
