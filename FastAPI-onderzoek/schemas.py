from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str
    quantity: int = Field(ge=0)