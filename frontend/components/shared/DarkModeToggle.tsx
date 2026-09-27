
'use client'
import { useEffect,useState } from 'react'
export default function DarkMode(){
  const [dark,setDark]=useState(false)
  useEffect(()=>{ document.documentElement.classList.toggle('dark',dark) },[dark])
  return <button onClick={()=>setDark(!dark)} className="p-2 rounded border">{dark?'☀️ Light':'🌙 Dark'} Mode - WCAG 2.1</button>
}
