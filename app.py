from flask import Flask,render_template,request
from flask_cors import cross_origin
from matplotlib import image
app = Flask(__name__)
from classifier import VehiclesCounting
import cv2
log_filename = 'Camera 1'
line_position = 0.7
line_angle = 0


@app.route('/')
@app.route('/home')
def home():
    #cl.model_load()
    return render_template('home.html')

@app.route('/result', methods=['GET','POST'])
def result():

    if request.method == 'POST':
        
        f = request.files['vi']  
        f.save(f.filename)
        n = 'Result ' + f.filename
        #image = request.file["video"]
        #image.save("static/uploads/"+image.filename)
        vc=VehiclesCounting(log_filename, video=f.filename, info=True,dont_show=True,output=n,detection_line=(line_position, line_angle))
        #result = vc.run()
        vc.run()
        #cv2.imshow(result)
        return render_template('result.html', op = n)

if __name__ == "__main__":
    app.run(debug=True)