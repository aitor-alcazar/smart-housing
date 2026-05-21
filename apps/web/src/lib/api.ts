const API=import.meta.env.VITE_API_BASE_URL||"http://localhost:8000";
export async function health(){try{const r=await fetch(`${API}/health`);return r.ok}catch{return false}}
export async function scrape(url:string){const r=await fetch(`${API}/api/properties/scrape`,{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({url})});if(!r.ok) throw new Error("scrape failed"); return r.json();}
export async function evaluate(payload:any){const r=await fetch(`${API}/api/evaluations`,{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(payload)});if(!r.ok) throw new Error("eval failed"); return r.json();}
