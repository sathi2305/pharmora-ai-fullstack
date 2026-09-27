
// PWA Service Worker for offline TTS cache + medicine DB
self.addEventListener('install', e=>{
  e.waitUntil(caches.open('pharmora-v1').then(c=>c.addAll(['/','/dashboard','/manifest.json'])))
})
self.addEventListener('fetch', e=>{
  e.respondWith(caches.match(e.request).then(r=> r || fetch(e.request).then(res=>{
    if(e.request.url.includes('/tts/')){ caches.open('pharmora-tts').then(c=>c.put(e.request,res.clone())) }
    return res
  })))
})
