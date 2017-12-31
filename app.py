from flask import Flask, render_template, request, jsonify
from skippers import identify_skippers

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='<#',
        comment_end_string='#>'
    ))

app = CustomFlask(__name__)

@app.route('/')
def index():
    return render_template('skippers.html')

@app.route('/refresh-data-set', methods=['POST'])
def refresh_data():
    time = request.get_json()['time']
    skip = request.get_json()['skip']
    skippers = identify_skippers(int(time), int(skip))
    return jsonify(skippers)

if __name__ == '__main__':
    app.run()
