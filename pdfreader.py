import os
import sys
import re
import time
import PyPDF2

def getPageCount(pdf_file):
	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
	pages = pdfReader.numPages
	return pages

def extractData(pdf_file, page):
	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
	pageObj = pdfReader.getPage(page)
	data = pageObj.extractText()
	return data

#def getWordLength(pdf_file, wordCount):


def getWordCount(data):
	data = data.split()
	return len(data)

def main():
	if len(sys.argv)!=2:
		print('Missing arguments, command usage: python pdfreader.py <FileName>')
		exit(1)
	else:
		pdfFile = sys.argv[1]
	
		# check if the specified file exists or not
		try:
			if os.path.exists(pdfFile):
				print("File Found!")
		except OSError as err:
			print(err.reason)
			exit(1)

		wordLength = []
		# get the word count in the pdf file
		totalWords = 0
		numPages = getPageCount(pdfFile)
		for i in range(numPages):
			text = extractData(pdfFile, i)
			totalWords += getWordCount(text)
			wordLength.append(len(text))
		time.sleep(1)
		print(totalWords)
		avgWordLength = sum(wordLength) / totalWords
		print(avgWordLength)

if __name__ == '__main__':
	main()