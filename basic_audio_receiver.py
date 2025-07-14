import os
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    current_time = datetime.now()

    # Format the datetime into a string (e.g., 20250709_215958)
    # You can customize this format using strftime directives.
    # %Y: Year with century (e.g., 2025)
    # %m: Month as a zero-padded decimal number (01-12)
    # %d: Day of the month as a zero-padded decimal number (01-31)
    # %H: Hour (24-hour clock) as a zero-padded decimal number (00-23)
    # %M: Minute as a zero-padded decimal number (00-59)
    # %S: Second as a zero-padded decimal number (00-59)
    datetime_str = current_time.strftime("%Y%m%d_%H%M%S")

    # Save the uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename.replace(".wav", f"-{datetime_str}.wav"))
    file.save(filepath)
    
    return jsonify({'message': 'File processed successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030)