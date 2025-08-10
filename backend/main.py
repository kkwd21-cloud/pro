from flask import Flask, request, send_file, jsonify
import os
import subprocess
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/create_video', methods=['POST'])
def create_video():
    if 'audio' not in request.files or 'image' not in request.files:
        return jsonify({'error': '음악과 이미지 파일을 모두 업로드해야 합니다.'}), 400

    audio_file = request.files['audio']
    image_file = request.files['image']

    audio_path = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()) + '_' + audio_file.filename)
    image_path = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()) + '_' + image_file.filename)

    audio_file.save(audio_path)
    image_file.save(image_path)

    output_filename = str(uuid.uuid4()) + '_output.mp4'
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)

    # FFmpeg 명령어:
    # 이미지와 오디오를 합쳐서 영상 생성 (이미지 고정, 음악 길이에 맞춤)
    command = [
        'ffmpeg',
        '-loop', '1',
        '-i', image_path,
        '-i', audio_path,
        '-c:v', 'libx264',
        '-tune', 'stillimage',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-pix_fmt', 'yuv420p',
        '-shortest',
        output_path
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return jsonify({'error': '영상 생성 중 오류가 발생했습니다.', 'detail': str(e)}), 500

    # 생성된 영상 반환
    return send_file(output_path, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
