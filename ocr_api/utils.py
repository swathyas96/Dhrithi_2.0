import numpy as np
from os import mkdir
import PIL.Image as Image
from io import BytesIO
from pdf2image import convert_from_bytes
import cv2
from core.settings import BASE_DIR
from pdf2docx import Converter
from os.path import isfile


def save_image_from_in_memory_image(image: any, filename: any, file_type: any) -> None:
    """
    Saves an image from in-memory data to the specified directory.

    Args:
        image: The in-memory image data.
        filename: The filename for the saved image.
        file_type: The file type or extension of the image.

    Raises:
        OSError: If the folder creation fails.

    Returns:
        None
    """
    image = Image.open(BytesIO(bytearray(image)))
    try:
        mkdir(f"media/pdf2img/{filename.strip(f'.{file_type}')}")
    except OSError as e:
        print("Couldn't create folder", e)
    cv2.imwrite(
        f"media/pdf2img/{filename.strip(f'.{file_type}')}/{0}.png", np.array(image)
    )
    return image


# Convert PDF to Images
def pdf_to_images(pdf_file: any, filename: str) -> any:
    """
    Converts a PDF file into a list of images.

    Args:
        pdf_file: The PDF file to be converted.

    Returns:
        A list of images extracted from the PDF file.
    """
    images = convert_from_bytes(pdf_file)
    for i in range(len(images)):
        try:
            mkdir(f"documents/pdf2image/{filename}")
        except:
            pass
        cv2.imwrite(f"documents/pdf2image/{filename}/{i}.png", np.array(images[i]))
    return images


def get_image_from_path(filename: str) -> any:
    image = cv2.imread(filename)
    return image


def convert_pdf_to_docx(filename: any) -> None:
    print(str(BASE_DIR) + filename)
    # convert pdf to docx
    print(isfile(str(BASE_DIR) + filename))
    cv = Converter(str(BASE_DIR) + filename)
    filename = filename.replace(".pdf", ".docx").replace("PDF", "Doc")
    # all pages by default
    cv.convert(str(BASE_DIR) + filename)
    cv.close()
