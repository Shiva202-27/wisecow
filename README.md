# Wisecow DevOps Deployment - AccuKnox Assessment

## Problem Statement 1

Containerized Wisecow application and deployed on Kubernetes.

### Implemented

- Dockerized Wisecow application
- Kubernetes Deployment
- Kubernetes Service exposure
- TLS enabled using Kubernetes TLS Secret
- NGINX Ingress configured
- GitHub Actions CI/CD pipeline
- Docker image build and push automation

## Tech Stack

- Docker
- Kubernetes
- Minikube
- GitHub Actions
- NGINX Ingress
- TLS

## Kubernetes Files

Located in:

k8s/

- deployment.yaml
- service.yaml
- ingress.yaml


## Problem Statement 2

Automation scripts:

1. System Health Monitoring Script
   - CPU monitoring
   - Memory monitoring
   - Disk monitoring
   - Alert logging

2. Application Health Checker
   - HTTP status check
   - Detects application UP/DOWN


## Problem Statement 3

KubeArmor Zero Trust Policy

Implemented:

- KubeArmor security policy
- Runtime workload monitoring
- Policy proof screenshot added


## Deployment

Apply manifests:

kubectl apply -f k8s/


Check:

kubectl get pods
kubectl get svc
kubectl get ingress