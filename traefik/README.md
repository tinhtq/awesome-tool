# Install

```bash
helm repo add traefik https://helm.traefik.io/traefik
helm repo update
helm install --create-namespace traefik traefik/traefik -n traefik -f values.yml
```

## Convert SSL certificate to secret in Kubernetes

Put the cert and key file for SSL (.crt and .key) into this directory and run below command

```bash
python3 convert-ssl-to-secrets.py
```
