from PIL import Image
import torch
import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from dotenv import load_dotenv

# Load environment variables (if any)
load_dotenv()

# Load BLIP caption model and processor
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

# Caption generation function
def generate_caption(image: Image.Image):
    inputs = caption_processor(images=image, return_tensors="pt")
    output = caption_model.generate(**inputs)
    caption = caption_processor.decode(output[0], skip_special_tokens=True).strip()
    return caption

# Gradio UI
interface = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="🧠 Generated Caption"),
    title="🖼️ AI Image Caption Generator",
    description="Upload an image and let AI generate a smart caption using BLIP."
)

if __name__ == "__main__":
    interface.launch()
