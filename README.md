# Ergoshear website

A lightweight FastAPI landing page for **ergoshear.dev**, with responsive
styling, no JavaScript or external assets, and a JSON health endpoint.

## Run with Docker

```sh
docker build -t ergoshear-website .
docker run --rm -p 8000:8000 ergoshear-website
```

Open <http://localhost:8000>. The container runs as a non-root user and includes
a health check at `/healthz`, which returns `{"status":"ok"}`.

Point the domain's DNS to your hosting server and configure your HTTPS reverse
proxy to forward requests to port 8000. TLS and DNS are managed outside this
application.

## Local development

Use Python 3.10 or newer:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt '.[dev]'
uvicorn app.main:app --reload
```

## Validation

```sh
ruff check .
ruff format --check .
yamllint .
python -m unittest discover -s tests -v
```

Runtime dependencies are pinned in [requirements.txt](requirements.txt).
After changing dependencies in [pyproject.toml](pyproject.toml), regenerate
the pins with `uv pip compile pyproject.toml --python-version 3.13 -o requirements.txt`.

The GitHub Actions workflow runs lint checks and tests, builds the Docker image,
and smoke-tests it on pull requests. Builds on `main` and version tags publish
to `ghcr.io/ergoshear/frontend-website`. API documentation endpoints are disabled
because this application serves a website, not a public API.