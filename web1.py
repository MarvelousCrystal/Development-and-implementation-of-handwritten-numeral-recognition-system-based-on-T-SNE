from flask import Flask,render_template,url_for, flash, request, redirect
from werkzeug.utils import secure_filename
import os
import io, base64
from kmeans_label import low_predict
from high_knn_label import highknn_predict,dealdata
from low_knn_label import lowknn_predict
from low_dimense import highTOlow,to_2Dresult


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def image_to_base64(image_path):
    byteio = io.BytesIO()
    byteio.write(open(image_path, "rb").read())
    byteio.seek(0)
    data = byteio.read()
    return base64.b64encode(data).decode()

@app.route('/', methods=['GET', 'POST'])#可以不输入homepage,直接到该网页
@app.route("/homepage",methods=['GET', 'POST'])
def homepage(name=None):
    return render_template("homepage.html", name=name)


@app.route("/show",methods=['GET', 'POST'])
def show():
    return render_template("show.html")

@app.route("/dimensereduct",methods=['GET', 'POST'])
def dimensereduct():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_path)
            origin = image_to_base64(full_path)
            dealdata(full_path)
            highTOlow()
            to_2Dresult()
            low_predict()
            args1, args2 = request.form["args1"], request.form["args2"]
            res = highknn_predict(int(args1))
            image1 = image_to_base64(res)

            low_res = lowknn_predict(int(args2))

            image2 = image_to_base64(low_res)

            # final = knn_predict()

            data_map = {
                "image1": image1,
                "image2": image2,
                # "final": final,
                "origin": origin
            }
            return render_template('dimensereduct.html', **data_map)
    return render_template("dimensereduct.html")

@app.route("/predict",methods=['GET', 'POST'])
def predict():
    return render_template("predict.html")

@app.route("/index",methods=['GET', 'POST'])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
