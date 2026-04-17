from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Fake AI result (بنغيره بعدين)
        result = "Object detected successfully!"

        return render_template('result.html', prediction=result, image=filepath)

    return "No file uploaded"

if __name__ == '__main__':
    app.run(debug=True)
