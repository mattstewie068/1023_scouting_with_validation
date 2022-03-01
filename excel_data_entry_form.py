import PySimpleGUI as sg
import pandas as pd


sg.theme('DarkTeal9')

excel_file = 'scouting_data.xlsx'
df = pd.read_excel(excel_file)

layout = [
    [sg.Text('input QR code below')],
    [sg.InputText()],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('data entry form',layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Clear':
        clear_input()

    if event == 'Submit':

        # raw_data = values

        # print(" ")
        # print(raw_data)
        # print(" ")

        # headers = []
        # headerless_data = []

        # semicolon_split_scan = raw_data.split(";")

        # print(semicolon_split_scan)
        # print(" ")    

        # for x in range(len(semicolon_split_scan)):
        #     item = semicolon_split_scan[x]
        #     item = item.split("=")
        #     value = item[0]
        #     headers.append(value)
        #     value = item[1]
        #     headerless_data.append(value)

        # print(headers)
        # print(" ")
        # print(headerless_data)
        # print(" ")

        # data_dictionary = dict(zip(headers,headerless_data))

        # print(data_dictionary)


        df = df.append(values, ignore_index=True)
        df.to_excel(excel_file, index=False)
        sg.popup('Data saved!')
        clear_input()
window.close()