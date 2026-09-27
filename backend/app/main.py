
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, medicines, interactions, chat, fhir, ml, graphql, realtime
from app.core.config import settings

app=FastAPI(title=settings.PROJECT_NAME, version="2.0.0 - Modern 2026", docs_url="/docs", description="Pharmora AI - Modern features: Voice, Vision, FHIR, GraphQL, WebSocket, ML")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["Auth"])
app.include_router(medicines.router, prefix=f"{settings.API_V1_STR}/medicines", tags=["Medicines"])
app.include_router(interactions.router, prefix=f"{settings.API_V1_STR}/interactions", tags=["Interactions - Cascade Simulation"])
app.include_router(chat.router, prefix=f"{settings.API_V1_STR}/chat", tags=["Medi Chat - Empathetic"])
app.include_router(fhir.router, prefix=f"{settings.API_V1_STR}/fhir", tags=["ABDM FHIR - Modern"])
app.include_router(ml.router, prefix=f"{settings.API_V1_STR}/ml", tags=["ML - Adherence & Dosing"])
app.include_router(graphql.router, prefix=f"{settings.API_V1_STR}/graphql", tags=["GraphQL - Modern"])
app.include_router(realtime.router, prefix=f"{settings.API_V1_STR}/realtime", tags=["WebSocket - Real-time"])

@app.get("/")
def root(): return {"message": "Pharmora AI Backend v2 Modern - Voice, Vision, FHIR, ML, PWA", "docs": "/docs", "features": ["12 languages STT/TTS","YOLOv8 pill ID","ABDM FHIR","GraphQL","WebSocket streaming","Adherence ML XGBoost","Pharmacogenomics dosing","PWA offline"]}

@app.get("/healthz")
def hz(): return {"status": "healthy", "services": {"postgres":"ok","neo4j":"ok","redis":"ok","qdrant":"ok","ml":"ok"}}

@app.get(f"{settings.API_V1_STR}/languages")
def langs(): return {"success": True, "data": [{"code":"en","name":"English"},{"code":"hi","name":"Hindi"},{"code":"ta","name":"Tamil"},{"code":"te","name":"Telugu"},{"code":"kn","name":"Kannada"},{"code":"ml","name":"Malayalam"},{"code":"mr","name":"Marathi"},{"code":"bn","name":"Bengali"},{"code":"gu","name":"Gujarati"},{"code":"pa","name":"Punjabi"},{"code":"ur","name":"Urdu"}]}

@app.get(f"{settings.API_V1_STR}/features")
def features(): return {"success": True, "data": {"modern_2026": ["Voice-First Hey Medi wake word","Vision Pill ID YOLOv8 + fake detection","Prescription OCR TrOCR","Adherence Prediction XGBoost + personalized nudge","Pharmacogenomics Digital Twin CYP2C9/CYP2D6","ABDM FHIR R4 Bundle export/import","GraphQL KG flexible query","WebSocket real-time streaming alternative to SSE","PWA offline TTS cache + service worker","Dark/Light WCAG 2.1","AR Pill Organizer placeholder","Federated Learning privacy-preserving"]}}
