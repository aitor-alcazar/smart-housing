import { useEffect, useState } from "react";import { health } from "../lib/api";
export default function(){
	const [ok,setOk]=useState(false);
	useEffect(()=>{health().then(setOk)},[]);
	return <div className='space-y-4'>
		<div className='card'>
			<h1 className='text-2xl font-bold'>Smart Housing</h1>
			<p>AI-assisted property viability analysis.</p>
			<p className={ok?"text-green-600":"text-amber-600"}>Backend: {ok?"Connected":"Offline — this static site will use demo mode"}</p>
			<p className='text-sm text-slate-500'>This frontend is prepared as an MVP for GitHub Pages. Backend features will be integrated later.</p>
		</div>
	</div>
}
