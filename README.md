House Rate Prediction System

This project is a Machine Learning-based system designed to predict house prices based on various features like area, bedrooms, bathrooms, and amenities. The system uses Python, Flask, and HTML for user interaction and prediction display.

🚀 Features

✅ Predicts house prices using machine learning algorithms
✅ User-friendly HTML form for input
✅ Displays prediction results directly on the webpage
✅ Built using Python, Flask, and scikit-learn

📂 Project Structure

/House-Rate-Prediction
├── app.py            # Main Flask application (entry point)
├── train.py          # ML model training script
├── train3133.pkl     # Trained machine learning model & scaler
├── requirements.txt  # Dependencies for the project
├── templates/        # HTML templates folder
│   ├── front.html    # Welcome page
│   └── index.html    # Input form for prediction
└── static/           # CSS, images, etc.

🖥️ Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/sarthakhadawale/House-Rate-Prediction.git
cd House-Rate-Prediction

Step 2: Create a Virtual Environment

python -m venv venv

Step 3: Activate the Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Step 4: Install Dependencies

pip install -r requirements.txt

Step 5: Run the Flask App

python app.py

Step 6: Access the Application

Open your browser and go to: ➡️ http://localhost:5002

⚙️ Usage

On the Welcome Page, click "Continue".

Fill in the required input values in the HTML form.

Click the "Submit" button to get the predicted house price.

The predicted price will be displayed on the same page.

📊 Input Features

area (sq. ft.)

bedrooms (number of bedrooms)

bathrooms (number of bathrooms)

stories (number of floors)

mainroad (1 = Yes, 0 = No)

guestroom (1 = Yes, 0 = No)

basement (1 = Yes, 0 = No)

hotwaterheating (1 = Yes, 0 = No)

airconditioning (1 = Yes, 0 = No)

parking (number of parking spaces)

prefarea (1 = Yes, 0 = No)

furnishingstatus (1 = Furnished, 0.5 = Semi-furnished, 0 = Unfurnished)

🔎 Sample Prediction Output

✅ Prediction: The estimated house price is ₹X,XX,XXX

🧩 Model Training

The train.py script is used to train the machine learning model.

The trained model and scaler are saved as train3133.pkl.

The saved model is loaded in app.py for predictions.

❗ Important Notes

Ensure the train3133.pkl file is present in the project folder.

If you face issues like ModuleNotFoundError, run:

pip install <missing_module>

🤝 Contributing

Contributions are welcome! If you encounter any bugs or have suggestions for improvement, feel free to create an issue or submit a pull request.

🏆 Credits

Developed by: Sarthak Hadawale
Project guided by: Technogeek's Data Science course

