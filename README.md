# Salary Prediction Web App

## Overview

This web application predicts a salary based on the number of years of experience using a linear regression model. The application is built using Flask, a Python web framework.

## Prerequisites

Before using the Salary Prediction web application, ensure you have the following installed:

- Python (3.6 or higher)
- Flask
- scikit-learn
- pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Alwin-Sajan/Salary_Prediction_ML.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Salary_Prediction_ML
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter the number of years of experience and click the "Predict Salary" button.

## File Structure

- **app.py**: The main Flask application file.
- **templates/index.html**: HTML template for the web page.
- **Salary_data.csv**: Dataset containing information about years of experience and corresponding salaries.

## Dependencies

The following Python libraries are used in this project:

- Flask: Web application framework.
- pandas: Data manipulation library.
- scikit-learn: Machine learning library for linear regression.


## Additional Notes

- The linear regression model is trained on the provided dataset (`Salary_data.csv`).
- This application is for educational purposes, and additional considerations are needed for a production environment.

## Future Improvements

- Implement user authentication and authorization.
- Improve the front-end for a more user-friendly experience.
- Enhance error handling and input validation.
- Consider deploying the application to a production server.

