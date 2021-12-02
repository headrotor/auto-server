from flask import Flask, render_template, jsonify, request, redirect, url_for
from random import randint
 
app = Flask(__name__)
@app.route('/')
def hex_color():
    return render_template("index.html")
 
@app.route('/valueofslider')
def slide():
    slide_val = request.args.get('slide_val')
    print(slide_val)
    return slide_val

@app.route('/valueofslider2')
def slide2():
    slide_val = request.args.get('slide_val')
    print(slide_val)
    return slide_val

@app.route('/dragvalue')
def drag():
    drag_val = request.args.get('drag_val')
    print(f"val1: {drag_val}")
    return drag_val

@app.route('/dragvalue2')
def drag2():
    drag_val = request.args.get('drag_val')
    print(f"val2: {drag_val}")
    return drag_val

@app.route('/SomeFunction')
def SomeFunction():
    print('Button Pressed')
    return "Nothing"


if __name__ == '__main__':
    app.run(debug=True,host="192.168.1.149",port=5007)
