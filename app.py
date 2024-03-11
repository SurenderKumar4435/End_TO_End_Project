from flask import Flask,request

app  = Flask(__name__)

@app.route("/",methods=["GET"])
def hello():
    return "<h1>Hello Surender Kumar you are welcome</h1> !"



@app.route("/welcome",methods=["GET"])
def welcome():
    return "Hello Surender Kumar you are welcome2 !"

@app.route("/success/<score>")
def success(score):
    return "Hello Surender Kumar you are  marks {} ".format(score)



@app.route("/fail/<score>")
def success(score):
    return "Hello Surender Kumar you are  marks {} ".format(score)


if __name__=="__main__":
    app.run(debug= True)