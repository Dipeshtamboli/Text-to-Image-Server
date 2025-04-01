Here is the full content for your `README.md` file:


# Text-to-Image Generator Server

## Project Title
**Text-to-Image Generator Server**

## Description
This project hosts a server that utilizes a text-to-image model (Stable Diffusion) to generate high-quality images based on user-provided text prompts. It includes a Flask backend API, a web interface for user interaction, and Docker support for easy deployment.

---

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Docker Setup](#docker-setup)
6. [Folder Structure](#folder-structure)
7. [Troubleshooting](#troubleshooting)

---

## Features
- Generate images from text prompts using Stable Diffusion.
- Advanced options for image customization:
  - Negative prompts.
  - Adjustable width, height, guidance scale, and inference steps.
- Web interface for easy interaction.
- REST API for programmatic access.
- Dockerized deployment for portability.

---

## Requirements

### Hardware
- **GPU**: Recommended for faster image generation (e.g., NVIDIA GPU with CUDA support).
- **CPU**: Supported but slower.

### Software
- Python 3.10 or later.
- Docker (optional for containerized deployment).

### Dependencies
The following Python libraries are required:
- `Flask`
- `torch`
- `diffusers`
- `transformers`
- `Pillow`
- `accelerate`
- `python-dotenv`

---

## Installation

### Step 1: Clone the Repository
```
git clone https://github.com/your-repo/text-to-image-server.git
cd text-to-image-server
```

### Step 2: Set Up a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

### Step 3: Install Dependencies
```
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the root directory with the following content:
```
SECRET_KEY=your-secret-key-here
MODEL_ID=runwayml/stable-diffusion-v1-5
OUTPUT_DIR=app/static/images/generated
```

### Step 5: Run the Application
```
python run.py
```

Access the web interface at **http://128.46.202.226:31001**.

---

## Usage

### Web Interface
1. Open your browser and navigate to **http://128.46.202.226:31001**.
2. Enter a text prompt in the input field.
3. Customize advanced options (optional).
4. Click the "Generate Image" button.
5. View the generated image and download it if desired.

### API Endpoint
You can also interact with the server programmatically via the REST API:

#### Generate Image (POST)
```
curl -X POST http://localhost:5000/api/generate \
-H "Content-Type: application/json" \
-d '{
    "prompt": "A sunset over mountains",
    "negative_prompt": "",
    "height": 512,
    "width": 512,
    "num_inference_steps": 50,
    "guidance_scale": 7.5
}'
```
The response will include the generated image in base64 format.

---

## Access the Application
Visit **http://128.46.202.226:31001** in your browser.

---

## Folder Structure

```
text-to-image-server/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css         # Web interface styling.
│   │   ├── js/
│   │   │   └── main.js           # Frontend logic.
│   │   └── images/
│   │       └── generated/        # Directory for generated images.
│   ├── templates/
│   │   └── index.html            # Web interface HTML template.
│   ├── __init__.py               # Flask app initialization.
│   ├── routes.py                 # API endpoints and routes.
│   └── model.py                  # Stable Diffusion model handler.
├── docker/
│   ├── Dockerfile                # Docker instructions for building the container.
│   └── docker-compose.yml        # Docker Compose configuration.
├── .env                          # Environment variables file.
├── config.py                     # Application configuration settings.
├── requirements.txt              # Python dependencies list.
├── run.py                        # Application entry point.
└── README.md                     # Documentation file (this file).
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: Slow Image Generation on CPU  
**Solution:** Use a machine with an NVIDIA GPU and CUDA support for faster processing.

#### Issue: Missing Dependencies  
**Solution:** Ensure all dependencies are installed using `pip install -r requirements.txt`.

#### Issue: Permission Denied When Running Docker  
**Solution:** Run Docker commands with elevated privileges (`sudo` on Linux).

#### Issue: Model Not Loading  
**Solution:** Verify that the model ID in `.env` is correct (`runwayml/stable-diffusion-v1-5`).

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

Special thanks to:
- Hugging Face for providing Stable Diffusion tools.
- The Flask community for their excellent web framework.

For questions or contributions, please open an issue on GitHub.
