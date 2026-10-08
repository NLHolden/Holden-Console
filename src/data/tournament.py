from pydantic import BaseModel, Field

from data.enums import PokerSite


class Tournament(BaseModel):
    name: str
    buy_in: float = Field(gt=0)
    site: PokerSite
