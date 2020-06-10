import posTagging,fileProcessing
import pandas as pd
import konlpy

symbolDatas = pd.read_excel('./symbolData/all.xlsx', encoding="utf-8")
symbolDatas = symbolDatas.applymap(str)
count = 0   #상징에서 복합용언 몇 개 인지
maxCount=0    #복합용언 중 제일 긴 값의 길이
maxWord = ''  #
maxWordTagging = '' # 복합용언을 가진 상징 중, 가장 긴 값의 상징 정보
komoran = konlpy.tag.Komoran(max_heap_size= 1024 * 6) # 반드시 전역 변수에서 한번만 실행하자
print('Symbol Size: ', len(symbolDatas))
for sentence in symbolDatas.values.tolist():
    words = komoran.pos(sentence[0])
    tmpCount=0
    tmpvalue=''

    for word in words:
        print(word)
        if word[1] == 'VA' or word[1] == 'VV' or word[1] == 'VX' or word[1] == 'NNG' or word[1] == 'NNP' or word[1] == 'NNB' or word[1] == 'NR' or word[1] == 'NP' :
            tmpCount=tmpCount+1
            tmpvalue = tmpvalue + word[0]
            tmpInfo=words


    if tmpCount>1:
        if maxCount<tmpCount:
            maxCount=tmpCount
            maxWord = tmpvalue
            maxWordTagging=tmpInfo
        count = count+1
print('count: ', count)
print('maxCount: ',maxCount)
print('maxWord: ', maxWord)
print('info: ', maxWordTagging)

"""
symbolWords=set()
dbWords=list()

symbolDatas = pd.read_excel('./symbolData/all.xlsx', encoding="utf-8")
symbolDatas = symbolDatas.applymap(str)

dbDatas = pd.read_excel('./data/all.xlsx',encoding="utf-8")
dbDatas = dbDatas.applymap(str)

symbolDatas_list = symbolDatas.values.tolist()
dbDatas_list = dbDatas.values.tolist()
komoran = konlpy.tag.Komoran(max_heap_size= 1024 * 6) # 반드시 전역 변수에서 한번만 실행하자

for sentence in symbolDatas_list:
    words = komoran.pos(sentence[0])
    if words[0][1] == 'VA' or words[0][1] == 'VV' or words[0][1] == 'VX':
        symbolWords.add(words[0][0]+ '다') #symbol에 있는 복합 명사의 명사들이 상징에 있따고 가정
    elif words[0][1] == 'NNG' or words[0][1] == 'NNP' or words[0][1] == 'NNB' or words[0][1] == 'NR' or words[0][1] == 'NP' :
        symbolWords.add(words[0][0])

for sentence in dbDatas_list:
    words = komoran.pos(sentence[0])
    if words[0][1] == 'VA' or words[0][1] == 'VV' or words[0][1] == 'VX':
        dbWords.append(words[0][0] + '다')  # symbol에 있는 복합 명사의 명사들이 상징에 있따고 가정
    elif words[0][1] == 'NNG' or words[0][1] == 'NNP' or words[0][1] == 'NNB' or words[0][1] == 'NR' or words[0][
        1] == 'NP':
        dbWords.append(words[0][0])

print(dbWords)
print(symbolWords)
dbWordSize = len(dbWords)
symbolWordSize = len(symbolWords)

setDb=set(dbWords)
diff = len(symbolWords.difference(setDb))
print('dbWordSize: ', dbWordSize)
print('symbolWordSize: ',symbolWordSize)

print('diff: ',diff)
print('result : ',(symbolWordSize-diff)/dbWordSize)
"""