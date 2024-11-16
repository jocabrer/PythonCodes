import random
from datetime import datetime, timedelta

# Función para generar una fecha aleatoria entre dos fechas dadas
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Función para generar datos de 'personas'
def generate_persona_data(start_id, num_records):
    names = ['Carlos', 'Maria', 'Juan', 'Ana', 'Luis', 'Jorge', 'Elena', 'Josefina', 'Pedro', 'Laura', 'Gabriel', 'Sofia']
    last_names = ['Gomez', 'Perez', 'Diaz', 'Martinez', 'Lopez', 'Sanchez', 'Ramirez', 'Torres', 'Silva', 'Mendoza']
    domains = ['example.com', 'test.com', 'correo.cl', 'empresa.cl', 'negocio.com']
    empresa_ids = [random.randint(10, 30) for _ in range(num_records)]
    is_active = [1, 0]
    start_date = datetime(2023, 9, 1)
    end_date = datetime(2024, 3, 31)
    
    # Generar las sentencias INSERT
    insert_statements = []
    for i in range(num_records):
        persona_id = start_id + i
        nombre = f"{random.choice(names)} {random.choice(last_names)}"
        correo = f"{nombre.replace(' ', '').lower()}@{random.choice(domains)}"
        empresa_id = random.choice(empresa_ids)
        es_activo = random.choice(is_active)
        created_at = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')
        updated_at = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')
        insert_statements.append(
            f"INSERT INTO personas (id, empresaID, nombre, correo, notas, rut, fonoMovil, fonoFijo, esActivo, createdAt, updatedAt, usuarioCreadorID, codigoPersonaTipo) "
            f"VALUES({persona_id}, {empresa_id}, '{nombre}', '{correo}', '', '', '', '', {es_activo}, '{created_at}', '{updated_at}', 8, 'CLIENTE');"
        )
    
    return insert_statements

# Generar 100 registros más
persona_data = generate_persona_data(102, 100)
persona_data
