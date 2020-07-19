from flask import Flask, request, render_template
import sam_pro
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    for x in request.form.values():
        s=x
    output=sam_pro.func(s)
    
    
    return render_template('index.html', prediction_text='Sensed meaning : {}'.format(output))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)
