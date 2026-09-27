import { create } from 'zustand'
export const useAuthStore = create((set:any)=>({user:null,token:null,login:(u:any,t:string)=>{localStorage.setItem('token',t);set({user:u,token:t})},logout:()=>{localStorage.removeItem('token');set({user:null,token:null})}}))
