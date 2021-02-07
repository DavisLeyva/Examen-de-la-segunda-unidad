import psycopg2
def crear_tablas():
    comandos = (
        """CREATE TABLE DATOS_PACIENTE(
            CONTADOR VARCHAR PRIMARY KEY,
            NOMBRE_PACIENTE VARCHAR(30) NOT NULL,
            APELLIDO_PACIENTE VARCHAR(30) NOT NULL,
            DNI_PACIENTE VARCHAR(8) NOT NULL,
            EDAD_PACIENTE INTEGER NOT NULL,
            TEMPERATURA_PACIENTE FLOAT NOT NULL,
            PULSO_PACIENTE FLOAT NOT NULL)
        """,
    )
    
    conn = None
    
    try:
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        database="BASE_DATOS_PACIENTES",
        password="davis")
        
        cur = conn.cursor()
        
        for comando in comandos:
            cur.execute(comando)
        
        cur.close()
        conn.commit()

        if conn is not None:
            conn.close()
            
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    crear_tablas()
