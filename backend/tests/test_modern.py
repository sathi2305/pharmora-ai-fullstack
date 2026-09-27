
def test_simulation_cascade():
    from app.services.simulation import simulate_cascade
    r=simulate_cascade(["db01579","db00285"])
    assert r["risks"][0]["risk_percent"]==86
    assert "CYP2C9" in r["risks"][0]["enzyme"]

def test_fhir_export():
    from app.api.fhir import export_fhir
    res=export_fhir("user_1")
    assert res["success"]==True
    assert "Bundle" in str(res["data"])

def test_ml_adherence():
    from app.api.ml import predict_adherence
    res=predict_adherence()
    assert 0 <= res["data"]["skip_prob"] <= 1
