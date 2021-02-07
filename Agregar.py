import psycopg2
def insert_inventario(CONTADOR,NOMBRE_PACIENTE,APELLIDO_PACIENTE,DNI_PACIENTE,EDAD_PACIENTE,TEMPERATURA_PACIENTE,PULSO_PACIENTE):
    sql = """ INSERT INTO DATOS_PACIENTE (CONTADOR,NOMBRE_PACIENTE,APELLIDO_PACIENTE,
                                            DNI_PACIENTE,EDAD_PACIENTE,TEMPERATURA_PACIENTE,
                                            PULSO_PACIENTE) VALUES (%s,%s,%s,%s,%s,%s,%s);"""
    
    conn = None
    
    try:
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        database="BASE_DATOS_PACIENTES",
        password="davis")
        
        cur = conn.cursor()
        
        cur.execute(sql, (CONTADOR,NOMBRE_PACIENTE,APELLIDO_PACIENTE,DNI_PACIENTE,EDAD_PACIENTE,TEMPERATURA_PACIENTE,PULSO_PACIENTE))
        
        conn.commit()
        cur.close()

        if conn is not None:
            conn.close()
            
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()

#if __name__ == "__main__":
    #insert_inventario("1",'davis','leyva',"44558866", 99, 45.5,77)