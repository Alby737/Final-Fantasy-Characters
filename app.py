from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    # List all images in the static/img directory
    imgs = os.listdir('static/')
    # Convert relative paths to absolute paths
    imgs = ['static/' + file for file in imgs]
    # Select a random image
    random_img = random.choice(imgs)
    # Render the template with the path to the random image
    return render_template('index.html', img=random_img)

if __name__ == '__main__':
    app.run(debug=True,port=5793, host='0.0.0.0')

