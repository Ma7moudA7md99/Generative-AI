from flask import Flask, render_template, request
import google.generativeai as palm


app = Flask(__name__)

palm.configure(api_key='AIzaSyBcrrD3VHaMaRRY87mVCMoTE6XdLDCcfrI')

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024   
}


@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""

    if request.method == 'POST':
        prompt = request.form['prompt']

        respone = palm.generate_text(**defaults, prompt=prompt)
        response_text = respone.result

    return render_template("home.html", response_text=response_text)


if __name__ == '__main__':
    app.run(debug=True)
