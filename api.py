from fastapi import FastAPI
from router.router import evento



app = FastAPI()

app.include_router(evento)

@app.get("/",operation_id="main")
def root():
    return "hola"
#class ActualizarEvento(BaseModel):
#    id_evento: Optional[int] = None
#    nombre: Optional[str] = None
#    fecha:  Optional[str] = None
#    hora_inicio:  Optional[str] = None
#    hora_fin: Optional[str] = None
#    ubicacion: Optional[str] = None
#    descripcion: Optional[str] = None
#    file: Optional[str] = None
#    id_usuario: Optional[int] = None
#    id_empresa: Optional[int] = None
#    estado: Optional[str] = None
#   frecuencia_eventos:Optional[str] = None
#    tipo_evento:Optional[str] = None
#    clasificacion_evento:Optional[str] = None

#eventos = {
#        1:  {
#             "id_evento": 1,
#             "nombre": "ENGAGE CON TERESA GOMEZ",
#             "fecha": "30/03/2023",
#             "hora_inicio":"-",
#             "hora_fin":"-",
#             "ubicacion":"-",
#             "descripcion":"-",
#             "file":"./writable/uploads/1/Eventos/1/photoMain/1678211970_11c2af2e653b42ae5e47.jpg",
#             "id_usuario": "null",
#             "id_empresa": "null",
#             "estado": "Activo",
#             "frecuencia_eventos":"-",
#             "tipo_evento":"-",
#             "clasificacion_evento":"-"
#        }
#    }

#@app.get("/obtener-evento/{id_evento}")
#def obtener_evento(id_evento:int):
#    return eventos[id_evento]
 
#@app.get("/optener-por-nombre")
#def obtener_evento(nombre:str):
#    for id_evento in eventos:
#        if eventos[id_evento]["nombre"] == nombre:
#            return eventos[id_evento]
#    return {"Data":"Not found"}

#@app.post("/crear-evento/{id_evento}")
#def crear_evento(evento:EventoDatos):
#   e=Evento(id_evento=evento.id_evento,nombre=evento.nombre,fecha=evento.fecha,hora_inicio=evento.hora_inicio,hora_fin=evento.hora_fin,ubicacion=evento.ubicacion,descripcion=evento.descripcion,file=evento.file,id_usuario=evento.id_usuario,id_empresa=evento.id_empresa,estado=evento.estado,frecuencia_eventos=evento.frecuencia_eventos,tipo_evento=evento.tipo_evento,clasificacion_evento=evento.clasificacion_evento)
#   db.add(e)
#   db.commit()
#   return e

#@app.put("/actualizar-evento/{id_evento}")
#def actualizar_evento(id_evento:int, evento: ActualizarEvento):
#    if id_evento in eventos:
#        return {"Error": "Item ID already exists."}

#    if evento.nombre != None:
#       eventos[id_evento].nombre = evento.nombre 

#    if evento.fecha != None:
#       eventos[id_evento].fecha = evento.fecha

#    if evento.hora_inicio != None:
#       eventos[id_evento].hora_inicio = evento.hora_inicio

#    if evento.hora_fin != None:
#       eventos[id_evento].hora_fin = evento.hora_fin 

#    if evento.ubicacion != None:
#       eventos[id_evento].ubicacion = evento.ubicacion

#    if evento.descripcion != None:
#       eventos[id_evento].descripcion = evento.descripcion

#    if evento.file != None:
#       eventos[id_evento].file = evento.file 

#    if evento.id_usuario != None:
#       eventos[id_evento].id_usuario = evento.id_usuario

#    if evento.id_empresa != None:
#       eventos[id_evento].id_empresa = evento.id_empresa

#    if evento.estado != None:
#       eventos[id_evento].estado = evento.estado 

#    if evento.frecuancia_eventos != None:
#       eventos[id_evento].frecuancia_eventos = evento.frecuancia_eventos

#    if evento.tipo_evento != None:
#       eventos[id_evento].tipo_evento = evento.tipo_evento

#    if evento.clasificacion_evento != None:
#       eventos[id_evento].clasificacion_evento = evento.clasificacion_evento 


#@app.delete("/borrar-evento")
#def borrar_evento(id_evento:int = Query(..., description = "blah blah")):
#    if id_evento not in eventos:
#        return {"Error": "ID does not exist."}

#    del eventos[id_evento]
#    return {"Success": "Item deleted!"}