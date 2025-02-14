from flask import Flask, request, jsonify
import csv
import smtplib

app = Flask(__name__)

# ✅ Save form data
def save_to_csv(data):
    with open("submissions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([data['name'], data['email'], data['message']])

# ✅ Send email
def send_email(data):
    sender_email = "your-email@gmail.com"
    receiver_email = "ittainer123@outlook.com"
    password = "your-email-password"

    subject = "New Volunteer Submission"
    body = f"Name: {data['name']}\nEmail: {data['email']}\nMessage: {data['message']}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{body}")

# ✅ API Endpoint
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    save_to_csv(data)
    send_email(data)
    return jsonify({"message": "Form submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
