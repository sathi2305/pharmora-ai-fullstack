# DevOps
Branching GitFlow main<-develop<-feat/*
CI/CD .github/workflows/ci.yml lint-test black isort flake8 mypy pytest eslint npm test bandit trivy, build docker ghcr.io/pharmora, deploy develop->staging EKS ArgoCD main->prod blue-green
Envs dev docker-compose, staging EKS t3.medium RDS, prod EKS m5.large autoscale 3-20 CloudFront WAF daily backup
Monitoring Prometheus Grafana latency queue tokens, Loki logs, Sentry, /healthz
IaC Terraform /infra