import psycopg2

connecta = psycopg2.connect(
    user="postgres", password="Fatima104398301j", port="5432", host="localhost", database="escuela"
)

connecta.autocommit=True

apuntador = connecta.cursor()


# Creando table de estudiantes
apuntador.execute(
    "CREATE TABLE IF NOT EXISTS estudiantes (ID SERIAL,BOLETA BIGINT PRIMARY KEY,NOMBRE VARCHAR(255), APELLIDO_PATERNO VARCHAR(50),APELLIDO_MATERNO VARCHAR(50), email VARCHAR(255))"
)

# Creando table de materias
apuntador.execute(
    "CREATE TABLE IF NOT EXISTS  materias (BOLETA BIGINT,CODIGO_MATERIA INTEGER  PRIMARY KEY,CALIFICACION_1 DOUBLE PRECISION,CALIFICACION_2 DOUBLE PRECISION,CALIFICACION_3 DOUBLE PRECISION)"


)

datos=[

("92021898", "RAFAEL", "JARDON","NAVARRO","rafael@mail.com"),
("92021899", "FATIMA", "JARDON","SANCHEZ","fatima@mail.com"),
("92021897", "ANTONIO", "GARCIA","URIBE","antonio@mail.com"),
("92021896", "ANGEL", "PEREZ","GARCIA","angel@mail.com"),
("92021895", "OSCAR", "SALMERON","SOLIS","oscar@mail.com"),
("92021894", "SEBASTIAN", "ESTRADA","SANCHEZ","sebastian@mail.com"),
("92021893", "BRUNO", "PEREZ","PEREZ","bruno@mail.com"),
("92021892", "MARIA", "POMPOSO","NAVARRO","maria@mail.com"),
("92021891", "MARIBEL", "RODRIGUEZ","MANZANO","maribel@mail.com"),
("92021890", "MONICA", "GUTIERREZ","CASTAÑEDA","monica@mail.com"),


]

datos1=[
("92021898", 56, 10,9,8),
("92021899",51,6,7,8) ,
("92021897", 50,6,7,8),
("92021896", 49,6,7,8),
("92021895", 52,6,7,8),
("92021894", 40,6,7,8),
("92021893",60,9,7,8 ),
("92021892", 59,6,7,8),
("92021891",57,6,7,8 ),
("92021898",58, 6,5,9)
]




for registro in datos:

    apuntador.execute(
    "INSERT INTO estudiantes (BOLETA, NOMBRE, APELLIDO_PATERNO,APELLIDO_MATERNO, email) VALUES (%s, %s, %s,%s,%s)", registro)
    

for registro1 in datos1:

    apuntador.execute(
    "INSERT INTO materias (BOLETA,CODIGO_MATERIA,CALIFICACION_1,CALIFICACION_2, CALIFICACION_3) VALUES (%s, %s, %s,%s,%s)", registro1)




# Create table

apuntador.execute("SELECT * FROM  estudiantes JOIN materias  ON estudiantes.BOLETA=materias.BOLETA WHERE materias.codigo_materia=56")
resultados=apuntador.fetchall()
for fila in resultados:
    print (fila)

apuntador.close()


