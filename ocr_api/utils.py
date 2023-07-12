import numpy as np
from os import mkdir
import PIL.Image as Image
from io import BytesIO
import cv2


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