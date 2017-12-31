from flask import Flask, render_template, request

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
    pass

if __name__ == '__main__':
    app.run()
