from flask import Flask,request
from caesar import rotate_string
app=Flask(__name__)
app.config["DEBUG"] =True

form='''
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
      
 <h1>Caesar</h1>
    <form method="POST">
        <label for="rot"><strong>Roatate by:</strong>
        <input id="rot" type="text" name="rot" value="0">
        </label> 
        <label for="message">
        <textarea id='message' name="text">{0}</textarea>
        </label> 
        
        <button type="submit"><strong>Submit Query</strong></button>
    </form>
    </body>
</html>
'''


@app.route('/')
def index():
#will display form from form golbal variable
    return form.format(" ")


#returning form.format(variable) will allow data to return on same page in same form. (compared to just returning form)

@app.route('/' , methods=["POST"])
def encrypt():
    text = request.form['text']
    rot = request.form['rot']
    encrypt_string = rotate_string(text, int(rot))
    
    return form.format(encrypt_string)
#returning form.format(variable) will allow data to return on same page in same form(compared to returning encrypt_string)
app.run()
