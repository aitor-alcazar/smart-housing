from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from app.core.database import init_db, get_session
from app.models.models import UserPreferences, Property, Evaluation
from app.services.evaluation.scoring import score_property
from app.services.ai.mock_provider import MockAIProvider
import json
app=FastAPI(title="Smart Housing API")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173","https://<github-user>.github.io"],allow_methods=["*"],allow_headers=["*"])
@app.on_event("startup")
def st(): init_db()
@app.get('/health')
def health(): return {"status":"ok"}
@app.get('/api/preferences')
def get_prefs(s:Session=Depends(get_session)):
    p=s.exec(select(UserPreferences)).first()
    if not p: p=UserPreferences(); s.add(p); s.commit(); s.refresh(p)
    return p
@app.post('/api/preferences')
@app.put('/api/preferences')
def save_prefs(payload:dict,s:Session=Depends(get_session)):
    p=s.exec(select(UserPreferences)).first() or UserPreferences()
    for k,v in payload.items():
        if hasattr(p,k): setattr(p,k,v)
    s.add(p); s.commit(); s.refresh(p); return p
@app.post('/api/properties/scrape')
async def scrape(payload:dict,s:Session=Depends(get_session)):
    url=payload.get('url','')
    if not url.startswith('http'): raise HTTPException(400,'Invalid URL')
    demo={"source":"generic","url":url,"title":"Exterior 3-bedroom apartment near public transport","price":320000,"surface_m2":88,"rooms":3,"bathrooms":1,"floor":"2","has_elevator":True,"has_parking":False,"is_exterior":True,"orientation":"west","energy_certificate":"E","address_text":"Alcalá de Henares, Madrid","description":"Bright exterior apartment...","features":["elevator","exterior"],"images":[],"missing_data":["building_year"],"extraction_confidence":0.7}
    p=Property(**{k:v for k,v in demo.items() if k in Property.model_fields}); s.add(p); s.commit(); s.refresh(p)
    return {"property_id":p.id,**demo}
@app.post('/api/evaluations')
async def evaluate(payload:dict,s:Session=Depends(get_session)):
    pid=payload.get("property_id")
    p=s.get(Property,pid) if pid else None
    prop=(p.model_dump() if p else payload.get("property_data",{}))
    prefs=(s.exec(select(UserPreferences)).first() or UserPreferences()).model_dump()
    scoring=score_property(prop,prefs)
    ai=await MockAIProvider().analyse_property_viability(prop,prefs,{}, {}, scoring)
    ev=Evaluation(property_id=pid or "manual",global_score=scoring["global_score"],viability=ai["viability"],scores_json=json.dumps(scoring["scores"]),ai_analysis_json=json.dumps(ai),financial_analysis_json=json.dumps({"estimated_monthly_mortgage":1080,"affordability_status":"stretched"}),renovation_estimate_json=json.dumps({"level":"medium","estimated_cost_min":26000,"estimated_cost_max":61000}),red_flags_json=json.dumps(ai["red_flags"]),positive_signals_json=json.dumps(ai["positive_signals"]),questions_to_ask_json=json.dumps(ai["questions_to_ask"]),negotiation_points_json=json.dumps(ai["negotiation_points"]),recommended_next_steps_json=json.dumps(ai["recommended_next_steps"]),missing_data_json=json.dumps(ai["unknowns"]),report_markdown=ai["summary"])
    s.add(ev); s.commit(); s.refresh(ev)
    return {"evaluation_id":ev.id,"global_score":ev.global_score,"viability":ev.viability,"scores":scoring["scores"],"summary":ai["summary"],"positive_signals":ai["positive_signals"],"red_flags":ai["red_flags"],"questions_to_ask":ai["questions_to_ask"],"negotiation_points":ai["negotiation_points"],"recommended_next_steps":ai["recommended_next_steps"],"missing_data":ai["unknowns"],"financial_analysis":{"estimated_monthly_mortgage":1080,"affordability_status":"stretched"},"estimated_intervention":{"level":"medium","estimated_cost_min":26000,"estimated_cost_max":61000},"ai_analysis":{"provider":"mock","model":"mock","confidence":ai["confidence"],"reasoning_summary":ai["summary"]},"report_markdown":ai["summary"]}
@app.get('/api/evaluations')
def list_eval(s:Session=Depends(get_session)): return s.exec(select(Evaluation)).all()
@app.get('/api/evaluations/{eid}')
def get_eval(eid:str,s:Session=Depends(get_session)): return s.get(Evaluation,eid)
