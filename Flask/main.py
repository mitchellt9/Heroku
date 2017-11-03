__author__ = 'Mitchell'

from flask import Flask, abort, request,jsonify,render_template
import json
import time
import os

app = Flask(__name__)
# data1={'name':'ankit','class':'mca'}

@app.route('/')
def my_form():
    return render_template("hi.html")

#
# @app.route('/test/1')
# def testing():
#     return jsonify(data1)


@app.route('/test',methods=['POST'])
def my_post():
    value=request.form["email"] # Searches for the specific name value
    value2=request.form["namebox"]
    print(value)
    print(value2)
    return value+value2



# @app.route('/Page2')
# def renderpage():
#     return render_template("Page2.html")
#



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
