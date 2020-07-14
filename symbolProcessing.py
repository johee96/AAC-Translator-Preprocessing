from collections import defaultdict
import pprint as pp


# symbol id & symbol name
def getSymbolInfo(symbolData):
    symbolTable = defaultdict(list)

    for lab, row in symbolData.iterrows():
        key = str(row['의미1'])
        sId = str(row['symbol_id'])
        sName = str(row['상징명'])

        symbolInfo = (sId, sName)
        symbolTable[key].append(symbolInfo)
    return symbolTable


# 의미에 맞는 상징 태깅하기
def getSemanticTaggingSymbol(symbolData):
    semanticTaggingSymbol = defaultdict(set)

    for lab, row in symbolData.iterrows():
        mean1 = str(row['의미1'])
        for i in row[2:]:
            value = str(i)
            if value == 'nan':
                break
            semanticTaggingSymbol[value].add(mean1)

    pp.pprint(semanticTaggingSymbol)
    return semanticTaggingSymbol


"""
# test
symbolData = fileProcessing.readFile('testData/testSymbolData.xlsx', False, False)
symbolInfo = getSymbolInfo(symbolData)
semanticTaggingSymbol = getSemanticTaggingSymbol(symbolData)

pp.pprint(symbolInfo)
pp.pprint(semanticTaggingSymbol)
"""
