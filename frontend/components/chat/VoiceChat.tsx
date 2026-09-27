
'use client'
import { useState } from 'react'
export default function VoiceChat({onTranscript}:{onTranscript:(t:string,lang:string)=>void}){
  const [listening,setListening]=useState(false)
  const start=()=>{
    const SR:any = (window as any).webkitSpeechRecognition || (window as any).SpeechRecognition
    if(!SR) return alert('Speech not supported')
    const rec=new SR()
    rec.lang='ta-IN' // auto detect: en-IN, hi-IN, ta-IN
    rec.onstart=()=>setListening(true)
    rec.onresult=(e:any)=>{
      const text=e.results[0][0].transcript
      const lang=rec.lang.split('-')[0]
      onTranscript(text,lang)
      setListening(false)
    }
    rec.start()
  }
  return (
    <button onClick={start} className={`p-3 rounded-full ${listening?'bg-red-500 animate-pulse':'bg-[#0E7C86]'} text-white`}>
      🎙️ {listening?'Listening...':'Hey Medi (12 langs)'}
    </button>
  )
}
