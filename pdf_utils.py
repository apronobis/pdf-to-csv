from pdf2image import convert_from_path
from PIL import Image
import os  

def crop_pdf_images(pdf_path, output_folder):
    # Make sure the output folder exists, if not, create it  
    if not os.path.exists(output_folder):  
        os.makedirs(output_folder)  

    # Path to Poppler's bin (only necessary if Poppler is not in your PATH)  
    poppler_path = 'poppler/bin'  # Adjust this for your Poppler path  

    # Convert PDF to images  
    pages = convert_from_path(pdf_path, 300, poppler_path=poppler_path)  # 300 is the DPI  

    # Save each page as an image file  
    for i, page in enumerate(pages):  
        image_path = os.path.join(output_folder, f'{i + 1}.jpg')
        img = Image.new('RGB', (4800, 400), 'white')
        img.paste(page.crop((100, 1525, 4900, 1720)), (115, 100))
        img.save(image_path, 'JPEG')  

    print(f'PDF converted to images, cropped and saved in {output_folder}')