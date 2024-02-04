from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load the dataset and train the model
df = pd.read_csv("Salary_data.csv")
reg = LinearRegression()
reg.fit(df[['YearsExperience']], df.Salary)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    years_experience = float(request.form['years_experience'])

    # Use the trained model for prediction
    salary_prediction = reg.predict([[years_experience]])

    return render_template('index.html', prediction=f'Predicted Salary: ${salary_prediction[0]:,.2f}')

if __name__ == '__main__':
    app.run(debug=True)
