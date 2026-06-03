from flask import Flask, render_template, request, send_file,redirect, url_for
import pandas as pd
import joblib
import os
from flask import session 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    from_email = "creditcardfrauddect@gmail.com"  
    from_password = "yqew qokc cpzg xkhb" 
    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)

    # Set up the email details
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

app = Flask(__name__, template_folder="templates", static_folder="static")

# Load the trained model
model_file = 'random_forest.pkl'
model = joblib.load(model_file)

# Expected columns based on the model
expected_columns = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14',
                    'V15', 'V16', 'V17', 'V18', 'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']


@app.route('/')
def home():
    return render_template('appflask.html')


@app.route('/predict', methods=['POST'])
def predict():
    global input_df
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400

    try:
        # Read CSV file
        input_df = pd.read_csv(file)

        # Check if columns match expected format
        if not all(col in input_df.columns for col in expected_columns):
            return "Error: The uploaded file does not contain the required columns.", 400

        # Make predictions
        predictions = model.predict(input_df)

        # Add predictions to DataFrame
        input_df['Prediction'] = ["Fraudulent" if pred == 1 else "Non-Fraudulent" for pred in predictions]

        # Convert predictions to list for HTML rendering
        results = input_df[['Time', 'Amount', 'Prediction']].to_dict(orient="records")

                # Check for fraudulent transactions and send an email if found
        for row in input_df.itertuples():
            if row.Prediction == "Fraudulent":
                # Send an email for each fraudulent transaction
                subject = "Fraudulent Transaction Alert!!!!!"
                body = f"A fraudulent transaction was detected.\n\nTime: {row.Time}\nAmount: {row.Amount}\nPrediction: {row.Prediction}"
                to_email = "nandikarana9898@gmail.com"  # Replace with the recipient's email address
                send_email(subject, body, to_email)

        return render_template('appflask.html', results=results)

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/download')
def download():
    try:
        output_file = "predictions.csv"  # Define a filename
        input_df.to_csv(output_file, index=False)  # Save DataFrame as CSV

        return send_file(output_file, as_attachment=True)

    except Exception as e:
        return str(e)

@app.route('/logout')
def logout():
    session.clear()  # Clears session data if applicable
    return redirect(url_for('index'))  # Redirect to index.html

@app.route('/index')
def index():
    return render_template('index.html')  # Serve index.html 

@app.route('/loginsuccessful')
def login_success():
    return render_template('loginsuccessful.html')  # Ensure this file is inside templates folder

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)
