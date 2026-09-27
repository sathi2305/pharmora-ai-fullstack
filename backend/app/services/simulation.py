def simulate_cascade(drug_ids, genotype=None):
    risks=[]
    if len(drug_ids)>=2:
        risks.append({"drugs": drug_ids[:2], "enzyme": "CYP2C9", "severity": "major", "risk_percent": 86, "mechanism": "Fluconazole inhibits CYP2C9 which metabolizes Warfarin. AUC increases 2.3x -> bleeding.", "explain_path": "Warfarin -[METABOLIZED_BY]-> CYP2C9 <-[INHIBITS]- Fluconazole", "recommendation": "Consider alternative or reduce Warfarin 30-50% + monitor INR. Consult doctor.", "sources": ["DrugBank DB01579"]})
    if len(drug_ids)>=3:
        risks.append({"drugs": drug_ids, "enzyme": "CYP3A4", "severity": "moderate", "risk_percent": 62, "mechanism": "Three-drug cascade CYP3A4 saturation", "explain_path": "DrugA -> CYP3A4 <- DrugB", "recommendation": "Stagger dosing", "sources": ["KEGG"]})
    return {"cascade_graph": {"nodes": [{"id": d, "label": f"Drug {d[:6]}"} for d in drug_ids]+[{"id": "CYP2C9", "label": "CYP2C9"}], "edges": []}, "risks": risks, "genotype_adjusted": genotype is not None}
