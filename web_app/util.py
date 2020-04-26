import re

punctuationRe = re.compile(r'[\/.,\[\];{}|:"<>\?!]')
symbolsRe = re.compile(r'[0-9@#$&%\n\*()!\+-]')
URLRe = re.compile(r'https?:\/\/\S+')

def makeString(text):
    return str(text)

def removePunctuation(text):
    text = punctuationRe.sub(' ', text)
    return text

def removeSymbols(text):
    text = symbolsRe.sub(' ', text)
    return text

def removeURLs(text):
    text = URLRe.sub('', text)
    return text
