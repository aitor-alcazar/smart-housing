from typing import Optional
from sqlmodel import SQLModel, Field
import uuid
class UserPreferences(SQLModel, table=True):
    id:str=Field(default_factory=lambda:str(uuid.uuid4()), primary_key=True)
    max_price:int=350000
    max_monthly_payment:int=1000
    preferred_locations_json:str="[]"
    min_surface_m2:int=75
    min_rooms:int=3
    min_bathrooms:int=1
    elevator_required:bool=True
    parking_required:bool=False
    exterior_required:bool=True
    preferred_orientation_json:str='["south","south-west","west"]'
    max_renovation_level:str="medium"
    min_energy_certificate:str="E"
    floor_preferences_json:str='["1","2","3","4"]'
    building_age_max:Optional[int]=None
    category_weights_json:str='{"financial":0.3,"preferences":0.25,"condition":0.2,"building":0.15,"renovation_risk":0.1}'
    financial_assumptions_json:str='{"down_payment_percent":20,"purchase_tax_percent":10,"notary_registry_management_percent":1.5,"mortgage_interest_percent":3,"mortgage_years":30,"renovation_buffer_percent":15}'
class Property(SQLModel, table=True):
    id:str=Field(default_factory=lambda:str(uuid.uuid4()), primary_key=True)
    source:str="generic";url:str="";title:str="";price:Optional[int]=None;surface_m2:Optional[int]=None;rooms:Optional[int]=None;bathrooms:Optional[int]=None;floor:Optional[str]=None
    has_elevator:Optional[bool]=None;has_parking:Optional[bool]=None;is_exterior:Optional[bool]=None;orientation:Optional[str]=None;energy_certificate:Optional[str]=None;address_text:Optional[str]=None;description:Optional[str]=None
    features_json:str="[]";raw_data_json:str="{}";extraction_confidence:float=0.5
class Evaluation(SQLModel, table=True):
    id:str=Field(default_factory=lambda:str(uuid.uuid4()), primary_key=True)
    property_id:str;preferences_snapshot_json:str="{}";global_score:int=0;viability:str="medium";scores_json:str="{}";financial_analysis_json:str="{}";image_analysis_json:str="{}";ai_analysis_json:str="{}";renovation_estimate_json:str="{}";red_flags_json:str="[]";positive_signals_json:str="[]";questions_to_ask_json:str="[]";negotiation_points_json:str="[]";recommended_next_steps_json:str="[]";missing_data_json:str="[]";report_markdown:str=""
