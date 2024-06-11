print('Añade tus animes favoritos a la lista de espera.')

anime_lista = []

while True:
    añadir_anime = input('Escribe el nombre del anime que deseas: ')
    anime_lista.append(añadir_anime)
    continuar = input('¿Quieres añadir este anime a la lista? (s/n): ')
    if continuar.lower() != 's' and continuar.lower() != 'si' :
        break
    
    # Convertir la lista a un string
anime_texto = ', '.join(anime_lista)
print(f'Tus animes añadidos a la lista son: {anime_texto}')
    
    
anime_texto = [anime.capitalize() for anime in anime_texto]

busqueda_anime = input('Introduce el nombre del anime que quieres buscar: ')
if busqueda_anime.lower in anime_texto:
    print(f'{busqueda_anime} está en la lista de animes.')
else:
    print(f'{busqueda_anime} no se encuentra en tu lista de espera.Por favor,añadelo a tu lista.')
   
   


