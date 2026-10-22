from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if name and email:
            message = f"Thanks, {name}! Your interest has been noted."
        else:
            message = "Please enter your name and email address."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)