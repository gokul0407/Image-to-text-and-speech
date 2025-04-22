# from flask import Flask, render_template, request, redirect, url_for
# from werkzeug.utils import secure_filename
# import os
# from utils.image_processing import preprocess_image
# from utils.ocr_utils import extract_text, text_to_speech

# app = Flask(__name__)

# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         return redirect(request.url)
#     file = request.files['file']
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         preprocessed_image = preprocess_image(filepath)
#         extracted_text = extract_text(preprocessed_image)

#         audio_path = text_to_speech(extracted_text)

#         if audio_path:
#             return render_template('index.html', text=extracted_text, audio_path=audio_path)
#         else:
#             return render_template('index.html', error="No text found to convert to speech.")
#     else:
#         return render_template('index.html', error="Invalid file type. Please upload a PNG, JPG, or JPEG image.")

# if __name__ == "__main__":
#     if not os.path.exists(app.config['UPLOAD_FOLDER']):
#         os.makedirs(app.config['UPLOAD_FOLDER'])
#     app.run(debug=True)



from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from utils.image_processing import preprocess_image
from utils.ocr_utils import extract_text, text_to_speech
import logging

# Setup logging for debugging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Configure upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Ensure uploads folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Check if file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if file is part of request
    if 'file' not in request.files:
        logging.error("No file part in the request")
        return redirect(request.url)

    file = request.files['file']
    
    # If file is valid, process it
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            # Save the uploaded image
            file.save(filepath)
            logging.debug(f"File saved at: {filepath}")

            # Preprocess the image
            preprocessed_image = preprocess_image(filepath)
            logging.debug(f"Preprocessed image: {preprocessed_image}")

            # Extract text from the image
            extracted_text = extract_text(preprocessed_image)
            logging.debug(f"Extracted Text: {extracted_text}")

            # Convert text to speech
            audio_path = text_to_speech(extracted_text)
            
            if audio_path:
                return render_template('index.html', text=extracted_text, audio_path=audio_path)
            else:
                logging.error("No text found to convert to speech.")
                return render_template('index.html', error="No text found to convert to speech.")
        
        except Exception as e:
            logging.error(f"Error processing the image: {e}")
            return render_template('index.html', error="There was an error processing the image.")
    
    else:
        logging.error("Invalid file type or no file selected.")
        return render_template('index.html', error="Invalid file type. Please upload a PNG, JPG, or JPEG image.")

if __name__ == "__main__":
    app.run(debug=True)
