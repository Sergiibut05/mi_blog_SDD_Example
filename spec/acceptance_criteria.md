# Criterios de aceptación — Mi Blog

Estos criterios definen las condiciones para considerar terminado el MVP. Las imágenes de portada forman parte de la entrega; las imágenes de cada publicación son opcionales.

## 1. Página de inicio y listado

- [ ] Al ejecutar `python manage.py runserver`, la ruta `/` carga la página de inicio sin errores.
- [ ] La página muestra las publicaciones ordenadas de la más reciente a la más antigua.
- [ ] Cada publicación del listado muestra su título, fecha de publicación y un extracto del contenido.
- [ ] El título de cada publicación enlaza a su página de detalle.
- [ ] Hay al menos dos publicaciones de ejemplo visibles en el listado.
- [ ] La portada incluye una imagen representativa que se carga correctamente y se adapta al ancho de la pantalla.

## 2. Detalle y navegación

- [ ] Al abrir una publicación desde el listado, su página de detalle muestra el título, la fecha y el contenido completo.
- [ ] Desde la página de detalle hay un enlace visible para volver a `/`.
- [ ] El recorrido desde el listado a una publicación y de vuelta al listado se completa en un máximo de tres clics.

## 3. Imágenes de las publicaciones

- [ ] El administrador puede asociar una imagen ilustrativa a una publicación desde Django Admin.
- [ ] En el detalle, la imagen de una publicación se muestra cuando se ha añadido.
- [ ] Una publicación sin imagen sigue mostrándose correctamente, sin espacio roto ni error.
- [ ] Las imágenes de las publicaciones se adaptan al ancho disponible y no desbordan el contenido.
- [ ] Cuando sea posible, las imágenes o ilustraciones de ejemplo tienen un tono humorístico y son pertinentes al contenido.
- [ ] Las imágenes cuentan con texto alternativo descriptivo para que su contenido sea comprensible si no se visualizan.

## 4. Administración y acceso

- [ ] Un usuario autorizado puede crear, editar y borrar publicaciones desde el Django Admin estándar.
- [ ] Cada publicación tiene los estados borrador y publicada; solo las publicadas aparecen en las páginas de lectura.
- [ ] La gestión de publicaciones requiere autenticación; no hay formularios públicos para crear o editar contenido.
- [ ] Las páginas de lectura son accesibles sin iniciar sesión.

## 5. Diseño adaptable y legibilidad

- [ ] La página de inicio y el detalle son legibles y utilizables en un viewport de aproximadamente 375 px de ancho y en escritorio.
- [ ] El texto tiene una tipografía legible y contraste suficiente con el fondo.
- [ ] Las imágenes de portada y de publicaciones no provocan desbordamiento horizontal en móvil.

## 6. Ejecución y documentación

- [ ] El proyecto puede iniciarse localmente con SQLite aplicando las migraciones y ejecutando `python manage.py runserver`.
- [ ] El README explica cómo crear y activar un entorno virtual, instalar dependencias, ejecutar migraciones, crear un superusuario, definir o cambiar su contraseña y arrancar el servidor.
- [ ] El proyecto está versionado en Git y subido a GitHub.