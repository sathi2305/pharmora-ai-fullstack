
'use client'
import { useState } from 'react'
export default function Meds(){
  const [q,setQ]=useState('warfarin')
  const [res,setRes]=useState([])
  const search=async()=>{
    const r=await fetch(`http://localhost:8000/api/v1/medicines/search?q=${q}&lang=ta`)
    const d=await r.json()
    setRes(d.data||[])
  }
  return (<div className="p-6"><h1 className="text-2xl font-bold">Medicine DB 15K + Jan Aushadhi pricing</h1><div className="flex gap-2 mt-4"><input className="border p-3 rounded flex-1" value={q} onChange={e=>setQ(e.target.value)}/><button onClick={search} className="bg-[#0E7C86] text-white px-6 rounded">Search</button><button className="border px-4 rounded">📷 Scan</button></div><div className="grid grid-cols-2 gap-4 mt-6">{res.map((m:any)=><div key={m.id} className="bg-white p-4 rounded shadow"><h3 className="font-bold">{m.brand_name} ({m.generic_name})</h3><p>MRP ₹{m.mrp}</p></div>)}</div></div>)
}
