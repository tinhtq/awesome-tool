# Install

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install --create-namespace monitoring prometheus-community/kube-prometheus-stack -n monitoring -f values.yml
```
