from utils.convert import ExtractData
from PyQt5.QtCore import QThread, pyqtSignal

class ConvertAllThread(QThread):
    # if you have no argument to pass when emitting the signal, leave this blank
    # otherwhise fill it in with the type of data your signal want to emit
    _signal = pyqtSignal()

    def __init__(self, file):
        super(ConvertAllThread, self).__init__()
        self.file = file # format must be a List type
    
    def __del__(self):
        self.wait()
    
    # run() method is where you put your function inside the QThread
    # the signal will emitted when the function done executing
    def run(self):
        for i in self.file:
            ExtractData(i).convert_all()
        self._signal.emit()

class GeneralInfThread(QThread):
    # if you have no argument to pass when emitting the signal, leave this blank
    # otherwhise fill it in with the type of data your signal want to emit
    _signal = pyqtSignal()

    def __init__(self, file):
        super(GeneralInfThread, self).__init__()
        self.file = file # format must be a List type
    
    def __del__(self):
        self.wait()
    
    # run() method is where you put your function inside the QThread
    # the signal will emitted when the function done executing
    def run(self):
        for i in self.data:
            ExtractData(i).general_inf()
        self._signal.emit()

class FinancialPosThread(QThread):
    # if you have no argument to pass when emitting the signal, leave this blank
    # otherwhise fill it in with the type of data your signal want to emit
    _signal = pyqtSignal()

    def __init__(self, file):
        super(FinancialPosThread, self).__init__()
        self.file = file # format must be a List type
    
    def __del__(self):
        self.wait()
    
    # run() method is where you put your function inside the QThread
    # the signal will emitted when the function done executing
    def run(self):
        for i in self.file:
            ExtractData(i).financial_pos()
        self._signal.emit()

class ProfitLossThread(QThread):
    # if you have no argument to pass when emitting the signal, leave this blank
    # otherwhise fill it in with the type of data your signal want to emit
    _signal = pyqtSignal()

    def __init__(self, file):
        super(ProfitLossThread, self).__init__()
        self.file = file # format must be a List type
    
    def __del__(self):
        self.wait()
    
    # run() method is where you put your function inside the QThread
    # the signal will emitted when the function done executing
    def run(self):
        for i in self.file:
            ExtractData(i).profit_or_loss()
        self._signal.emit()

class CashflowThread(QThread):
    # if you have no argument to pass when emitting the signal, leave this blank
    # otherwhise fill it in with the type of data your signal want to emit
    _signal = pyqtSignal()

    def __init__(self, file):
        super(CashflowThread, self).__init__()
        self.file = file # format must be a List type
    
    def __del__(self):
        self.wait()
    
    # run() method is where you put your function inside the QThread
    # the signal will emitted when the function done executing
    def run(self):
        for i in self.file:
            ExtractData(i).cashflow()
        self._signal.emit()