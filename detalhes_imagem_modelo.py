from pydantic import BaseModel, Field
from typing import List

class DetalhesImagemModelo(BaseModel):
    titulo: str = Field(
        description="Titulo adequado para a imagem analisada."
    )
    descricao: str = Field(
        description="Descrição detalhada da imagem analisada."
    )
    rotulos: List[str] = Field(
        description="Lista de rótulos ou tags associados à imagem."
    )