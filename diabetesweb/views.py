from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load and train model once
data = pd.read_csv('C:/Users/arpit/Downloads/diabetes.csv')  # Updated path
X = data.drop("Outcome", axis=1)
Y = data["Outcome"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    if request.method == 'POST':
        val1 = float(request.POST['pregnancies'])
        val2 = float(request.POST['glucose'])
        val3 = float(request.POST['bloodPressure'])
        val4 = float(request.POST['skinThickness'])
        val5 = float(request.POST['insulin'])
        val6 = float(request.POST['bmi'])  # BMI
        val7 = 0.5  # Default Diabetes Pedigree Function
        val8 = float(request.POST['age'])  # Age

        # Make prediction
        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
        has_diabetes = pred[0] == 1

        if has_diabetes:
            result_text = "⚠️ You have Diabetes"
            bg_class = "danger-bg"
            tips_heading = "🩺 Tips to Manage Diabetes"
            tips = [
                "Stay physically active (e.g., 30 mins walk daily)",
                "Maintain a healthy, balanced diet",
                "Regularly monitor blood sugar levels",
                "Stay hydrated – drink plenty of water",
                "Get enough sleep (7–9 hours)",
                "Avoid smoking and excessive alcohol"
            ]
        else:
            result_text = "✅ You don't have Diabetes"
            bg_class = "safe-bg"
            tips_heading = "💪 Tips to Stay Healthy and Prevent Diabetes"
            tips = [
                "Exercise regularly to maintain a healthy weight",
                "Eat more fruits, vegetables, and whole grains",
                "Limit sugar and refined carbs",
                "Get regular health checkups",
                "Sleep well and manage stress",
                "Stay consistent with healthy routines"
            ]

        # ✅ Add custom tips based on age and BMI
        custom_tips = []

        # Age-based suggestions
        if val8 < 30:
            custom_tips.append("Build strong health habits while you're young.")
        elif 30 <= val8 < 50:
            custom_tips.append("Include strength training in your routine.")
        else:
            custom_tips.append("Get regular screenings and stay active.")

        # BMI-based suggestions
        if val6 < 18.5:
            custom_tips.append("You're underweight. Consider a nutritionist's advice.")
        elif 18.5 <= val6 <= 24.9:
            custom_tips.append("Your BMI is healthy. Keep it up!")
        elif 25 <= val6 <= 29.9:
            custom_tips.append("You're overweight. Focus on cardio & portion control.")
        else:
            custom_tips.append("Obesity increases health risks. Prioritize a balanced diet and regular activity.")

        return render(request, "result.html", {
            "result2": result_text,
            "bg_class": bg_class,
            "tips_heading": tips_heading,
            "tips": tips,
            "custom_tips": custom_tips
        })
    else:
        return render(request, "predict.html")
