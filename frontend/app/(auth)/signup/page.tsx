
'use client'
import { useState } from 'react'
export default function Signup(){
  const [form,setForm]=useState({full_name:'Sathiyamoorthi',email:'',password:'',age:22,gender:'male',language:'en'})
  const submit=async()=>{
    const r=await fetch('http://localhost:8000/api/v1/auth/signup',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(form)})
    const d=await r.json()
    if(d.success){ localStorage.setItem('token',d.data.access_token); location.href='/dashboard' }
  }
  return (<div className="p-12 max-w-lg mx-auto"><h1 className="text-2xl font-bold">Create Account - Pharmora AI</h1><input placeholder="Full Name" className="mt-4 border p-3 rounded w-full" value={form.full_name} onChange={e=>setForm({...form,full_name:e.target.value})}/><input placeholder="Email" className="mt-3 border p-3 rounded w-full" value={form.email} onChange={e=>setForm({...form,email:e.target.value})}/><input placeholder="Password" type="password" className="mt-3 border p-3 rounded w-full" value={form.password} onChange={e=>setForm({...form,password:e.target.value})}/><button onClick={submit} className="mt-6 bg-[#39577D] text-white p-3 rounded w-full">Sign Up</button></div>)
}
