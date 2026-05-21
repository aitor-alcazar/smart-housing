def score_property(prop:dict,prefs:dict)->dict:
    financial=75 if prop.get("price",0)<=prefs.get("max_price",350000) else 45
    preferences=85 if prop.get("rooms",0)>=prefs.get("min_rooms",3) else 55
    condition=65;building=70;renovation_risk=60;data_quality=80
    global_score=int(financial*0.3+preferences*0.25+condition*0.2+building*0.15+renovation_risk*0.1)
    return {"scores":{"financial":financial,"preferences":preferences,"condition":condition,"building":building,"renovation_risk":renovation_risk,"data_quality":data_quality},"global_score":global_score}
