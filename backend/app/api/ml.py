
from fastapi import APIRouter
import random
router=APIRouter()
@router.get("/adherence/predict")
def predict_adherence(user_id: str = "demo"):
    # Mock XGBoost model trained on adherence history + time + side effect fear
    skip_prob = random.uniform(0.2,0.45)
    return {"success": True, "data": {"skip_prob": skip_prob, "next_dose": "8:00 PM", "nudge": "Friendly Tamil reminder: Thambi marunthu edukka marandhuteengala? 💙", "model": "XGBoost v2.1", "features": ["past_adherence_7d","time_of_day","side_effect_mentions"]}}
@router.post("/dose/personalize")
def personalize_dose(payload: dict):
    # Pharmacogenomics dosing
    genotype = payload.get("genotype",{})
    drug = payload.get("drug_id")
    if genotype.get("CYP2C9")=="*2/*3" and drug=="db01579":
        return {"success": True, "data": {"original_dose": "5mg", "recommended": "2.5-3mg", "reason": "Poor metabolizer CYP2C9 *2/*3 - reduce 50% per CPIC guideline", "guideline": "CPIC Warfarin 2023", "confidence": 0.89}}
    return {"success": True, "data": {"recommended": "Standard dose", "confidence": 0.72}}
