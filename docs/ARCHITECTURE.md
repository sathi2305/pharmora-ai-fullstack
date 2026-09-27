# Architecture
Component Diagram: Client Next.js PWA -> API Gateway FastAPI -> Core Services (User, Medicine, KG Neo4j, Simulation Celery, Medi RAG, Health) -> Data Layer Postgres Neo4j Qdrant Redis -> External DrugBank PharmGKB ABDM

Data Flow: Signup->Firebase verify->Create User+HealthProfile JSONB->Dashboard; Add Meds->Search FTS+Neo4j->KG cascade query->Celery SciPy ODE->Risk%+path->Medi explanation; Chat->Whisper STT->Qdrant RAG->Streaming LLM->TTS; Health->Wearable->Timescale->Anomaly->Correlate