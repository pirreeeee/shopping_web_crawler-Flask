# encoding=UTF-8
from flask import Flask, render_template, request, Response, redirect, url_for
import json
import yahoo 
import momo

app = Flask(__name__)

    

@app.route('/')
def index():    # get html page
    return render_template('index.html')

@app.route('/yahoo')
def html_table():
    df = yahoo.crawler()
    # content = yahoo.content()
    url = yahoo.imgUrl()
    return render_template('yahoo.html',  tables=[df.to_html(classes='data', header="true")], urlList = url)

@app.route('/momo')
def html():
    df = momo.craw()
    content = momo.bank()
    return render_template('momo.html',  tables=[df.to_html(classes='data', header="true")], contentlist = content)


if __name__ == "__main__":
    app.config['ENV'] = "development"
    app.config['DEBUG'] = True
    app.run(port=3000)