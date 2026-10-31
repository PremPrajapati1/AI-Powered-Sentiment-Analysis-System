# AI-Powered Sentiment Analysis System

An AI-powered sentiment analysis application that analyzes customer reviews and classifies them into three categories: **Positive, Negative, and Neutral**.

This project uses Natural Language Processing (NLP), TF-IDF vectorization, and machine learning algorithms to understand customer opinions and evaluate sentiment classification performance. A Streamlit web application provides an interactive interface for users to analyze reviews.

## Features

- Classifies customer reviews into Positive, Negative, and Neutral sentiments.
- Text preprocessing and feature extraction using TF-IDF.
- Machine learning model comparison.
- Hyperparameter tuning using GridSearchCV.
- 5-fold cross-validation.
- Model evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - Confusion Matrix
- Saves the trained sentiment analysis pipeline.
- Interactive web application built with Streamlit.

## Technologies Used

- **Programming Language:** Python
- **NLP:** TF-IDF
- **Machine Learning:** Logistic Regression, Multinomial Naive Bayes
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib
- **Web Framework:** Streamlit
- **Model Serialization:** Pickle

## Project Structure

```text
Sentiment_Analysis/
│
├── data/
│   └── customer_reviews.csv
│
├── models/
│   └── train_model.py
│
├── save_model/
│   └── sentiment_pipeline.pkl
│
├── results/
│   └── confusion_matrix.png
│
├── app.py
├── requirements.txt
└── README.md
```

*Note: Update the folder structure above if your actual project directories are different.*

## Machine Learning Workflow

1. Load the customer reviews dataset.
2. Clean and preprocess review text.
3. Convert text into numerical features using TF-IDF.
4. Split the dataset into training and testing sets.
5. Train and compare machine learning classifiers.
6. Perform hyperparameter tuning using GridSearchCV.
7. Apply 5-fold cross-validation.
8. Evaluate the best-performing model.
9. Save the trained pipeline.
10. Use Streamlit to make predictions through a web interface.

## Model Performance

The following results were obtained during the current experiment:

| Evaluation Metric | Result |
|---|---:|
| Test Accuracy | 100% |
| Cross-validation Macro F1 | 100% |
| Negative Precision | 100% |
| Negative Recall | 100% |
| Neutral Precision | 100% |
| Neutral Recall | 100% |
| Positive Precision | 100% |
| Positive Recall | 100% |

### Confusion Matrix

The model correctly classified all 60 test samples.

| Actual / Predicted | Negative | Neutral | Positive |
|---|---:|---:|---:|
| Negative | 20 | 0 | 0 |
| Neutral | 0 | 20 | 0 |
| Positive | 0 | 0 | 20 |

### Best Model Parameters

The GridSearchCV process selected Logistic Regression with the following parameters:

- Classifier: Logistic Regression
- C: 1
- TF-IDF minimum document frequency: 1
- N-gram range: (1, 2)
- Cross-validation: 5 folds
- Best CV macro F1-score: 1.00

**Dataset note:** Although the original dataset contained 10,000 rows, duplicate removal left 300 unique reviews, with 100 reviews in each sentiment class. The experiment used 240 training samples and 60 testing samples. The perfect scores should therefore be interpreted cautiously; further testing on a larger, independent dataset is needed to assess real-world generalization.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Sentiment_Analysis.git
```

### 2. Navigate to the project directory

```bash
cd Sentiment_Analysis
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Train the Model

Run the training script:

```bash
python models/train_model.py
```

The trained pipeline and evaluation results will be saved in their respective output directories.

## Run the Streamlit Application

Start the application using:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## Future Improvements

- Train on a larger and more diverse customer review dataset.
- Test model performance on unseen real-world reviews.
- Explore advanced NLP models such as BERT.
- Add sentiment visualization and analytics dashboards.
- Deploy the Streamlit application online.

## Author

**Prem Kumar**

BCA Student | Software Developer

## License

This project is intended for educational and learning purposes.
