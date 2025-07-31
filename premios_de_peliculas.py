#Johann Herrera - 1662920
#Angel Rodas - 1594125

#-----------Sistema de premios de peliculas----------

categorias_voto = ["Mejor Guion", "Mejor Dirección", "Mejor Banda Sonora", "Mejor Animación"]

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
            print(f"La película '{titulo}' ya está registrada.\n")
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
    print(f"Pelicula '{titulo}' registrada con exito en la categoria '{categoria}'.\n")

def registrar_votos(titulo):
    if not peliculas:
        print("No hay películas registradas.")
        return

    for pelicula in peliculas:
        if titulo.lower().strip() == pelicula["titulo"].lower().strip():
            print("\nSeleccione la categoría en la que desea votar:")
            for i, cat in enumerate(categorias_voto, start=1):
                print(f"{i}. {cat}")
            try:
                opcion = int(input("Ingrese el número de la categoría: "))
                if 1 <= opcion <= len(categorias_voto):
                    categoria_elegida = categorias_voto[opcion - 1]
                    pelicula["votos"][categoria_elegida] += 1
                    print(f"Voto registrado para '{titulo}' en la categoría '{categoria_elegida}'.")
                else:
                    print("Opcion invalida. Debe elegir un numero valido.")
            except ValueError:
                print("Entrada invalida. Debe ingresar un numero.")
            return

    print("No se encontró ninguna película con ese título.")


def mostrar_resultados():
    if peliculas:
        for peli in peliculas:
            print(f"\nTítulo: {peli['titulo']} ({peli['categoria']})\n")
            for clave, valor in peli["votos"].items():
                print(f"  {clave}: {valor}")
    else:
        print("No hay peliculas registradas.")

def determinar_ganador():
    for categoria in categorias_voto:
        max_votos = -1
        ganadora = None
        total_votos = 0  
        
        for pelicula in peliculas:
            votos_categoria = pelicula["votos"].get(categoria, 0)
            total_votos += votos_categoria
            if votos_categoria > max_votos:
                max_votos = votos_categoria
                ganadora = pelicula["titulo"]
        
        if total_votos == 0:
            print(f"{categoria}:no hay votos registrados aun")
        else:
            print(f"{categoria}: {ganadora} ({max_votos} votos)")


while True:
    try:
        print ("Bienvenido al sistema de premios de peliculas")
        print ("1. Registrar pelicula y su categoria")
        print ("2. Registrar votos por titulo")
        print ("3. Mostrar resultados actuales")
        print ("4. Pelicula ganadora por categoria")
        print ("5. Salir...")
        opcion = int(input("Ingrese una de las siguientes opciones: "))
        
        if opcion == 1:

            titulo = input("Ingrese el título de la película: ")
            categoria = input("Ingrese la categoría: ")
            registrar_pelicula(titulo, categoria)

        elif opcion == 2:
            titulo = input("Ingrese el título de la película: ")
            registrar_votos(titulo)

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


