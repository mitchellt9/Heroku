__author__ = 'Mitchell'
from flask import Flask, request,render_template
import os
from addition_logic import *         #IMPORTED FILE CONTAINING THE PYTHON FUNCTION

app = Flask(__name__)

@app.route('/')                        #DEFAULT PATH
def render_addition():                 #SHOULD HAVE 1 FUNCTION ATLEAST TO RENDER A HTML PAGE
    return render_template("add.html")

"""PYTHON FUNCTION TO BE RUN"""
@app.route('/result', methods=['POST']) #use POST here since some data is being sent there
def render_result():
    a=int(request.form["value1"]) #Value of the first text box is sent here
    b=int(request.form["value2"]) #Value of the second text box is sent here
    result=sum(a,b)               #This is the argument passed and returned to the python based logic file
    return render_template('result.html', value="Adding"+str(a)+" and "+str(b)+ " is "+str(result))            #This return is automatically handled by Flask and redirected to a new page

# def render_result():
#     a=int(request.form["value1"]) #Value of the first text box is sent here
#     b=int(request.form["value2"]) #Value of the second text box is sent here
#     result=multiply(a,b)               #This is the argument passed and returned to the python based logic file
#     return render_template('result.html', value="Multiplying "+str(a)+" and "+str(b)+ " is "+str(result))            #This return is automatically handled by Flask and redirected to a new page


"""Error Handling """
@app.errorhandler(404)            #This is a Flask inbuild function which handles error 500
def page_not_found(e):
    return render_template('somethingwentwrongpage.html') #redirected to a page I setup for error handling

@app.errorhandler(400)            #This is a Flask inbuild function which handles error 500
def page_not_found(e):
    return "name mismatch" #redirected to a page I setup for error handling


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

