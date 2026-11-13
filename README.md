# Student Performance Prediction Using Machine Learning

## PROJECT OVERVIEW
This project uses Machine Learning techniques to predict student performance based on input student data. It demonstrates the complete machine learning workflow, including data preprocessing, model training, model evaluation, model saving, and making predictions on new records.

## TECHNOLOGIES USED
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib / Seaborn (if used)

## PROJECT FEATURES
- Data loading and preprocessing
- Exploratory data analysis
- Training and evaluation of Machine Learning models
- Comparison of model performance
- Saving the best-performing trained model
- Loading the saved model for future predictions
- Predicting results for new student records
- Interactive Streamlit application

## PROJECT STRUCTURE
```text
Student-Performance-Prediction-ML/
│
├── app.py
├── best_student_model.joblib
├── new_student_records.csv
├── requirements.txt
└── README.md
```

## HOW TO RUN THE PROJECT

### 1. Clone the Repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder
```bash
cd Student-Performance-Prediction-ML
```

### 3. Install Required Libraries
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```

## MODEL PREDICTION
The project loads the saved Machine Learning model and uses it to generate predictions for new student records.

## LEARNING OUTCOMES
- Understanding the Machine Learning workflow
- Data preprocessing and feature handling
- Model training and evaluation
- Saving and loading trained models
- Making predictions on unseen data
- Building an interactive application using Streamlit
