from flask import Blueprint, request, jsonify, render_template, current_app, send_file
import os
import io
from PIL import Image
import base64
import time

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@main.route('/api/generate', methods=['POST'])
def generate_image():
    """API endpoint to generate images from text prompts"""
    data = request.json
    
    # Get parameters from request
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    
    negative_prompt = data.get('negative_prompt', '')
    height = int(data.get('height', 512))
    width = int(data.get('width', 512))
    num_inference_steps = int(data.get('num_inference_steps', 50))
    guidance_scale = float(data.get('guidance_scale', 7.5))
    
    try:
        # Generate image
        image = current_app.model.generate_image(
            prompt=prompt,
            negative_prompt=negative_prompt,
            height=height,
            width=width,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale
        )
        
        # Save image with timestamp to avoid overwriting
        timestamp = int(time.time())
        save_prompt = prompt.replace(" ", "_").replace("/", "_")[:30]  # Limit length for filename
        filename = f"generated_{timestamp}_{save_prompt}.png"
        output_path = os.path.join(current_app.config['OUTPUT_DIR'], filename)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        current_app.model.save_image(image, output_path)
        
        # Convert image to base64 for response
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return jsonify({
            'success': True,
            'image': img_str,
            'filename': filename
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main.route('/api/images/<filename>', methods=['GET'])
def get_image(filename):
    """Return a generated image by filename"""
    try:
        path = os.path.join(current_app.config['OUTPUT_DIR'], filename)
        return send_file(path, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 404
