# Install K3s without Traefik

```bash
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="server --disable traefik" sh
```

# Install GatewayAPI

```bash
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.0.0/standard-install.yaml
```
