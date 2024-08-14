# Movie Genre Classification

This project focuses on building a machine learning model that predicts the genre of a movie based on its plot summary or other textual information. The model helps classify movies into genres like action, romance, thriller, drama, or comedy.

## Project Overview

- **Project Name:** Movie Genre Classification
- **Dataset:** `kaggle_movie_train.csv`
- **Objective:** To predict the genre of a movie based on its plot description.
- **Main File:** `app.py`
- **Model Output:** The trained model is saved as `movie-genre-mnb-model.pkl`, and the TF-IDF vectorizer is saved as `cv-transform.pickle`.

## Methodology

1. **Data Preprocessing:**
   - The dataset was loaded, and the textual data was preprocessed to remove noise, tokenize words, and apply techniques like TF-IDF or word embeddings.
   - The preprocessed text was then used to create feature vectors.

2. **Modeling:**
   - Several classifiers were explored, including:
     - Naive Bayes
     - Logistic Regression
     - Support Vector Machines
   - After experimentation, the best-performing model was saved using pickle as `movie-genre-mnb-model.pkl`.

3. **Model Evaluation:**
   - The model was evaluated on various metrics to ensure its accuracy in predicting movie genres.
   - The final model was chosen based on its performance on a validation set.

4. **Prediction:**
   - Users can input a movie's plot summary, and the model will predict its genre, such as action, romantic, thriller, drama, or comedy.

## Files in the Repository

- `app.py`: The main Python file that contains the implementation of the movie genre classification model.
- `cv-transform.pickle`: Pickled file of the TF-IDF vectorizer used to transform the input text.
- `movie-genre-mnb-model.pkl`: Pickled file of the trained Naive Bayes model.
- `kaggle_movie_train.csv`: The dataset used for training the model.
- `README.md`: Project documentation (this file).

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/movie-genre-classification.git

## Install Dependencies

pip install -r requirements.txt

## Run the Application

python app.py

## Predict Movie Genre

1.Input the plot summary of a movie.
2.The model will output the predicted genre, such as action, romantic, thriller, drama, or comedy.

## Model Details

TF-IDF Vectorization: Used to convert text into numerical features.
Classifier: Naive Bayes (other classifiers like Logistic Regression and SVM were also explored).
Evaluation Metrics: The model's performance was evaluated using metrics like accuracy, precision, recall, and F1 score.
