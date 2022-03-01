import os


filename = "Scouting_UI" #type name of ui file

ui_file = filename + ".ui"
#print(ui_file)

new_py_file_name = filename + ".py"
#print(new_py_file_name)

command_string = "pyuic6 -o " + new_py_file_name + " " + ui_file
#print(command_string)

def convert_ui_to_py():
    os.system(command_string)



convert_ui_to_py()