from flask import Flask, requent, render_template
import pickle

app = Flask(__name__)

vectorizer = pickle.load(open('vec.pkl','rb'))
classifier = pickle.load(open('clf.pkl','rb'))

@app.route('/', methods=['GET','POST'])
def home():
  if request.method == 'POST':
    input_text = request.form['news_text']
    input_vec = vectorizer.transform([input_text])
    input_clf = classifier.predict(input_vec)

return render_template('home.html')

if __name__ == '__main__':
  app.run()
