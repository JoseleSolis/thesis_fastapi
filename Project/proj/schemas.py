from pydantic import BaseModel


class Person(BaseModel):
    name: str
    last_name: str

class Item(BaseModel):
    serial_number : str
    description : str
    stock_number : int
    category_id: int

class ItemCategory(BaseModel):
    name: str

