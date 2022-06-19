from flask import Flask, render_template, request, Response
import gamepad
import screencapture

app = Flask(__name__)
gamepadMethod = []

for k, v in gamepad.__dict__.items():
    if "function" in str(v):
        if not (k.startswith('_')):
            gamepadMethod.append(k)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
            fires = getattr(gamepad, request.form['prout'])
            fires()

    return render_template('index.html', methodList=gamepadMethod)

@app.route('/video_feed')
def video_feed():
    return Response(screencapture.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
