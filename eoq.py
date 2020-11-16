from eoq_gui import *
from sympy import *
import math

def signals(self):
    self.buttonCalc.clicked.connect(self.calc)  # Connect buttonCalc clicked signal to the calc function

def calc(self):  # Do the calculation
    d = float(self.lineEdit_d.text())
    h = float(self.lineEdit_h.text())
    k = float(self.lineEdit_k.text())
    l = float(self.lineEdit_l.text())
    c1 = float(self.lineEdit_c1.text())
    c2 = float(self.lineEdit_c2.text())
    q = float(self.lineEdit_q.text())
    x=Symbol('x')
    
    ym=math.sqrt((2*k*d)/h)
    
    if q <= ym:
        eoq=ym
    else:
        tcu1=(c1*d)+((k*d)/ym)+((h*ym)/2)
        temp=solve(x**2+(((2*((c2*d)-tcu1))/h)*x)+((2*k*d)/h),x)
        Q=temp[1]
        if q > Q:
            eoq=ym
        else:
            eoq=q
            
    t0=eoq/d
    if l <= t0:
        rop=l*d
    else:
        n=math.floor(l/t0)
        le=l-(n*t0)
        rop=le*d
    
    self.lineEdit_eoq.setText(str(eoq))
    self.lineEdit_rop.setText(str(rop))
    

Ui_MainWindow.signals = signals  # Add new attributes to Ui_MainWindow
Ui_MainWindow.calc = calc #Functions 

if __name__ == "__main__":  # A library or a stand-alone program
    import sys
    app = QtWidgets.QApplication(sys.argv)  # Must create a QApplication object
                                            # sys.argv allows passing parameters in command line
    MainWindow = QtWidgets.QMainWindow()  # Create a main window instance.
    ui = Ui_MainWindow()  # Create a Ui_MainWindow instance
    ui.setupUi(MainWindow)  # Add widgets to the main window
    ui.signals()  # Connect signals with the appropriate functions
    MainWindow.show()  # Show the main window
    sys.exit(app.exec_())  # If a termination signal is captured, exit the program.
