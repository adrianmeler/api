from fastapi import APIRouter
from schema.evento_schema import EventoSchema
from config.db import cursor,db




evento = APIRouter()

@evento.get("/")
def root():
    return {"message":"hola"}


@evento.post("/api/evento")
def create_evento(data_evento:EventoSchema):
    query = "INSERT INTO eventos(nombre,fecha,hora_inicio,hora_fin,ubicacion,descripcion,file,id_usuario,id_empresa,estado,frecuencia_eventos,tipo_evento,clasificacion_evento) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (data_evento.nombre,data_evento.fecha,data_evento.hora_inicio,data_evento.hora_fin,data_evento.ubicacion,data_evento.descripcion,data_evento.file,data_evento.id_usuario,data_evento.id_empresa,data_evento.estado,data_evento.frecuencia_eventos,data_evento.tipo_evento,data_evento.clasificacion_evento)
    cursor.execute(query,values)
    db.commit()
    


@evento.put("/api/put/{id}")
def update_evento(id:int, data_evento:EventoSchema):
    query = "UPDATE eventos SET nombre=%s, fecha=%s, hora_inicio=%s, hora_fin=%s, ubicacion=%s, descripcion=%s, file=%s, id_usuario=%s, id_empresa=%s, estado=%s, frecuencia_eventos=%s, tipo_evento=%s, clasificacion_evento=%s WHERE id_evento=%s"
    values = (data_evento.nombre,data_evento.fecha,data_evento.hora_inicio,data_evento.hora_fin,data_evento.ubicacion,data_evento.descripcion,data_evento.file,data_evento.id_usuario,data_evento.id_empresa,data_evento.estado,data_evento.frecuencia_eventos,data_evento.tipo_evento,data_evento.clasificacion_evento, id)
    cursor.execute(query,values)
    db.commit()


@evento.delete("/api/delete/{id}")
def borrar_evento(id:int):
    query = "DELETE FROM eventos WHERE id_evento=%s"
    cursor.execute(query,(id,))
    db.commit()


@evento.get("/api/leer")
def leer_datos():
    query = "SELECT * FROM eventos"
    cursor.execute(query)
    result = cursor.fetchall()
    for evento in result:
        return evento
    