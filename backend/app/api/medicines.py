from fastapi import APIRouter, Query
router=APIRouter()
MOCK=[{"id":"db01579","brand_name":"Warfarin","generic_name":"Warfarin","composition":["Warfarin 5mg"],"manufacturer":"Cipla","mrp":45.5,"atc_code":"B01AA03","description":"Anticoagulant"}, {"id":"db00285","brand_name":"Fluconazole","generic_name":"Fluconazole","composition":["Fluconazole 150mg"],"manufacturer":"Sun","mrp":89.0,"atc_code":"J02AC01","description":"Antifungal CYP2C9 inhibitor"}, {"id":"db01234","brand_name":"Dolo 650","generic_name":"Paracetamol","composition":["Paracetamol 650mg"],"manufacturer":"Micro Labs","mrp":28.0,"atc_code":"N02BE01","description":"Analgesic"}]
@router.get("/search")
def search(q: str=Query(..., min_length=1), lang: str="en", limit: int=20):
    results=[m for m in MOCK if q.lower() in m["brand_name"].lower() or q.lower() in m["generic_name"].lower()]
    return {"success": True, "data": results[:limit]}
@router.get("/{med_id}")
def get_one(med_id: str, lang: str="en"):
    med=next((m for m in MOCK if m["id"]==med_id), None)
    if not med: return {"success": False}
    return {"success": True, "data": {**med, "side_effects": ["Bleeding"], "alternatives": [{"brand_name": "Generic Warfarin", "saving_percent":40}]}}
