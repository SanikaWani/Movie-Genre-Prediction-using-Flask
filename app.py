# Importing essential libraries
from flask import Flask, render_template, request
import pickle

# Load the Multinomial Naive Bayes model and CountVectorizer object from disk
filename = 'movie-genre-mnb-model.pkl'
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('cv-transform.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Retrieve the message from the form
            message = request.form['message']
            
            # Prepare the message for prediction
            data = [message]
            vect = cv.transform(data).toarray()
            
            # Make a prediction
            my_prediction = classifier.predict(vect)
            
            # Render the result page with the prediction
            return render_template('result.html', prediction=my_prediction[0])
        
        except Exception as e:
            # Handle exceptions (e.g., missing vectorizer or model, invalid input)
            return f"An error occurred: {e}"
    
    # Handle other request methods (if necessary)
    return "Invalid request method"

if __name__ == '__main__':
	app.run(debug=True)