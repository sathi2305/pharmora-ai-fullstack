
# Modern GraphQL alternative to REST for medicine KG - Strawberry GraphQL
from fastapi import APIRouter
router=APIRouter()
# In prod: import strawberry
@router.post("/")
def graphql_query(query: dict):
    # Mock GraphQL resolver for KG
    q = query.get("query","")
    if "medicines" in q:
        return {"data": {"medicines": [{"id":"db01579","brand_name":"Warfarin","interactions":[{"enzyme":"CYP2C9","risk":86}]}]}}
    return {"data": {"medi": {"answer": "GraphQL KG query - modern flexible API"}}}
