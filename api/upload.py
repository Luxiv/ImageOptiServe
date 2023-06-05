from fastapi import UploadFile, APIRouter
from pathlib import Path
from models.image import Image
from queues.optimizer import send_image_to_queue
from utils.image_optimizer import unique_id_gen

router = APIRouter()

image_path = Path("X:/ImageOptiServe/static/images/original/")


@router.post("/upload")
async def upload_image(file: UploadFile):
    """
    Uploads an image and sends it for optimization via a queue.

    :param file: The uploaded image file.
    :return: A message indicating a successful upload.
    """
    image_id = unique_id_gen(image_path)

    image = Image(
        id=image_id,
        path=f"{image_path}/{image_id}.jpeg",
        quality=100
    )

    await file.seek(0)
    with open(image.path, "wb") as f:
        f.write(await file.read())

    send_image_to_queue(image.path)

    return {"message": "Image uploaded successfully"}
