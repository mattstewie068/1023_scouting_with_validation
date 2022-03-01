import sys

from Scouting_UI import Ui_MainWindow

from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import pandas as pd

with open("team_list.txt", "r") as tl:
    teams = tl.read().split(',')

team_list = list(map(int,teams))

class button_menu(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Button_1.clicked.connect(self.Button_1_Action)
        self.ui.Button_2.clicked.connect(self.Button_2_Action)
        self.ui.Textbox_1.setFocus()

        self.scan_count = int(self.ui.scan_count.text())

    def Button_1_Action(self):
        self.ui.Textbox_1.setText("")
        self.ui.Textbox_1.setFocus()
        self.ui.Message.setText("Status: Text Box Cleared. Enter QR Code.")

    def Button_2_Action(self):
        
        excel_file = 'raw_data.xlsx'
        df = pd.read_excel(excel_file)

        raw_data = self.ui.Textbox_1.toPlainText()

        # print(" ")
        # print(raw_data)
        # print(" ")

        try:
            headers = []
            headerless_data = []


            semicolon_split_scan = raw_data.split(";")

            for x in range(len(semicolon_split_scan)):
                item = semicolon_split_scan[x]
                item = item.split("=")
                value = item[0]
                headers.append(value)
                value = item[1]
                headerless_data.append(value)

            #print(headerless_data)
            # print(headerless_data[5])
            # print(team_list)



            if (int(headerless_data[5]) not in team_list):
                print("Invalid team # Entry! Please re-enter qr-code.")
                self.ui.Message.setText("Status: Invalid Team Number! Correct team number and re-enter QR Code.")
                return
                

        except Exception:
            print("Invalid Entry! Please re-enter qr-code.")
            self.ui.Message.setText("Status: Invalid Entry! Please re-enter QR Code.")

        else:
            try:
                data_dictionary = dict(zip(headers,headerless_data))

                df = df.append(data_dictionary, ignore_index=True)
                df.to_excel(excel_file, index=False)   

                #print("Data entry sucessful!")
                self.scan_count += 1
                self.ui.scan_count.setText(str(self.scan_count))

                self.ui.Message.setText("Status: Data entry sucessful! Enter next QR Code.")
            except:
                self.ui.Message.setText("Close Excel File and re-enter qr-code.")
        finally:
            self.ui.Textbox_1.setText("")
            self.ui.Textbox_1.setFocus()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    program = button_menu()
    program.show()

    sys.exit(app.exec())


# to build run auto-py-to-exe in terinal