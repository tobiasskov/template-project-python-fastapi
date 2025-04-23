# template-project-python-fastapi

This is a template project for a fastapi based Python API.

## Deployment

**Build and run api:**

```bash
docker build --target "production" --tag "xyz-api" .
docker run --publish 8080:8080 "xyz-api"
```

**Then visit:** [localhost](http://localhost:8080/docs)

## TODO

- Add codegeneration
