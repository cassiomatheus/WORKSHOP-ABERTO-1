from pydantic import BaseModel
from datetime import datetime

class Vendas(BaseModel):
    numero_contrato: str
    data_contrato: str
    valor_contrato: float

