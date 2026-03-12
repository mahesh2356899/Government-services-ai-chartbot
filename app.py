from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form["msg"].lower()
    responses = {
        "ration": "To apply for Ration Card, visit your nearest MeeSeva center.",
        "pan": "You can apply for PAN card at https://www.onlineservices.nsdl.com",
        "scholarship": "Visit National Scholarship Portal: https://scholarships.gov.in",
        "aadhaar": "Aadhaar services are available at https://uidai.gov.in",
        "voter": "Apply for Voter ID at https://www.nvsp.in",
        "passport": "Passport services are available at https://www.passportindia.gov.in",
        "driving": "Driving License services are available at https://parivahan.gov.in"
    }

    for key in responses:
        if key in user_message:
            return jsonify({"response": responses[key]})

    return jsonify({"response": "Sorry, I can help with Ration, PAN, Aadhaar, Voter ID, Passport, and Scholarships only."})

if __name__ == "__main__":
    app.run(debug=True)