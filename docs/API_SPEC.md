# API Spec
POST /api/v1/auth/signup, /login, /google -> access_token
GET /api/v1/medicines/search?q=warfarin&lang=ta
POST /api/v1/medicines/scan (image)
POST /api/v1/user/medicines
POST /api/v1/interactions/simulate {drug_ids} -> {cascade_graph, risks[]}
POST /api/v1/chat/stream {message,language} SSE
GET /api/v1/chat/history
POST /api/v1/health/metrics
Responses {success,data,error,meta}, Bearer JWT, Rate limit 100/min