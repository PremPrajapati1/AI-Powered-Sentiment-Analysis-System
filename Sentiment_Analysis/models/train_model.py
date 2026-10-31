import os
import joblib
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load_Dataset
df = pd.read_csv("M:\Collage And Internship Project Files\AIML 3Month Project 2\Sentiment_Analysis\data\sentiment_analysis_dataset.csv")

# Clean The Required Columns
df = df.dropna(subset=["review_text", "sentiment"]).copy()
df["review_text"] = df["review_text"].astype(str).str.strip()
df["sentiment"] = df["sentiment"].astype(str).str.strip()
df = df[df["review_text"] != ""]
df = df[df["sentiment"] != ""]

# Remove Duplicates value
df = df.drop_duplicates(subset=["review_text"])

print("Dataset shape:", df.shape)
print("\nSentiment distribution:")
print(df["sentiment"].value_counts())

# Separate input and target
X = df["review_text"]
y = df["sentiment"]

# Split before training
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=42, stratify=y)

# Build a Pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])

# compare algorithms and tune parameters
param_grid = [
    {
        "tfidf__ngram_range": [(1, 1),(1, 2)],
        "tfidf__min_df": [1, 2],
        "classifier": [LogisticRegression(max_iter=1000)],
        "classifier__C": [1, 3]
    },
    {
        "tfidf__ngram_range": [(1, 1),(1, 2)],
        "tfidf__min_df": [1, 2],
        "classifier": [MultinomialNB()],
        "classifier__alpha": [0.5, 1.0]
    }
]

grid = GridSearchCV(estimator=pipeline, param_grid=param_grid, cv=5, scoring="f1_macro", n_jobs=1, verbose=1)
grid.fit(X_train, y_train)

# Select Best Model
best_model = grid.best_estimator_
print("\nBest parameters:", grid.best_params_)
print("Best CV macro F1:", round(grid.best_score_, 4))


# Evaluate on unseen test data
y_pred = best_model.predict(X_test)

print("\nTest Accuracy:", round(accuracy_score(y_test, y_pred), 4))

print("\nClassification report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Plot confusion matrix
labels = best_model.classes_
cm = confusion_matrix(y_test, y_pred, labels=labels)

os.makedirs("save_model", exist_ok=True)
os.makedirs("results", exist_ok=True)

plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=labels, yticklabels=labels)
plt.xlabel("Predicted Sentiment")
plt.ylabel("Actual Sentiment")
plt.title("Sentiment Analysis - Confusion Matrix")
plt.tight_layout()
plt.savefig("results/confusion_matrix.png", dpi=150)
plt.show()

# save
joblib.dump(best_model, "save_model/sentiment_pipeline.pkl")

print("\nModel saved to save_model/sentiment_pipeline.pkl")
print("Confusion matrix saved to results/confusion_matrix.png")