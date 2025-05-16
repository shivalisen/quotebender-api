from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, Self

characters = ['Aang', 'Katara', 'Sokka', 'Zuko', 'Toph', 'Iroh', 'Suki', 'Cabbage Merchant', 'Azula', 'Mai', 'Ty Lee', 'Gyatso', 'Bumi', 'Dai Li Agent', 'Huu', 'Avatar Roku', 'Avatar Kyoshi', 'Avatar Yangchen', 'Avatar Kuruk', 'Lion Turtle', 'Chong', 'Pakku', 'Aunt Wu', 'Guru Patik', 'Professor Zei']

class Params(BaseModel):
  character: Optional[str] = None
  season: Optional[int] = Field(default=None, ge=1, le=3)
  episode: Optional[int] = Field(default=None, ge=1, le=21)

  @field_validator('character', mode='after')
  @classmethod
  def is_character(cls, character: str) -> str:
    name = character.title()
    if name not in characters:
      raise ValueError
    return name
  
  @model_validator(mode='after')
  def check_season_for_episode(self) -> Self:
    if self.episode is None:
      return self
    
    if self.season is not None:
      if (self.season == 1 or 2) and (self.episode != 21):
        return self
      else:
        raise ValueError
      
    raise ValueError

