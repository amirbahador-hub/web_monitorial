from datetime import datetime
from pydantic import BaseModel, validator, HttpUrl
from web_monitorial.utils.status import status_codes


class Site(BaseModel):
    id: int
    url: str

class Pattern(BaseModel):
    regex: str | None
    is_exists: bool

class Metric(BaseModel):
    url: HttpUrl 
    status_code: int 
    timestamp: int 
    response_time: float | None
    pattern: Pattern

    @validator('status_code')
    def status_code_range(cls, v):
        if int(v) not in status_codes.values():
            raise ValueError(f'status code {v} is not valid')
        return v

