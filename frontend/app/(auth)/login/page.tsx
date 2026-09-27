
'use client'
import { useState } from 'react'
export default function Login(){
  const [email,setEmail]=useState('patient@test.com')
  const [password,setPassword]=useState('Test123!')
  const handle=async()=>{
    const r=await fetch('http://localhost:8000/api/v1/auth/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email,password})})
    const d=await r.json()
    if(d.success){ localStorage.setItem('token',d.data.access_token); location.href='/dashboard' }
  }
  return (<div className="flex min-h-screen"><div className="w-1/2 bg-[#39577D] text-white p-12"><h1 className="text-4xl font-bold">Pharmora AI</h1><p className="mt-4 text-xl">Your Empathetic AI Health Companion - Medi</p></div><div className="w-1/2 p-12 max-w-md mx-auto flex flex-col justify-center"><h2 className="text-2xl font-bold">Welcome back</h2><input className="mt-6 border p-3 rounded w-full" value={email} onChange={e=>setEmail(e.target.value)}/><input type="password" className="mt-4 border p-3 rounded w-full" value={password} onChange={e=>setPassword(e.target.value)}/><button onClick={handle} className="mt-6 bg-[#0E7C86] text-white p-3 rounded w-full">Sign In</button><button className="mt-3 border p-3 rounded w-full">Continue with Google</button></div></div>)
}
