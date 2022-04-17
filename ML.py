from flask import Flask, render_template,redirect,url_for,request,session,flash

import os
import sys
import re
import time
import PyPDF2

app = Flask(__name__)
app.secret_key = "a"

@app.route('/')
def index():
    return render_template('greenhouse.html')


@app.route('/result',methods = ['POST', 'GET'])

# def getPageCount(pdf_file):
# 	pdfFileObj = open(pdf_file, 'rb')
# 	pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
# 	pages = pdfReader.numPages
# 	return pages

# def extractData(pdf_file, page):
# 	pdfFileObj = open(pdf_file, 'rb')
# 	pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
# 	pageObj = pdfReader.getPage(page)
# 	data = pageObj.extractText()
# 	return data

# #def getWordLength(pdf_file, wordCount):


# def getWordCount(data):
# 	data = data.split()
# 	return len(data)




def result():
   if request.method == 'POST':
      result = request.form
      # just to get the values easily
      readinglevel = request.values.get('readinglevel')
      BookRating = request.values.get('BookRating')
      BookName  = request.values.get('BookName')
      BookPDF = request.values.get('BookPDF')

      print(readinglevel) # use result ig and put the data here. 
      print(BookRating)
      print(BookName)
      print(BookPDF)

      wordLength = []
      pdfFileObj = open(BookPDF, 'rb')
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
      pages = pdfReader.numPages
      for i in range(pages):
          pdfFileObj = open(BookPDF, 'rb')
          pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
          pageObj = pdfReader.getPage(i)
          data = pageObj.extractText()
          text = data
          texts = len(text.split())
          totalwords = texts + 1
          wordLength.append(len(text))

      time.sleep(1)
      print(totalwords)
      avgWordLength = sum(wordLength) / totalwords
      print(avgWordLength)

      
      return render_template("result.html",result = avgWordLength)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')