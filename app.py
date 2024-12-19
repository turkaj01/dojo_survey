from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "mysecretkey"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if the form is being submitted and the fields are populated
        name = request.form.get("name")
        location = request.form.get("location")
        language = request.form.get("language")
        comment = request.form.get("comment")

        # Store form data in the session only if they're not empty
        if name and location and language and comment:
            session["name"] = name
            session["location"] = location
            session["language"] = language
            session["comment"] = comment
            # Redirect to the results page
            return redirect("/results")
        else:
            # Handle case where any of the form fields are empty
            error_message = "Please fill in all fields"
            return render_template("index.html", error=error_message)
    
    return render_template("index.html")

@app.route("/results")
def results():
    # Retrieve form data from the session
    name = session.get("name")
    location = session.get("location")
    language = session.get("language")
    comment = session.get("comment")

    # Check if session variables exist
    if name and location and language and comment:
        # Pass the data to the template
        return render_template("results.html", name=name, location=location, language=language, comment=comment)
    else:
        # Handle case where session data isn't found
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
