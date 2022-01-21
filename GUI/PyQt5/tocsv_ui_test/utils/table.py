from PyQt5 import QtCore

import pandas as pd

 # A class to convert pandas dataframe into table model to be displayed
class PandasModel(QtCore.QAbstractTableModel):
    ##### NOTICE #####
    # As per documentation, it was recommended to return an invalid QVariant
    # if there's no value to return, this will apllied to all methods defined here

    # Assign user role
    DtypeRole = QtCore.Qt.ItemDataRole.UserRole + 1000
    ValueRole = QtCore.Qt.ItemDataRole.UserRole + 1001

    def __init__(self, df=pd.DataFrame(), parent=None):
        super(PandasModel, self).__init__(parent)
        self.df = df
    
    # Set the dataframe by resetting previous one
    def set_dataframe(self, dataframe):
        self.beginResetModel()
        self.df = dataframe.copy()
        self.endResetModel()
    
    # Call the dataframe
    def dataframe(self):
        return self.df
    
    # Call dataframe method above and assign a qt property into it
    dataframe = QtCore.pyqtProperty(pd.DataFrame, fget=dataframe, fset=set_dataframe)

    # overwrite headerData method and use slot decorator on it
    # it is necessary to convert python method into a Qt slot
    # so that the signal could recognize the method
    @QtCore.pyqtSlot(int, QtCore.Qt.Orientation, result=str)
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return self.df.columns[section]
            else:
                return self.df.index[section]
        return QtCore.QVariant()

    # overwrite rowCount method
    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self.df.index)
    
    # overwrite columnCount method
    def columnCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return self.df.columns.size
    
    # overwrite data method
    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if (
            not index.isValid() 
            or (not 0 <= index.row() < self.rowCount())
            and (0 <= index.column() < self.columnCount())
        ):
            return QtCore.QVariant()
        
        row = self.df.index[index.row()]
        col = self.df.columns[index.column()]
        dtype = self.df[col].dtype
        val = self.df.iloc[row][col]

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            return str(val)
        elif role == PandasModel.ValueRole:
            return val
        
        if role == PandasModel.DtypeRole:
            return dtype

        return QtCore.QVariant()
    
    # overwrite roleNames method
    def roleNames(self):
        roles = {
            QtCore.Qt.ItemDataRole.DisplayRole: b'display',
            PandasModel.DtypeRole: b'dtype',
            PandasModel.ValueRole: b'value',
        }
        return roles