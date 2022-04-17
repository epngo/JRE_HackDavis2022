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
      print(result) # use result ig and put the data here. 
      return render_template("result.html",result = result)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')