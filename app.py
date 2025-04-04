from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# 保存上传视频的路径
UPLOAD_FOLDER = 'uploaded_videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return 'No video part in the request', 400

    video = request.files['video']
    if video.filename == '':
        return 'No selected file', 400

    filename = secure_filename(video.filename)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    video.save(save_path)
    return 'Video uploaded successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
