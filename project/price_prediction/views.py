from django.shortcuts import render
import joblib

# Load the trained model
model = joblib.load('C:\\Users\\Alfin\\PycharmProjects\\electricity_bill\\project\\price_prediction\\models\\linear_regression_model.joblib')

def predict_price(request):
    predicted_price = None  # Initialize to None
    if request.method == 'POST':
        last_reading = float(request.POST['last_reading'])
        current_reading = float(request.POST['current_reading'])
        # Assuming the form has fields for 'last_reading' and 'current_reading'

        # Make predictions
        predicted_price = model.predict([[last_reading, current_reading, current_reading - last_reading]])

    return render(request, 'price_prediction/predict_price.html', {'predicted_price': predicted_price})

