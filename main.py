from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form action="/encrypt" method="POST">
            rotate by
            <input type="text" name="rot" value="0">
            <textarea name="text">{}</textarea>
            <input type="submit" value="Submit Query">
        </form>
    </body>
</html>
'''

@app.route("/")
def index():
    return form.format("")

@app.route("/encrypt", methods=['GET', 'POST'])
def encrypt():
    rot = int(request.form.get('rot'))
    rot_text = request.form.get('text')
    encrypt_text = rotate_string(rot_text, rot)
    return form.format(encrypt_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
