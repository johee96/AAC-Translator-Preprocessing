import posTagging, fileProcessing
import pandas as pd

# merge files
# symbolDatas = fileProcessing.mergeFiles('symbolData','symbol')
# dlgDatas = fileProcessing.mergeFiles('data','')

symbolData = fileProcessing.readFile('symbolData/all.xlsx')
dlgData = fileProcessing.readFile('data/all.xlsx')
# posTagging.symbolProcessing(symbolDatas)
taggingData, rateData = posTagging.symbolMatching(symbolData, dlgData)
fileProcessing.saveFile(dlgData, taggingData, rateData)
"""

1. 품사 태깅달고 해보기
2. 품사 태깅 안 달고 단어로만 해보기
3. 상징에 사용된 품사를 바탕으로 사용할 품사 정하기 
4. nnp,nng -> n으로 묶어서 시도하기

전처리
1. !? 이런 것을 때고 해야하나??
2. 숫자,영어 혼용 된 것 처리
    - 숫자를 다 한글로 바꿀까?   
    - 상징에서 어떤 부분이 숫자인지 파악하기 
"""
