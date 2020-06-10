import pandas as pd
import os


def saveFile(dlgData, taggingData, rateData):
    dlgData['tagging'] =taggingData
    dlgData['rate'] = rateData
    print("save..")
    dlgData.to_excel("./result/taggingData.xlsx", header=True, index=False)



def readFile(filePath):
    data = pd.read_excel(filePath)
    data = data.applymap(str)  # 숫자값 때문에 사용
    data.iloc[:, 0] = data.iloc[:, 0].str.replace(pat=r'[^A-Za-z0-9가-힝]', repl=r' ',
                                                  regex=True)  # 뒤에 ?!에 따라서 품사가 다름
    return data


def mergeFiles(folder, type):
    allData = pd.DataFrame()
    path = "./" + folder + "/"
    fileList = os.listdir(path)

    if type is 'symbol':
        for fileNameRaw in fileList:
            if '.xlsx' not in fileNameRaw:
                continue
            fileName = path + fileNameRaw
            file = pd.read_excel(fileName, sheet_name=None, header=None, skiprows=1, usecols="B", encoding="utf-8")
            mergeDf = pd.concat(file, ignore_index=True)
            allData = allData.append(mergeDf, ignore_index=True)

        allData.columns = ['상징명']
        allData['상징명'] = allData['상징명'].str.split('[').str[0]
        allData['상징명'] = allData['상징명'].str.replace(pat=r'[^A-Za-z0-9가-힝]', repl=r'',
                                                    regex=True)  # replace all special symbols to space
    else:
        for fileNameRaw in fileList:
            if '.xlsx' not in fileNameRaw:
                continue
            fileName = path + fileNameRaw
            file = pd.read_excel(fileName, usecols='B')
            allData = allData.append(file, ignore_index=True)

    allData = allData.applymap(str)  # 숫자값 때문에 사용
    allData = allData.drop_duplicates()
    allData.to_excel("./" + folder + "/all.xlsx", header=True, index=False)

    print(allData.head())
    print(allData.shape)
    return allData
