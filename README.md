# Django YoshinoGames Proyect

Yoshino Games Proyect es una aplicación web construida con el framework Django que permite a los usuarios explorar, comprar y revisar videojuegos. A continuación, se detallan las características principales: 

## Funcionalidades
**Catálogo de Videojuegos:**  
Los usuarios pueden navegar por una amplia variedad de videojuegos organizados por género, plataforma y popularidad.
Cada juego tiene una página de detalles con información como título, descripción, precio y calificación.

(La aplicacion aun esta en desarrollo por lo tanto a futuro se agregaran mas funcionalidades como un Carrito, Gestiond de Usuarios entre muchas mas.)

## Requisitos

- Python 
- Django 
- Request
- FastAPI

## Instalación

1. Clona este repositorio:

https://github.com/Felipe-Arciniegas/Proyecto-Final-YoshinoGames  (FrontEnd)

https://github.com/Felipe-Arciniegas/VideoJuegos_Api  (BackEnd)

2. Crea un entorno virtual e instala las dependencias:
```bash
cd tienda-de-videojuegos
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Agregar Imagenes (IMPORTANTE!!)

Descargue el Archivo comprimido con la carpeta static, descomprimala y reemplazela en la carpeta de la App
https://drive.google.com/file/d/1Zk75q-qmUA8nn9KQeWhX-XQ31XKwJjYO/view?usp=sharing

4. Ejecute en un Puerto diferente la API de la aplicacion:

(La explacion del uso, activacion e instalacion de la API se encuentra en el archivo README del repositorio.)



5. Ejecuta el servidor de desarrollo:
```bash
python manage.py runserver
```

## Uso y Funciones

Puede ver los Templates y las Urls para encontrar las funciones, por ahora solo esta activo el Home y la Store, los otros aun estan en Desarrollo y espero a futuro poder terminarlos y agregar muchas mas funciones.


## Contribución

Si deseas contribuir, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m "Agrega nueva funcionalidad"`).
4. Envía un pull request.
