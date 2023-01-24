from typing import Union
from pydantic import BaseModel

class IncomeOutcome(BaseModel):
    id: Union[int, None] = None
    desc: Union[str, None] = None
    amount: Union[float, None] = None
    date: Union[str, None] = None