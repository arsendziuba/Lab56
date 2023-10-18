def writeConfig(file, data):
    file.seek(0)
    content = file.read()
    if "Configuration file! Do not modify!" not in content:
        file.write("Configuration file! Do not modify!\n")
    file.write(data + ";\n")

def clearConfigFile(func):
    def wrapper(*args, **kwargs):
        if not os.path.exists("config.data"):
            with open("config.data", "w") as new_file:
                new_file.write("Configuration file! Do not modify!\n")
        with open("config.data", "r+") as file:
            func(file, *args, **kwargs)
            file.truncate(0)
            file.seek(0)
    return wrapper

@clearConfigFile
def write_data_to_file(file, data):
    writeConfig(file, data)

import os

data_list = ["data1", "data2", "data3", "data4", "data5"]

for data in data_list:
    write_data_to_file(data)
