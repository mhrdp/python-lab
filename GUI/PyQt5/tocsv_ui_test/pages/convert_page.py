from PyQt5 import QtWidgets
from ui.convert_ui import Ui_MainWindow
from utils.table import PandasModel

import pandas as pd
import threads.convert_threads as threads

class ConvertData(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ConvertData, self).__init__()

        # Import everything inside Ui_MainWindow.setupUi
        self.setupUi(self)

        self.setWindowTitle('FUND Capital Inc.')

        # Because signal wants a function as a argument, you can add lambda
        # to make a nested function and counter a TypeError exception
        # because self.get_path() alone return a result, so it's already not a function
        # or alternatively, you can exclude the '()' from the functions
        self.btn_browse.clicked.connect(lambda: self.browse_file())

        self.btn_all.clicked.connect(lambda: self.convert_all_thread())
        self.btn_gen_inf.clicked.connect(lambda: self.gen_inf_thread())
        self.btn_b_sheet.clicked.connect(lambda: self.financial_pos_thread())
        self.btn_pro_loss.clicked.connect(lambda: self.profit_or_loss_thread())
        self.btn_cashflow.clicked.connect(lambda: self.cashflow_thread())
        self.btn_table.clicked.connect(lambda: self.generate_table())

        # Close button
        self.btn_exit.clicked.connect(lambda: self.close_window())

    def generate_table(self):
        path = self.path_dir.text()
        df = pd.read_csv(path)
        
        # If you want to filter the dataframe
        # model = PandasModel(df[['entity_code']])

        model = PandasModel(df)
        self.table_pd.setModel(model)
    
    def convert_all_thread(self):
        self._convert_all_thread = threads.ConvertAllThread(self.path_dir.text().split(', '))
        self.process_start()

        # Start the thread
        self._convert_all_thread.start()

        # This will catch the signal emitted from ConvertAllThread.run()
        # as a mean to determine whether the methods done executing
        self._convert_all_thread._signal.connect(self.process_finish)
        
    def gen_inf_thread(self):
        self._gen_inf_thread = threads.GeneralInfThread(self.path_dir.text().split(', '))
        self.process_start()       
        
        # Start the thread
        self._gen_inf_thread.start()

        # This will catch the signal emitted from GeneralInfThread.run()
        # as a mean to determine whether the methods done executing
        self._gen_inf_thread._signal.connect(self.process_finish)
    
    def financial_pos_thread(self):
        self._financial_pos_thread = threads.FinancialPosThread(self.path_dir.text().split(', '))
        self.process_start()

        # Start the thread
        self._financial_pos_thread.start()

        # This will catch the signal emitted from FinancialPos.run()
        # as a mean to determine whether the methods done executing
        self._financial_pos_thread._signal.connect(self.process_finish)
    
    def profit_or_loss_thread(self):
        self._profit_or_loss_thread = threads.ProfitLossThread(self.path_dir.text().split(', '))
        self.process_start()
        
        # Start the thread
        self._profit_or_loss_thread.start()

        # This will catch the signal emitted from ProfitLossThread.run()
        # as a mean to determine whether the methods done executing
        self._profit_or_loss_thread._signal.connect(self.process_finish)
    
    def cashflow_thread(self):
        self._cashflow_thread = threads.CashflowThread(self.path_dir.text().split(', '))
        self.process_start()

        # Start the thread
        self._cashflow_thread.start()

        # This will catch the signal emitted from CashflowThread.run()
        # as a mean to determine whether the methods done executing
        self._cashflow_thread._signal.connect(self.process_finish)


    def process_start(self):
        self.progress_bar.setRange(0, 0)
        self.btn_disabled()

    def process_finish(self):
        self.progress_bar.setRange(0, 100)
        self.btn_enabled()

    
    def btn_disabled(self):
        self.label_info.setText('Processing...')
        self.btn_all.setEnabled(False)
        self.btn_cashflow.setEnabled(False)
        self.btn_b_sheet.setEnabled(False)
        self.btn_exit.setEnabled(False)
        self.btn_gen_inf.setEnabled(False)
        self.btn_pro_loss.setEnabled(False)
        self.btn_table.setEnabled(False)
    
    def btn_enabled(self):
        self.label_info.setText('Finished!')
        self.btn_all.setEnabled(True)
        self.btn_b_sheet.setEnabled(True)
        self.btn_cashflow.setEnabled(True)
        self.btn_exit.setEnabled(True)
        self.btn_gen_inf.setEnabled(True)
        self.btn_pro_loss.setEnabled(True)
        self.btn_table.setEnabled(True)
    

    def browse_file(self):
        path = ', '
        filename = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open File', '', 'All Files (*);;Excel Files (*.xlsx *.xls)')

        if filename:
            self.path_dir.setText(path.join(filename[0]))
    
    def close_window(self):
        window_dialog = QtWidgets.QMessageBox.question(
            self, 'Notice!',
            'Are your sure want to quit?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        
        if window_dialog == QtWidgets.QMessageBox.Yes:
            import sys

            app = QtWidgets.QApplication(sys.argv)
            app.quit()
        else:
            pass