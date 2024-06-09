print('Lista de animes')

anime_lista = []

while True:
    añadir_anime = input('Introduce el nombre del anime: ')
    anime_lista.append(añadir_anime)
    continuar = input('¿Quieres añadir otro anime a la lista? (s/n): ')
    if continuar.lower() != 's' and continuar.lower() != 'si' :
        break

# Convertir la lista a un string
anime_texto = ', '.join(anime_lista)

print(f'Tus animes agregados a la lista son : {anime_texto}')