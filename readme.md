## Base de Datos Postgress
Se creo Base de dato escuela con pgadmin

## Se realiza conexion a la base de datos
    user="postgres", password="Fatima104398301j", port="5432", host="localhost", database="escuela"
    
    
## Se crean dos tablas estudiantes y materias

    "CREATE TABLE IF NOT EXISTS estudiantes (ID SERIAL,BOLETA BIGINT PRIMARY KEY,NOMBRE VARCHAR(255), APELLIDO_PATERNO VARCHAR(50),APELLIDO_MATERNO VARCHAR(50), email VARCHAR(255))"

    "CREATE TABLE IF NOT EXISTS  materias (BOLETA BIGINT,CODIGO_MATERIA INTEGER  PRIMARY KEY,CALIFICACION_1 DOUBLE PRECISION,CALIFICACION_2 DOUBLE PRECISION,CALIFICACION_3 DOUBLE PRECISION)"


## Se agregan registros a ambas tablas

for registro in datos:

    apuntador.execute(
    "INSERT INTO estudiantes (BOLETA, NOMBRE, APELLIDO_PATERNO,APELLIDO_MATERNO, email) VALUES (%s, %s, %s,%s,%s)", registro)
    

for registro1 in datos1:

    apuntador.execute(
    "INSERT INTO materias (BOLETA,CODIGO_MATERIA,CALIFICACION_1,CALIFICACION_2, CALIFICACION_3) VALUES (%s, %s, %s,%s,%s)", registro1)
    
## Se realiza consulta con Join

apuntador.execute("SELECT * FROM  estudiantes JOIN materias  ON estudiantes.BOLETA=materias.BOLETA WHERE materias.codigo_materia=56")
resultados=apuntador.fetchall()
for fila in resultados:
    print (fila)

apuntador.close()
