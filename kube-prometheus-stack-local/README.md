# Install

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install --create-namespace monitoring prometheus-community/kube-prometheus-stack -n monitoring -f values.yml
```

## Create external scrap_config

When want to create a monitor for an external URL, can add the scrape_config like the below

```yaml
prometheus:
  prometheusSpec:
    additionalScrapeConfigs:
      - job_name: external
        metrics_path: /metrics
        static_configs:
          - targets:
              - <IP>:<PORT>
```
