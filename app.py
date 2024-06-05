from flask import Flask, request, jsonify, render_template
import openai
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

openai.api_key = app.config['OPENAI_API_KEY']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/prompt', methods=['POST'])
def prompt():
    data = request.json
    prompt_text = data['prompt']
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Example engine
        prompt=prompt_text,
        max_tokens=150
    )

    return jsonify(response=response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)
