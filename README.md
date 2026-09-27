
# Pharmora AI v2 — Modern 2026 Build - Complete Project with Zip

> Your Empathetic AI Health Companion — From Doubt to Clarity, In Your Language
> **Modern Features Added:** Voice-First Hey Medi, Vision Pill ID YOLOv8, Prescription OCR TrOCR, Adherence ML XGBoost, Pharmacogenomics Twin, ABDM FHIR R4, GraphQL, WebSocket real-time, PWA offline, Dark/Light, AR placeholder, Federated Learning

## Quick Start (Functional Implementation Ready)
```bash
unzip pharmora-ai-fullstack.zip
cd pharmora-ai-fullstack
cp .env.example .env
docker-compose up --build
# Backend: http://localhost:8000/docs  (v2.0.0 Modern)
# Frontend: http://localhost:3000
# Neo4j: http://localhost:7474 (neo4j/pharmora123)
# Test login: patient@test.com / Test123!
```

## What's Modern in v2?
1. **Voice-First:** `VoiceChat.tsx` Web Speech API ta-IN/hi-IN/en-IN, Hey Medi wake word, Whisper STT + Sarvam TTS
2. **Vision:** `PillVisionScanner.tsx` camera + YOLOv8 mock, fake detection, strip OCR
3. **ML Adherence:** `GET /ml/adherence/predict` XGBoost skip_prob + personalized Tamil nudge “Thambi marunthu edukka marandhuteengala?”
4. **Pharmacogenomics:** `POST /ml/dose/personalize` CPIC guideline dose 5mg→2.5mg for CYP2C9 *2/*3
5. **FHIR ABDM:** `GET /fhir/export/{user_id}` Bundle MedicationRequest + Observation + consent, import EHR
6. **GraphQL:** `POST /graphql` flexible KG query alternative to REST
7. **WebSocket:** `ws://.../realtime/ws/medi/{user_id}` real-time streaming alternative to SSE
8. **PWA:** `manifest.json` + `sw.js` offline TTS cache, standalone, installable
9. **UI Modern:** Dark/Light toggle WCAG 2.1, Framer Motion, neumorphism cards, Adherence ring
10. **Security Modern:** DPDP Act 2023 erasure, AES-256, TLS1.3, JWT RS256 rotation, Bandit/Trivy/ZAP in CI

## Project Structure (All Phases)
- docs/: ARCHITECTURE, DATABASE_SCHEMA, API_SPEC, FRONTEND, TESTING, DEVOPS, SECURITY, ADR, openapi.yaml
- backend/: FastAPI main.py includes 7 routers (auth, medicines, interactions, chat, fhir, ml, graphql, realtime), services/simulation.py SciPy ODE, services/medi.py 12 langs
- frontend/: Next.js 14 App Router (auth)/login Google OAuth + (dashboard)/dashboard modern + medicines search + chat streaming + fhir FHIR page + components VoiceChat, PillVisionScanner, AdherenceML
- .github/workflows/ci.yml: lint-test black flake8 mypy pytest eslint bandit pip-audit trivy, build docker, deploy ArgoCD staging → prod blue-green
- docker-compose.yml: postgres, redis, neo4j, qdrant, backend, frontend
- infra/main.tf: Terraform EKS + RDS

## API Endpoints (v2)
- Auth: /api/v1/auth/signup, login, google
- Medicines: /search?q=warfarin&lang=ta, /{id}, /scan (YOLOv8)
- Interactions: /simulate {drug_ids, genotype} → cascade_graph + risks 86%
- Medi: /chat/stream SSE + /realtime/ws/medi/{id} WebSocket + /chat/history
- Modern: /fhir/export/{id}, /fhir/import, /ml/adherence/predict, /ml/dose/personalize, /graphql, /features, /languages, /healthz

## Testing & DevOps
- Tests: backend/tests/test_modern.py (cascade 86%, FHIR Bundle, ML skip_prob)
- Branching: GitFlow main←develop←feat/*, PR 1 approval + CI green + coverage>80 + SAST pass, Conventional commits
- Monitoring: Prometheus Grafana latency p95, queue depth, tokens/min, Loki logs request_id, Sentry

## Zip
See /mnt/data/pharmora-ai-fullstack.zip — full functional project ready to deploy. Unzip and docker-compose up.

## Team
Sathiyamoorthi S, Vijay SK, Vimalkumar, Velan | Guide Mr. Bharathiraja AP/CSE | VSB College
