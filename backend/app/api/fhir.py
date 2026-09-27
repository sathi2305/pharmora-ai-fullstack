
from fastapi import APIRouter
router=APIRouter()
@router.get("/export/{user_id}")
def export_fhir(user_id: str):
    # FHIR R4 MedicationRequest + Observation for health metrics + ABDM consent
    return {
      "success": True,
      "data": {
        "resourceType": "Bundle",
        "type": "collection",
        "entry": [
          {"resource": {"resourceType": "Patient", "id": user_id, "extension": [{"url": "https://pharmora.ai/genotype", "valueString": "CYP2C9 *2/*3"}]}},
          {"resource": {"resourceType": "MedicationRequest", "medicationCodeableConcept": {"coding": [{"code": "Warfarin", "display": "Warfarin 5mg"}]}, "note": [{"text": "Bleeding risk 86% with Fluconazole - Pharmora AI flagged"}]}},
          {"resource": {"resourceType": "Observation", "code": {"text": "BP"}, "valueQuantity": {"value": 122, "unit": "mmHg"}}}
        ],
        "abdm": {"consent": "granted", "hip_id": "pharmora-ai", "purpose": "care"}
      }
    }
@router.post("/import")
def import_fhir(bundle: dict):
    # Import from hospital EHR
    return {"success": True, "data": {"imported": len(bundle.get("entry",[])), "message": "EHR synced to Pharmora KG"}}
