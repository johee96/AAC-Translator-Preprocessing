import konlpy
import nltk
import pandas as pd

posList = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'VV', 'VA', 'VX', 'SL', 'SN', 'MM', 'MAG', 'XR', 'MAJ', 'XSN', 'XSV',
           'XSA', 'VCN', 'NA', 'NV', 'NF']


def symbolPosTagging(symbolData):
    komoran = konlpy.tag.Komoran(max_heap_size=1024 * 6)  # 반드시 전역 변수에서 한번만 실행하자
    semanticList = []
    symbolNameList = []
    taggingList = []
    for symbolSemantic in symbolData.keys():
        semanticList.append(symbolSemantic)
        symbolNameList.append(symbolData[symbolSemantic])
        words = komoran.pos(symbolSemantic)
        tmpList = list()
        for word in words:
            if word[1] in posList:
                if word[1] in ['NNG', 'NNP', 'NNB']:  # 명사를 n으로 묶음
                    word = word[:1] + ('N',)
                tmpList.append(word)
        taggingList.append(tmpList)
    taggingData = pd.DataFrame(zip(semanticList, pd.Series(taggingList), symbolNameList),
                               columns=['semantic', 'tagging', 'symbolName'])
    return taggingData


def symbolMatching(symbolData, dlgData):
    sentPosData = list()
    sentSymbolTaggingData = list()
    rateData = list()

    komoran = konlpy.tag.Komoran(max_heap_size=1024 * 6)  # 반드시 전역 변수에서 한번만 실행하자
    symbolPosTaggingData = symbolPosTagging(symbolData)
    symbolSemantic = symbolPosTaggingData['semantic'].tolist()
    symbolTaggingData = symbolPosTaggingData['tagging'].tolist()
    symbolNameData = symbolPosTaggingData['symbolName'].tolist()

    for sentence in dlgData['sentence'].values:
        sentDataList = list()  # 문장에 해당하는 list
        # print(sentence)
        tmp = komoran.pos(sentence)
        sentPosData.append(tmp)
        words = list()
        for word in tmp:
            if word[1] in posList:
                if word[1] in ['NNG', 'NNP', 'NNB']:  # 명사를 n으로 묶음
                    word = word[:1] + ('N',)
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
                sentDataList.append(symbolNameData[idx])
                cnt += 1
                low = high
                high = len(words) + 1
            else:
                if low == high - 1:
                    low = high
                    high = len(words) + 1
                else:
                    high -= 1
        #   print(sentDataList)
        rate = 0
        if cnt > 0:
            rate = cnt / len(words)
        rateData.append(rate)
        sentSymbolTaggingData.append(sentDataList)

    return sentPosData, sentSymbolTaggingData, rateData


"""
import konlpy
import nltk
import pandas as pd

posList = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'VV', 'VA', 'VX', 'SL', 'SN', 'MM', 'MAG', 'XR', 'MAJ', 'XSN', 'XSV',
           'XSA', 'VCN', 'NA', 'NV', 'NF']


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
                if word[1] in ['NNG','NNP','NNB']:          # 명사를 n으로 묶음
                    word = word[:1] + ('N',)
                tmpList.append(word)
        taggingList.append(tmpList)
       # print(tmpList)
    taggingData = pd.DataFrame(zip(nameList, pd.Series(taggingList)), columns=['name', 'tagging'])
    return taggingData


def symbolMatching(symbolData, dlgData):
    sentPosData = list()
    sentSymbolTaggingData = list()
    rateData = list()

    komoran = konlpy.tag.Komoran(max_heap_size=1024 * 6)  # 반드시 전역 변수에서 한번만 실행하자
    symbolPre = symbolProcessing(symbolData)
    symbolTaggingData = symbolPre['tagging'].tolist()
    symbolNameData = symbolPre['name'].tolist()

    for sentence in dlgData['sentence'].values:
        sentDataList = list()  # 문장에 해당하는 list
        #print(sentence)
        tmp = komoran.pos(sentence)
        sentPosData.append(tmp)
        words = list()
        for word in tmp:
            if word[1] in posList:
                if word[1] in ['NNG', 'NNP', 'NNB']:  # 명사를 n으로 묶음
                    word = word[:1] + ('N',)
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
     #   print(sentDataList)
        rate = 0
        if cnt > 0:
            rate = cnt / len(words)
        rateData.append(rate)
        sentSymbolTaggingData.append(sentDataList)

    return sentPosData, sentSymbolTaggingData, rateData



"""
