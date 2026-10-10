from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

STATIC_DIRECTORY = Path(__file__).resolve().parent / "static"

app = FastAPI(
    title="Ergoshear",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
app.mount("/static", StaticFiles(directory=STATIC_DIRECTORY), name="static")


@app.get("/", response_class=FileResponse, include_in_schema=False)
def homepage() -> FileResponse:
    return FileResponse(STATIC_DIRECTORY / "index.html", media_type="text/html")


@app.get("/healthz")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
