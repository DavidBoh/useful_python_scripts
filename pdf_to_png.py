import os
from pdf2image import convert_from_path

def pdf_to_images(pdf_path, output_dir):
  os.makedirs(output_dir, exist_ok=True)

  images = convert_from_path(pdf_path)

  #save each image as png
  for i, image in enumerate(images):
    output_path = os.path.join(output_dir, f"page_{i+1}".png")
    image.save(output_path, "PNG")
    print(f"Saved {output_path}")

#provide PDF path and output dir

pdf_path = "path/file.pdf"
output_dir = "."

pdf_to_images(pdf_path,output_dir)
