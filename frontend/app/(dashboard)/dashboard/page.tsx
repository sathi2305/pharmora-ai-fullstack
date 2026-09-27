
'use client'
import { useState } from 'react'
import PillVisionScanner from '@/components/medicine/PillVisionScanner'
import AdherenceML from '@/components/dashboard/AdherenceML'
import VoiceChat from '@/components/chat/VoiceChat'
export default function Dash(){
  const [risks,setRisks]=useState([])
  const [voiceText,setVoiceText]=useState('')
  const sim=async()=>{
    const r=await fetch('http://localhost:8000/api/v1/interactions/simulate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({drug_ids:['db01579','db00285'],genotype:{CYP2C9:'*2/*3'}})})
    const d=await r.json()
    setRisks(d.data?.risks||[])
  }
  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold">Good Morning! Health Score 86/100 - Modern Dashboard 2026</h1>
      <div className="grid grid-cols-3 gap-4 mt-6">
        <div className="space-y-4">
          <div className="bg-white p-4 rounded shadow"><h3 className="font-bold">My Medicines - Modern</h3><button onClick={sim} className="mt-2 bg-[#0E7C86] text-white px-3 py-1 rounded">Simulate Cascade 2 drugs → 86%</button></div>
          <AdherenceML />
          <VoiceChat onTranscript={(t,lang)=>setVoiceText(`${t} (${lang})`)} />
          {voiceText && <div className="bg-white p-2 rounded text-sm">Voice: {voiceText}</div>}
        </div>
        <div className="bg-white p-4 rounded shadow"><h3 className="font-bold">Interaction Alerts - Explainable</h3>{risks.map((r:any,i)=><div key={i} className="mt-2 p-2 bg-red-50 border-l-4 border-red-500"><p className="font-bold text-red-700">{r.severity} {r.risk_percent}%</p><p className="text-sm">{r.mechanism}</p><p className="text-xs opacity-70">{r.explain_path}</p><p className="text-xs text-blue-600">{r.sources?.[0]}</p></div>)}</div>
        <div className="space-y-4"><div className="bg-white p-4 rounded shadow"><h3 className="font-bold">Vitals Trend - Recharts</h3><p className="text-sm">BP 122/80 ↓ after Telmisartan</p><div className="mt-2 h-20 bg-[#F5F7FA] rounded">Chart modern</div></div><PillVisionScanner /></div>
      </div>
      <div className="fixed bottom-6 right-6 bg-[#39577D] text-white p-4 rounded-full shadow-lg">Medi WebSocket Live</div>
    </div>
  )
}
