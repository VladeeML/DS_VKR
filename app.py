from flask import Flask, request, render_template
from keras.models import load_model
import pandas as pd
import joblib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def compute():
    text_result = ''
    error = dict()
    if request.method == 'POST':
        data = request.form
        try:
            data1 = {k:[float(v)] for k,v in data.items()}
        except ValueError:
            for k,v in data.items():
                try:
                    float(v)
                except ValueError:
                    error['name'] = k
                    error['value'] = v
                    break
        if not error:
            input = pd.DataFrame(data=data1)
            result = model.predict(input)[0][0]
            text_result = '{column} = {data:.5f}'.format(column='Соотношение матрица-наполнитель', data=result)
    return render_template('index.html', result=text_result, error=error)


if __name__ == '__main__':
    model = load_model('model_mn')
    app.run(host='localhost', port=8081, debug=True)