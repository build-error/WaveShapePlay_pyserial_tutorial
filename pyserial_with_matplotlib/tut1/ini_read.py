dataFile_ini = open('dataSetup.ini', 'r')
ini_data_result = {}

def getINI():
    iniHeader = dataFile_ini.readline().split(':')
    print(iniHeader[0] + ' ' + iniHeader[1].rstrip())
    iniReadLines = int(iniHeader[1].rstrip())

    for i in range(0, iniReadLines):
        variable = dataFile_ini.readline().split(':')
        print(variable)
        ini_data_result[variable[0]] = variable[1].rstrip()

    return ini_data_result

if __name__ == '__main__':
    getINI()