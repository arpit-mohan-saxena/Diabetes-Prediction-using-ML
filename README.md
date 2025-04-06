💉 SugarSense - Diabetes Prediction and Management
📌 Overview
SugarSense is a comprehensive web application designed to predict the likelihood of diabetes based on user health data using machine learning. Beyond prediction, it offers personalized tips for diabetes management based on age and BMI, suggests diabetic-friendly recipes, and includes visual progress tracking features for users.

🚧 Work in Progress: Currently working on adding user-based charts to visualize and track previous readings over time for better diabetes management insights.

This project involves:

Data preprocessing

Exploratory Data Analysis (EDA)

Machine learning classification models

Personalized health recommendations

Recipe suggestions

Progress tracking with visual charts

🛠️ Technologies Used
Python: For machine learning and backend logic

Pandas: For data manipulation and analysis

NumPy: For numerical operations

Scikit-learn: For machine learning models and evaluation

Flask: For the web backend

Matplotlib & Seaborn: For data visualizations

Jupyter Notebook: For development and model training

📊 Dataset
The dataset used is the PIMA Indians Diabetes Dataset (or replace with your actual source). It includes several medical attributes such as:

Glucose Level

Insulin

BMI (Body Mass Index)

Age

Blood Pressure

Skin Thickness

Pregnancies

Diabetes Pedigree Function (a measure of family history)

🚀 Installation & Usage
Prerequisites
Make sure you have Python 3.x installed. You also need the libraries listed in requirements.txt.

Steps to Run the Project
Clone the repository:

bash
Copy
Edit
git clone https://github.com/arpit-mohan-saxena/Diabetes-Prediction-using-ML.git
cd Diabetes-Prediction-using-ML
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the model training and predictions:

Open and run the Jupyter Notebook file (model_training.ipynb) for training the machine learning model.

Once the model is trained, you can use it for making predictions based on new user input.

To run the web interface:

Start the Flask app:

bash
Copy
Edit
python app.py
Visit the app in your browser:

cpp
Copy
Edit
http://127.0.0.1:5000
Running the App
After the server is up, you can enter details (like age, BMI, etc.) and get diabetes predictions. The app will also provide personalized tips based on your health information, suggest diabetic-friendly recipes, and track progress through visual charts.

📈 Upcoming Feature: You'll soon be able to view user-based progress charts to monitor and analyze your historical readings over time.

📈 Model Performance
Training Accuracy: 78.66%

Testing Accuracy: 77.27%

Evaluation Metrics: Precision, Recall, F1-Score

The model is evaluated on several metrics to ensure its prediction accuracy and reliability.

📸 Visualizations
The project includes insightful visualizations that help both the user and developers understand the data and model performance better:

Correlation Heatmaps: To show relationships between different health metrics

Distribution Plots: For visualizing the distribution of key features like BMI, Glucose Levels, etc.

Feature Importance Charts: To display which features are most influential in predicting diabetes

(Feel free to add screenshots or graphs in this section for better presentation.)

🍴 Personalized Features
SugarSense offers features tailored to user health needs:

Personalized Tips: The app provides health suggestions based on the user’s age and BMI to manage and prevent diabetes.

Diabetic-Friendly Recipes: The app recommends healthy recipes and links to resources for a diabetic-friendly diet.

Progress Tracking: Users can track their progress with visual charts that display their diabetes management over time.

👥 Future Update: Enhanced tracking by storing and charting user-specific past records for more personalized health insights.

📢 Contributions
Contributions are welcome! 🎉
Feel free to fork the repository, submit issues, or open pull requests to make improvements.

🙏 Acknowledgments
Scikit-learn: For providing machine learning algorithms used in the project

Flask: For creating the backend server that runs the app

Pandas, NumPy, Matplotlib, Seaborn: For assisting with data manipulation and visualizations

Open-Source Community: For their contributions to the libraries and frameworks that made this project possible
