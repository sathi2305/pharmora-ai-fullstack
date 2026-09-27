
'use client'
import { useState } from 'react'
export default function Chat(){
  const [msg,setMsg]=useState('Warfarin + Fluconazole bleeding risk?')
  const [lang,setLang]=useState('en')
  const [hist,setHist]=useState([{role:'medi',message:'Hi I am Medi empathetic companion 💙'}])
  const send=async()=>{
    setHist(h=>[...h,{role:'user',message:msg}])
    const r=await fetch('http://localhost:8000/api/v1/chat/stream',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:msg,language:lang})})
    const reader=r.body?.getReader()
    let medi=''
    if(reader){ while(true){ const {done,value}=await reader.read(); if(done) break; const t=new TextDecoder().decode(value); medi+=t.replace('data: ','').replace('[DONE]',''); setHist(h=>{ const c=[...h]; if(c[c.length-1].role==='medi' && c.length>1) c[c.length-1]={role:'medi',message:medi}; else c.push({role:'medi',message:medi}); return c }) } }
  }
  return (<div className="p-6 max-w-3xl mx-auto"><h1 className="text-2xl font-bold">Medi Chat - 12 languages voice+text</h1><div className="mt-4 bg-white rounded shadow p-4 h-96 overflow-auto">{hist.map((m:any,i)=><div key={i} className={`mt-3 p-3 rounded ${m.role==='user'?'bg-[#DCE6F0] ml-12':'bg-[#C5E8E3] mr-12'}`}>{m.message}</div>)}</div><div className="flex gap-2 mt-4"><select value={lang} onChange={e=>setLang(e.target.value)} className="border p-2 rounded"><option value="en">EN</option><option value="ta">TA</option><option value="hi">HI</option></select><input className="flex-1 border p-3 rounded" value={msg} onChange={e=>setMsg(e.target.value)}/><button onClick={send} className="bg-[#39577D] text-white px-6 rounded">Send</button></div></div>)
}
