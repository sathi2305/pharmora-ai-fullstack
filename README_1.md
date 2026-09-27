# Pharmora AI — Complete Software Project: Concept to Implementation

> **Your Empathetic AI Health Companion — From Doubt to Clarity, In Your Language**
> Built as per structured SDLC: purpose → architecture → schema → API → frontend → testing → DevOps → security

## 1. Purpose, Target Users, Core Requirements
**Purpose:** Democratize medicine literacy. Replace static pairwise checkers with dynamic cascade simulation + empathetic multilingual LLM (Medi).
- Problem: 60% elderly on 5+ meds, exponential interaction, CYP450 shared-enzyme cascade missed, 88% Indians uncomfortable English, 50% non-adherence due to fear.
**Target Users:** Chronic patients 220M, Elderly+caregiver, Pharmacists, Doctors ABDM, Rural health workers.
**Core Functional:** Auth (email+Google OAuth), Dashboard (health score, adherence ring, alerts), Medi chat (voice/text 12 langs streaming), Medicine DB 15K drugs, Interaction engine (Neo4j + SciPy ODE), Health indicators (wearable+lab OCR), Vision pill ID YOLOv8, Pharmacogenomics twin.
**Non-Functional:** p95 <200ms API, <2s simulation 5 drugs, 99.9% uptime, scale 1M K8s, DPDP Act 2023 + HIPAA, WCAG 2.1 AA mobile-first PWA.

## 2. Tech Stack Justification
- Frontend: Next.js 14 App Router, React 18, Tailwind, shadcn/ui, Zustand, Cytoscape.js, Framer Motion — SSR SEO for medicine pages, ISR, team React expertise, PWA offline for rural.
- Backend: FastAPI Python + Node microservice realtime chat — Python needed SciPy + ML, FastAPI fastest async auto OpenAPI.
- DB: PostgreSQL 15 (users, meds, adherence, metrics), Neo4j 5 (KG 1.2M edges Drug-[:INHIBITS]->Enzyme), Redis (cache/session/rate limit), Qdrant (vector RAG multilingual-e5).
- AI: Llama 3.1 70B fine-tuned + GPT-4o fallback, LangChain RAG, Whisper large-v3 STT 90+ langs, Coqui XTTS + Sarvam AI TTS Indic voice, YOLOv8 pill, TrOCR prescription.
- Infra: Docker, K8s EKS, GitHub Actions, RDS + Neo4j Aura, CloudFront CDN, Prometheus Grafana Loki Sentry.

## 3. Architecture
Component Diagram: Client PWA -> API Gateway FastAPI Kong -> Core Services User/Medicine/KG/Simulation Celery/Medi RAG/Health/Multilingual -> Data Layer Postgres Neo4j Qdrant Redis -> External DrugBank PharmGKB KEGG FDA FAERS ABDM FHIR.
Data Flow: Signup Firebase Google verify -> Create User HealthProfile JSONB -> Dashboard. Add Meds Search FTS Neo4j fuzzy -> KG query MATCH (d)-[METABOLIZED_BY|INHIBITS]->(e)<-[:METABOLIZED_BY]-(other) -> Celery SciPy ODE dC/dt = -Vmax*C/(Km+C)*inhibition_factor -> Risk%+path -> Medi empathetic Tamil. Chat Whisper->Lang detect->Qdrant RAG->Streaming LLM->TTS. Health Wearable->TimescaleDB->Anomaly z-score->Correlate meds.

## 4. Database Schema
Postgres DDL in backend/app/models/schema.sql and docs/DATABASE_SCHEMA.md. Indexes: GIN fts, BTREE user+measured_at DESC, IVFFLAT embedding. Neo4j schema Drug-[:METABOLIZED_BY {km,vmax}]->Enzyme, Drug-[:INHIBITS {ki}]->Enzyme, Gene-[:ENCODES {activity}]->Enzyme, Drug-[:CAUSES]->AdverseEvent.

## 5. API Specification
See docs/API_SPEC.md and openapi.yaml. All responses {success,data,error,meta}. Auth Bearer JWT RS256 15m refresh 7d rotation + Google OAuth Firebase Admin SDK. Rate limit 100/min IP Redis sliding window. Endpoints: /auth/signup|login|google, /medicines/search, /medicines/{id}, /medicines/scan, /user/medicines, /interactions/simulate, /chat/stream SSE, /health/metrics.

## 6. Frontend Component Hierarchy
See docs/FRONTEND.md. Zustand stores useAuthStore, useMedicineStore, useChatStore, useHealthStore, useLanguageStore + React Query server cache optimistic updates. Dynamic import Cytoscape heavy, next/image, ISR 1h, PWA offline cache TTS.

## 7. Testing Strategy
See docs/TESTING.md. Unit Pytest+Jest 80%, Integration TestContainers Postgres Neo4j Redis, E2E Playwright scenarios: Signup Tamil Add Warfarin+Fluconazole 86% bleeding Ask Medi Tamil, Scan pill Dolo, Upload lab PDF OCR.

## 8. DevOps
Branching GitFlow main<-develop<-feat/*. PR needs 1 review+CI green+coverage>80%+SAST pass. CI/CD .github/workflows/ci.yml lint-test black isort flake8 mypy pytest eslint prettier npm test bandit npm audit trivy fs, build docker ghcr.io/pharmora, deploy develop->staging EKS ArgoCD, main->prod blue-green approval. Environments dev docker-compose, staging EKS t3.medium RDS, prod EKS m5.large autoscale 3-20 CloudFront WAF daily backup. Monitoring Prometheus Grafana latency p95 queue depth tokens/min, Loki JSON logs request_id, Sentry, /healthz. IaC Terraform infra/.

## 9. Security Hardening
See docs/SECURITY.md. Pydantic strict, image magic byte 10MB ClamAV, PDF 20MB, AES-256 pgcrypto at rest S3 SSE TLS1.3 HSTS, JWT RS256 bcrypt12, RBAC patient caregiver pharmacist doctor admin, SAST Bandit Semgrep, pip-audit npm audit, Trivy CRITICAL fail, ZAP DAST nightly, DPDP consent erasure DELETE /user/data, audit log immutable, Medi guardrails system prompt not doctor never diagnose consult doctor cite sources confidence<0.6 escalate.

## 10. Quick Start
```bash
git clone https://github.com/pharmora-ai/pharmora.git
cd pharmora-ai-fullstack
cp .env.example .env
docker-compose up --build
# Backend http://localhost:8000/docs
# Frontend http://localhost:3000
# Neo4j http://localhost:7474
```
Test: patient@test.com / Test123!

## 11. Living README & Contribution
Branch feat/* from develop conventional commits, PR template, ADR in docs/adr/, code review protocol: small PR <400 LOC, 1 approval, CI green, coverage not drop, security scan pass.

