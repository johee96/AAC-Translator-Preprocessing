import konlpy
import nltk
import pandas as pd

posList = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'VV', 'VA', 'VX', 'SL', 'SN', 'MM', 'MAG', 'XR', 'MAJ', 'MM']


def symbolProcessing(symbolDatas):
    komoran = konlpy.tag.Komoran(max_heap_size=1024 * 6)  # 반드시 전역 변수에서 한번만 실행하자
    nameList = []
    taggingList = []
    for sentence in symbolDatas.values:
        words = komoran.pos(sentence[0])
        # print(words)
        nameList.append(sentence)
        tmpList = list()
        for word in words:
            if word[1] in posList:
                tmpList.append(word)
        taggingList.append(tmpList)
        # print(tmpList)
    taggingData = pd.DataFrame(zip(nameList, pd.Series(taggingList)), columns=['name', 'tagging'])
    return taggingData


def symbolMatching(symbolDatas, dlgDatas):
    saveData = list()
    rateData = list()
    komoran = konlpy.tag.Komoran(max_heap_size=1024 * 6)  # 반드시 전역 변수에서 한번만 실행하자
    symbolPre = symbolProcessing(symbolDatas)
    symbolTaggingData = symbolPre['tagging'].tolist()
    symbolNameData = symbolPre['name'].tolist()

    for sentence in dlgDatas.values:
        sentDataList = list()  # 문장에 해당하는 list

        tmp = komoran.pos(sentence[0])
        words = list()
        for word in tmp:
            if word[1] in posList:
                words.append(word)
        # print(tmp)
        # print(words)

        low = 0;
        high = len(words) + 1
        cnt = 0
        while low < len(words):
            if words[low:high] in symbolTaggingData:
                # sentDataList = sentDataList + words[low:high]
                idx = symbolTaggingData.index(words[low:high])
                # print(low, ' ', high, " ", idx, " ", symbolNameData[idx][0])
                sentDataList.append(symbolNameData[idx][0])
                cnt += 1
                low = high
                high = len(words) + 1
            else:
                if low == high - 1:
                    low = high
                    high = len(words) + 1
                else:
                    high -= 1
        # print(tmpList)
        # print(sentDataList)
        rate = 0
        if cnt > 0:
            rate = cnt / len(words)
        rateData.append(rate)
        saveData.append(sentDataList)

    return saveData, rateData

    """
    for word in words:
        if [word] in symbolTaggingData['tagging'].tolist():
            idx = symbolTaggingData['tagging'].tolist().index([word])
            saveList.append(symbolTaggingData['name'][idx][0])
    """
