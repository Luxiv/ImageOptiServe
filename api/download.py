from fastapi import Query, APIRouter
from models.image import Image
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/download/{image_id}")
async def download_image(image_id: int, quality: int = Query(default=75, ge=25, le=100)):
    """
    Downloads an optimized image by ID and specified quality level.

    :param image_id: The ID of the image to download.
    :param quality: The desired quality level of the image (default: 75).
    :return: The downloaded image file as a response.
    """
    if quality not in [75, 50, 25]:
        return {"message": "Image should have next quality:75/50/25"}

    image = Image(
        id=image_id,
        path=f"X:/ImageOptiServe/static/images/{quality}percent/{image_id}.jpeg",
        quality=quality
    )

    return FileResponse(image.path, media_type="image/jpeg")
