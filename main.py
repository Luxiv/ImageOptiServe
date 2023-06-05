from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.upload import router as upload_router
from api.download import router as download_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(upload_router)
app.include_router(download_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
