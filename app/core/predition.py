from pydantic import BaseModel
from typing import Optional 
from enum import ENUM

class PredictionStatus(str,ENUM):
    peding='peding'  # partido no ha iniciado
    locked='locked'  # partido en curso o finalizado
    processed='processed' # puntos calculados
class PredictionCreate(BaseModel):
    fixture_id:int
    prediced_home:int
    prediced_away:int
class PredictionUpdate(BaseModel):
        prediced_home:int
        predicted_away: int

class PreditionResponde(BaseModel):
    id:str
    uid:str
    fixture_id:int
    Predicted_home:int
    Predicted_away:int
    points:Optional[int] = None
    status:PredictionStatus = PredictionStatus.pending
    proccesd: bool= False
    # Info del partido embebida para no hacer doble consulta en el front
    home_Team_name:Optional[str]=None
    away_team_name:Optional[str]=None
    home_Team_name:Optional[str]=None
    away_team_name:Optional[str]=None
    kickoff: Optional[str]= None
    Phase:Optional[int] = None
    real_away: Optional[int] = None