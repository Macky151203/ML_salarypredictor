from flask import Flask, render_template, request
import sal as s


app = Flask(__name__)

m=1

@app.route("/", methods=["GET","POST"])
def sal():
    global m
    if request.method=="POST" :
        salary = request.form["salary"]
        sal_pred= int(s.salprediction(salary))
        m=sal_pred
        print(sal_pred)
    return render_template("index.html", salpred= m)


if __name__=="__main__":
    app.run(debug=True)