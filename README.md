# Loan Eligibility Prediction

## Overview

This project is a web application that predicts loan eligibility based on user inputs. It uses a machine learning model trained on historical loan data to assess whether an applicant qualifies for a loan. The application is built using Flask and serves as a user-friendly interface for interacting with the model.

## Features

- **User-Friendly Interface:** The application provides a simple HTML form where users can input their details.
- **Loan Eligibility Prediction:** Based on the provided information, the application predicts whether the user is eligible for a loan.
- **Real-Time Response:** The application gives instant feedback on loan eligibility after form submission.

## Prerequisites

- Python 3.x
- Flask
- Scikit-learn
- Pandas
- Pickle

## Project Structure

- **app.py:** Main Flask application script.
- **templates/:** Directory containing HTML templates for the web pages.
  - `acc.html:` The main page where users input their details.
  - `succes.html:` Page displayed when the loan is approved.
  - `fail.html:` Page displayed when the loan is not approved.
- **loan-final-new_model.pkl:** The pre-trained machine learning model used for prediction.

## Usage

- **Home Page:** Users are greeted with a form where they can enter their personal and financial details.
- **Prediction Process:**
  - User inputs are processed and converted into numerical values that the model can understand.
  - The model predicts the loan eligibility based on the input features.
- **Results Page:** Depending on the prediction, the user is directed to either the success page (loan approved) or the failure page (loan not approved).

## Input Fields

- **Income of Applicant**
- **Co-Applicant Income**
- **Loan Amount**
- **Loan Term (in months)**
- **Number of Dependents**
- **Property Area** (Urban, Rural, Semi-urban)
- **Marital Status** (Single, Married)
- **Self-Employed** (Yes, No)
- **Education** (Graduate, Not-Graduate)
- **Gender** (Male, Female)
- **Previous Loan History** (Yes, No)

## Model Details

The prediction model is a machine learning classifier trained on a dataset of loan applications. The model uses various features such as applicant income, loan amount, and other demographic information to predict whether a loan application will be approved.

## Deployment

The application can be deployed on any server that supports Flask. For larger-scale use, consider deploying on cloud platforms like AWS, GCP, or Azure with appropriate scaling configurations.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this code.
   
   
   
