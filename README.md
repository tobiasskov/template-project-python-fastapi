# template-project-python-fastapi

This is a template project for a fastapi based Python API.

## Highlights

- Dev container with named volumes for pre-commit + uv caches and venv.
- Multistage dockerfile with optimized production environment with minimal layers and non-root non-sudo user

## Deployment

**Build and run api:**

```bash
docker build --target "production" --tag "xyz-api" .
docker run --publish 8080:8080 "xyz-api"
```

**Then visit:** [localhost](http://localhost:8080/docs)

## TODO

- Add property based testing for simulation type logic
- SQLite
