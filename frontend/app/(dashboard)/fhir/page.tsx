
'use client'
export default function FHIRPage(){
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">ABDM FHIR Integration - Modern Interoperability</h1>
      <p className="mt-2 opacity-70">Connects to Ayushman Bharat Digital Mission, EHR export, doctor handoff</p>
      <div className="mt-6 bg-white p-4 rounded shadow">
        <pre className="text-xs bg-[#F5F7FA] p-3 rounded overflow-auto">{`{
  "resourceType": "MedicationRequest",
  "medicationCodeableConcept": {"coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": "11289", "display": "Warfarin"}]},
  "dosageInstruction": [{"text": "5mg daily"}],
  "note": [{"text": "CYP2C9 *2/*3 slow metabolizer - bleeding risk 86% with Fluconazole - flagged by Pharmora AI"}]
}`}</pre>
        <button className="mt-4 bg-[#0E7C86] text-white px-4 py-2 rounded">Export FHIR to Doctor</button>
      </div>
    </div>
  )
}
