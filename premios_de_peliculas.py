#Johann Herrera - 1662920
#Angel Rodas - 1594125

#-----------Sistema de premios de peliculas----------
peliculas = [
    {"titulo": "Inception", "categoria": "Ciencia ficción", "votos": {
        "Mejor Guion": 0,
        "Mejor Dirección": 0,
        "Mejor Banda Sonora": 0,
        "Mejor Animación": 0
    }},
    {"titulo": "Titanic", "categoria": "Romance", "votos": {
        "Mejor Guion": 0,
        "Mejor Dirección": 0,
        "Mejor Banda Sonora": 0,
        "Mejor Animación": 0
    }},
    {"titulo": "El Padrino", "categoria": "Crimen", "votos": {
        "Mejor Guion": 0,
        "Mejor Dirección": 0,
        "Mejor Banda Sonora": 0,
        "Mejor Animación": 0
    }}
]

def registrar_pelicula(titulo, categoria):
    for peli in peliculas:
        if peli["titulo"].lower() == titulo.lower():
            print(f"La película '{titulo}' ya está registrada.")
            return

    peliculas.append({
        "titulo": titulo,
        "categoria": categoria,
        "votos": {
            "Mejor Guion": 0,
            "Mejor Dirección": 0,
            "Mejor Banda Sonora": 0,
            "Mejor Animación": 0
        }
    })
    print(f"Pelicula '{titulo}' registrada con exito en la categoria '{categoria}'.")


def registrar_votos(titulo, voto):
    if not peliculas:
        print("No hay peliculas registradas")
        return

    encontrado = False
    voto = voto.strip()  
    for pelicula in peliculas:
        if pelicula["titulo"].lower() == titulo.lower():
            categorias_validas = [k.lower() for k in pelicula["votos"].keys()]
            if voto.lower() in categorias_validas:
                clave_original = [k for k in pelicula["votos"].keys() if k.lower() == voto.lower()][0]
                pelicula["votos"][clave_original] += 1
                encontrado = True
                print(f"Voto registrado en '{clave_original}' para la película '{titulo}'.")
            break

    if not encontrado:
        print("Su voto debe ser a una de estas categorías exactamente:")
        print("Mejor Guion\nMejor Dirección\nMejor Banda Sonora\nMejor Animación")


def mostrar_resultados():
    if peliculas:
        for peli in peliculas:
            print(f"\nTítulo: {peli['titulo']} ({peli['categoria']})")
            for clave, valor in peli["votos"].items():
                print(f"  {clave}: {valor}")
    else:
        print("No hay peliculas registradas.")

def determinar_ganador():
    categorias = ["Mejor Guion", "Mejor Dirección", "Mejor Banda Sonora", "Mejor Animación"]
    
    for categoria in categorias:
        max_votos = -1
        ganadora = None
        
        for pelicula in peliculas:
            votos_categoria = pelicula["votos"].get(categoria)
            if votos_categoria is not None and votos_categoria > max_votos:
                max_votos = votos_categoria
                ganadora = pelicula["titulo"]
        
        if ganadora:
            print(f"{categoria}: {ganadora} ({max_votos} votos)")
        else:
            print(f"{categoria}: Sin votos registrados")


while True:
    try:
        print ("Bienvenido al sistema de premios de peliculas")
        print ("1. Registrar pelicula y su categoria")
        print ("2. Registrar votos por titulo")
        print ("3. Mostrar resultados actuales")
        print ("4. Pelicula ganadora por categoria")
        print ("5. Salir...")
        opcion = int(input("Ingrese una de las siguientes opciones"))
        
        if opcion == 1:

            titulo = input("Ingrese el título de la película: ")
            categoria = input("Ingrese la categoría: ")
            registrar_pelicula(titulo, categoria)

        elif opcion == 2:
            try:
                titulo = input("Ingrese el título de la película: ")
                print("Categorías de voto: Mejor Guion, Mejor Dirección, Mejor Banda Sonora, Mejor Animación")
                voto = input("Ingrese la categoría en la que vota exactamente como aparece: ")
                registrar_votos(titulo, voto)
            except Exception as e:
                print("Error al registrar el voto:", e)
        
        elif opcion == 3:
            mostrar_resultados()
        
        elif opcion == 4:
            print ("Los ganadores de cada categoria hasta el momento")
            determinar_ganador()
            
        elif opcion == 5:
            print ("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida, intente de nuevo")
    
    except ValueError:
        print ("Ingrese un valor numerico")


