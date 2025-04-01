import os
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import io

class TextToImageModel:
    def __init__(self, model_id="runwayml/stable-diffusion-v1-5"):
        self.model_id = model_id
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipe = None
        self.load_model()

    def load_model(self):
        """Load the Stable Diffusion model"""
        print(f"Loading model {self.model_id} on {self.device}...")
        
        # Check if CPU is being used and adjust settings accordingly
        if self.device == "cpu":
            self.pipe = StableDiffusionPipeline.from_pretrained(
                self.model_id,
                torch_dtype=torch.float32
            )
        else:
            self.pipe = StableDiffusionPipeline.from_pretrained(
                self.model_id,
                torch_dtype=torch.float16
            ).to(self.device)
        
        # Enable attention slicing to reduce memory usage
        self.pipe.enable_attention_slicing()
        print("Model loaded successfully!")

    def generate_image(self, prompt, negative_prompt="", height=512, width=512, 
                       num_inference_steps=50, guidance_scale=7.5):
        """Generate an image from a text prompt"""
        if not self.pipe:
            raise ValueError("Model has not been loaded. Call load_model() first.")
        
        print(f"Generating image for prompt: {prompt}")
        
        # Generate image
        image = self.pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            height=height,
            width=width,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale
        ).images[0]
        
        return image

    def save_image(self, image, output_path):
        """Save the generated image to a file"""
        image.save(output_path)
        return output_path

    def image_to_bytes(self, image):
        """Convert PIL Image to bytes for sending over HTTP"""
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        return img_byte_arr.getvalue()
