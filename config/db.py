import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="apieventos2"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Create the table with an auto-incrementing primary key
cursor.execute("""
    CREATE TABLE IF NOT EXISTS eventos (
        id_evento INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(255) NOT NULL,
        fecha INT NOT NULL,
        hora_inicio varchar(255) NOT NULL,
        hora_fin varchar(255) NOT NULL,
        ubicacion varchar(255) NOT NULL,
        descripcion varchar(255) NOT NULL,
        file varchar(255) NOT NULL,
        id_usuario INT NOT NULL,
        id_empresa INT NOT NULL,
        estado varchar(255) NOT NULL,
        frecuencia_eventos varchar(255) NOT NULL,
        tipo_evento varchar(255) NOT NULL,
        clasificacion_evento varchar(255) NOT NULL
    )
""")

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
#cursor.close()
#db.close()

