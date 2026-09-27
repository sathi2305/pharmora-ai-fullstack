from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from ..services.medi import generate_medi_response
import time
router=APIRouter()
class ChatReq(BaseModel):
    message: str
    language: str="en"
    user_meds: list=[]
    genotype: dict={}
@router.post("/stream")
def stream(req: ChatReq):
    full=generate_medi_response(req.message, req.language, req.user_meds, req.genotype)
    def gen():
        for w in full.split():
            yield f"data: {w} \n\n"
            time.sleep(0.02)
        yield "data: [DONE]\n\n"
    return StreamingResponse(gen(), media_type="text/event-stream")
@router.get("/history")
def hist():
    return {"success": True, "data": []}
