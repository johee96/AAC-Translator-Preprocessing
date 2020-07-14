import pandas as pd
import os
import datetime


def saveFile(dlgData, sentTaggingData, taggingData, rateData):
    dlgData['sent Pos'] = sentTaggingData
    dlgData['symbol Tagging1'] = taggingData
    dlgData['symbol Tagging2'] = taggingData
    dlgData['rate'] = rateData
    now = datetime.datetime.now()
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

    dlgData.to_excel("./result/taggingData_" + nowDatetime + ".xlsx", header=True, index=False)
    print("save..")


def readFile(filePath, dropna=True, option=True):
    data = pd.read_excel(filePath, encoding="utf-8", dtype=str)
    if option:
        data.iloc[:, 0] = data.iloc[:, 0].str.replace(pat=r'[^A-Za-z0-9가-힝]', repl=r' ',
                                                      regex=True)  # 뒤에 ?!에 따라서 품사가 다름
        data.iloc[:, 0] = data.iloc[:, 0].str.strip()  # 앞 뒤 공백 제거
    #  data = data.drop_duplicates()                               # 중복제거
    if dropna:
        data = data.dropna(axis=0)  # 비어있는 행 제거
    data = data.reset_index(drop=True)  # reset index
    print(data.head())
    print(data.shape)
    return data


def mergeFiles(folder, type):
    allData = pd.DataFrame()
    path = "./" + folder + "/"
    fileList = os.listdir(path)

    for fileNameRaw in fileList:
        if '.xlsx' not in fileNameRaw:
            continue
        fileName = path + fileNameRaw
        if type is 'symbol':
            file = pd.read_excel(fileName, sheet_name=None, header=None, skiprows=1, usecols="B", encoding="utf-8",
                                 dtype=str)
        else:
            file = pd.read_excel(fileName, sheet_name=None, usecols='B', encoding="utf-8", dtype=str)
        mergeDf = pd.concat(file, ignore_index=True)
        allData = allData.append(mergeDf, ignore_index=True)
        print("#", allData.shape)

    if type is 'symbol':  # symbol file에는 col name이 없기 떼문에 따로 처리
        allData.columns = ['상징명']
        allData['상징명'] = allData['상징명'].str.split('[').str[0]
    print(allData.shape)

    allData = allData.applymap(str)  # 숫자값 때문에 사용
    allData.iloc[:, 0] = allData.iloc[:, 0].str.strip()  # 앞 뒤 공백 제거
    # allData.apply(lambda x: x.str.strip(), axis=1)     # 앞 뒤 공백 제거

    #  allData = allData.drop_duplicates()                  # 중복제거
    allData = allData.dropna(axis=0)  # 비어있는 행 제거
    allData = allData.reset_index(drop=True)

    allData.to_excel("./" + folder + "/all.xlsx", header=True, index=False)
    print(allData.shape)
    print(allData.head())

    return allData
