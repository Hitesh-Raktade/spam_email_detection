from flask import Flask, render_template, request
from predict import predict_message  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        email_text = request.form.get("emailContent")
        if email_text and email_text.strip():
            result = predict_message(email_text)   
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
