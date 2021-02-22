from flask import Flask, flash, request, redirect, url_for,render_template

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def clock():
    if request.method =="GET":
        return render_template("index.html")

if __name__ =='__main__':
	app.run(debug = True)