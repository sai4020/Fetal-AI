from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
model=pickle.load(open('fetal_health_model.pkl','rb'))


@app.route('/')
def f():
    return render_template('index.html')

@app.route('/inspect')
def inspect():
    return render_template('inspect.html')

@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        input_data = request.form
        print(input_data)  # Debugging line

        # Access the form data and convert it to float
        feature1 = float(input_data.get('feature1'))
        feature2 = float(input_data.get('feature2'))
        feature3 = float(input_data.get('feature3'))
        feature4 = float(input_data.get('feature4'))
        feature5 = float(input_data.get('feature5'))
        feature6 = float(input_data.get('feature6'))
        feature7 = float(input_data.get('feature7'))
        feature8 = float(input_data.get('feature8'))
    
        # Make predictions using the loaded model
        input_features = [feature1, feature2, feature3, feature4, feature5, feature6, feature7,feature8]
        output = model.predict([input_features])

        # Process the output and return it
        res =  str(output[0])
        if res=="1":
            result="Normal"
        elif res=="2":
            result="Suspect"
        elif res=="3":
            result="Pathological"
        return render_template('output.html', output=result)


if __name__ == "__main__":
    app.run(port=5000, debug=False)
