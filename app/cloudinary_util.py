import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()
def configure_cloudinary():
    cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key=os.getenv('CLOUDINARY_API_KEY'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET')
    )

def upload_image_cloudinary(file):
    resultado = cloudinary.uploader.upload(file)
    return resultado['url'] if resultado else None
