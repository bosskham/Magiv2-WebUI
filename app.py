import gradio as gr
import torch
from transformers import AutoModel
from PIL import Image
import numpy as np

# Load the model from HuggingFace with trust_remote_code
model = AutoModel.from_pretrained("ragavsachdeva/magiv2", trust_remote_code=True).eval()

# Function to read and process images
def read_image(path_to_image):
    with open(path_to_image, "rb") as file:
        image = Image.open(file).convert("L").convert("RGB")
        image = np.array(image)
    return image

# Function to perform predictions and generate the transcript
def generate_transcript(chapter_pages, character_images, character_names, do_ocr=True):
    chapter_pages = [read_image(x) for x in chapter_pages]
    character_bank = {
        "images": [read_image(x) for x in character_images],
        "names": character_names
    }

    with torch.no_grad():
        per_page_results = model.do_chapter_wide_prediction(chapter_pages, character_bank, use_tqdm=True, do_ocr=do_ocr)

    transcript = []
    for i, (image, page_result) in enumerate(zip(chapter_pages, per_page_results)):
        model.visualise_single_image_prediction(image, page_result, f"page_{i}.png")
        speaker_name = {
            text_idx: page_result["character_names"][char_idx] for text_idx, char_idx in page_result["text_character_associations"]
        }
        for j in range(len(page_result["ocr"])):
            if not page_result["is_essential_text"][j]:
                continue
            name = speaker_name.get(j, "unsure")
            transcript.append(f"<{name}>: {page_result['ocr'][j]}")
    
    return "\n".join(transcript)

# Gradio Web UI
def webui():
    with gr.Blocks() as demo:
        gr.Markdown("# Magiv2 WebUI")

        # File upload components
        chapter_pages = gr.File(label="Upload Chapter Pages", type="filepath", file_count="multiple", file_types=[".png", ".jpg"])
        character_images = gr.File(label="Upload Character Images", type="filepath", file_count="multiple", file_types=[".png", ".jpg"])
        character_names = gr.Textbox(label="Enter Character Names (comma-separated)", placeholder="e.g., Luffy, Sanji, Zoro, Ussop")

        # Toggle for OCR
        ocr_toggle = gr.Checkbox(label="Enable OCR", value=True)

        # Output component
        transcript_output = gr.Textbox(label="Generated Transcript", lines=10)

        # Define the action on button click
        def on_generate_transcript(chapter_pages, character_images, character_names, do_ocr):
            names_list = [name.strip() for name in character_names.split(",")]
            return generate_transcript(chapter_pages, character_images, names_list, do_ocr)

        # Button to trigger transcript generation
        generate_button = gr.Button("Generate Transcript")
        generate_button.click(on_generate_transcript, [chapter_pages, character_images, character_names, ocr_toggle], transcript_output)

    demo.launch()

if __name__ == "__main__":
    webui()
