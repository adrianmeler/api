from pydantic import BaseModel
from typing import Optional


class EventoSchema(BaseModel):
    id_evento: Optional[int]
    nombre: str
    fecha: str
    hora_inicio: str
    hora_fin: str
    ubicacion: str
    descripcion: str
    file: str
    id_usuario: int
    id_empresa: int
    estado: str
    frecuencia_eventos: str
    tipo_evento: str
    clasificacion_evento: str

