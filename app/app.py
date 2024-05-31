import os

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime

import src.preprocessing as preprocessing
import src.scorer as scorer

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':

            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)

                new_filename = f'{filename.split(".")[0]}_{str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))}.csv'
                save_location = os.path.join('input', new_filename)
                file.save(save_location)

                input_df = preprocessing.import_data(save_location)
                preprocessed_df = preprocessing.run_preproc(input_df)

                submission = scorer.make_pred(preprocessed_df, save_location)
                submission.to_csv(save_location.replace('input', 'output'), index=False)

                return redirect(url_for('download'))
            
        return render_template('upload.html')

    @app.route('/download')
    def download():
        return render_template('download.html', files=os.listdir('output'))

    @app.route('/download/<filename>')
    def download_file(filename):
        return send_from_directory('output', filename)

    return app