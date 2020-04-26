from flask import Flask, render_template, request,flash
import otg_classifier
import pprint
import requests
import json

app = Flask(__name__)

@app.route('/')
def make():
    return render_template('index.html')

@app.route('/getFlair', methods=['POST', 'GET'])
def predict():
    if request.method=='POST':
        x = request.form['url']
        flairName,actual_flair = otg_classifier.predictIt(x)
        return render_template('flair.html', flair=flairName,actual=actual_flair)

@app.route('/automated_testing', methods=['POST', 'GET'])
def test():
    op_dic = {}
    if request.method == 'POST':
        if 'upload_file' not in request.files:
            pprint('No selected file')
            return 0
        else:
            data = request.files
            urls = data['upload_file'].readline()
            cnt = 1
            while urls:
                # print("Line {}: {}".format(cnt, urls.strip()))
                url = urls.strip().decode()
                print(url)
                try:
                    flairname,_ = otg_classifier.predictIt(str(url))
                    op_dic[str(url)] = str(flairname)
                    urls = data['upload_file'].readline()
                except:
                    break
            j = json.dumps(op_dic)
            print(j)
            return j

if __name__ == '__main__':
    app.run(debug=False)
