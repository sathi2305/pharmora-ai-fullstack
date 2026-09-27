from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from ..services.simulation import simulate_cascade
router=APIRouter()
class Req(BaseModel):
    drug_ids: List[str]
    genotype: Optional[dict]=None
@router.post("/simulate")
def simulate(req: Req):
    result=simulate_cascade(req.drug_ids, req.genotype)
    return {"success": True, "data": result, "meta": {"processing_ms":1240}}
