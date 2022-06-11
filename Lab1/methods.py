import re

def cutText(text):
    text = re.sub(r'[\s+\t\n]+', ' ', text)
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

def cutSentences(sentences:list):
    words = []
    for s in sentences:
        words.append(re.findall(r'\w+', s))
    return words

def averageLenght(words):
    sAmount = len(words)
    wAmount = 0
    median = []
    for w in words:
            wAmount += len(w)
            median.append(len(w))
    median.sort()
    centre = len(median) % 2
    if centre == 0:
        return int((median[centre] + median[centre - 1]) / 2), int(wAmount / sAmount)
    else:
        return median[centre], int(wAmount / sAmount)

def meetWords(words):
    myDict = {}
    for s in words:
        for w in s:
            w = w.lower()
            if w in myDict:
                myDict[w] += 1
            else:
                myDict[w] = 1
    return myDict

def grams(words, n, k:int):
    allGrams = {}
    output = {}
    for s in words:
        for w in s:
            if len(w) >= n:
                w = w.lower()
                if len(w) >= n:
                    for i in range(len(w) - 1):
                        if w[i:i+n] in allGrams:
                            allGrams[w[i:i+n]] += 1
                        else:
                            allGrams[w[i:i+n]] = 1
    allGrams = dict(sorted(allGrams.items(), key=lambda item: item[1])).copy()
    i = 0
    for j, v in allGrams.items(): 
        i += 1
        if i > len(allGrams) - k:
            output[j] = v #print(j, v)
    return output