
'use client'
import { useEffect,useState } from 'react'
export default function AdherenceML(){
  const [pred,setPred]=useState({skip_prob:0.32,next_dose:'8:00 PM',nudge:'Friendly Tamil reminder'})
  useEffect(()=>{
    // Mock ML prediction endpoint
    fetch('http://localhost:8000/api/v1/ml/adherence/predict').then(r=>r.json()).then(d=>setPred(d.data||pred))
  },[])
  return (
    <div className="bg-gradient-to-br from-[#39577D] to-[#0E7C86] text-white p-4 rounded shadow">
      <h3 className="font-bold">Adherence Intelligence - ML Prediction</h3>
      <p className="mt-2 text-sm">Skip Probability: {(pred.skip_prob*100).toFixed(0)}% — Next: {pred.next_dose}</p>
      <p className="text-xs opacity-80 mt-1">{pred.nudge}: “Thambi, marunthu edukka marandhuteengala? 💙” - Personalized by Medi</p>
      <div className="mt-3 bg-white/20 h-2 rounded"><div className="bg-white h-2 rounded" style={{width:`${(1-pred.skip_prob)*100}%`}}></div></div>
    </div>
  )
}
