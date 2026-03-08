# Marvin Galdamez Skills API

A simple FastAPI application to serve skill profile data.

## Endpoints

- `GET /v1/profile/skills`: Returns the skill profile in JSON format.
- `GET /health`: Health check endpoint.

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API:
   [http://localhost:8000/v1/profile/skills](http://localhost:8000/v1/profile/skills)

## Docker

Build the image:
```bash
docker build -t ghcr.io/mgaldamez/api-skills:latest .
```

Push to registry:
```bash
docker push ghcr.io/mgaldamez/api-skills:latest
```

## Kubernetes (FluxCD)

The manifests are located in the `k8s/` directory.

### Configuration
- **Ingress**: Configured for `api.mgaldamez.dev`. 
- **TLS**: SSL/TLS is handled by Cloudflare (offloaded). The Ingress is configured for HTTP traffic.

### FluxCD Integration
FluxCD can be configured to watch this repository and apply the manifests using Kustomization.
The `k8s/kustomization.yaml` file specifies the resources to be applied.
