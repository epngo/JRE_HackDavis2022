from flask import Flask, render_template,redirect,url_for,request,session,flash


app = Flask(__name__)
app.secret_key = "a"

@app.route('/')
def index():
    return render_template('greenhouse.html')


@app.route('/result',methods = ['POST', 'GET'])
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


      
      return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')