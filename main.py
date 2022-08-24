import sqlite3


def main():
    #crearalumno(1, 'Janice', 'Presley')
    #crearalumno(2, 'Chandler', "Bing")
    #crearalumno(3, 'Monica', 'Geller')
    #crearalumno(4, 'Ross', 'Geller')
    #crearalumno(5, 'Phoebe', 'Buffay')
    #crearalumno(6, 'Rachel', 'Green')
    #crearalumno(7, 'Joey', 'Trivianni')
    #crearalumno(8, 'Mike', 'Hannigan')

    buscaralumno(2)


def crearalumno(identificacion, nombre, apellido):
    conn = sqlite3.connect('escuela.db', isolation_level=None)
    cursor = conn.cursor()

    query = f"INSERT INTO alumnos(id, nombre, apellido) VALUES({identificacion}, '{nombre}', '{apellido}')"
    cursor.execute(query)
    cursor.close()
    conn.close()


def buscaralumno(identificacion):
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM alumnos WHERE id={identificacion}"
    rows = cursor.execute(query)
    print(rows.fetchone())

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
