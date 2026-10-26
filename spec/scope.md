# Alcance del producto — Mi Blog

## Objetivo del MVP

Entregar un blog personal mínimo construido con Django para publicar y leer entradas de texto. El MVP debe cubrir el recorrido básico de lectura y permitir al autor gestionar contenido desde el panel estándar de administración.

## Incluido

- **Listado de publicaciones:** página de inicio en `/`, con publicaciones ordenadas por fecha descendente y título, fecha y extracto para cada una.
- **Detalle de publicación:** página por entrada que muestra título, fecha y contenido completo, con un enlace para volver al listado. Se recomienda una URL legible con `slug`, por ejemplo `/posts/<slug>/`.
- **Modelo de datos:** publicación con título, contenido y fecha de publicación; `slug` único para las URLs cuando se utilice.
- **Administración:** crear, editar y borrar publicaciones mediante Django Admin. Cada publicación puede estar en borrador o publicada; solo las publicadas son visibles al público. No habrá formularios públicos de escritura.
- **Contenido de ejemplo:** incluir o documentar entre dos y tres publicaciones de prueba; el nombre inicial del blog será “Mi Blog”.
- **Portada visual:** incluir una imagen representativa en la página de inicio, optimizada y adaptable a móvil y escritorio. Puede ser una imagen o ilustración estática; no requiere gestión desde Django Admin.
- **Imágenes por publicación:** permitir asociar una imagen ilustrativa a cada entrada y gestionarla desde Django Admin. Las imágenes son opcionales y deben ser pertinentes al contenido.
- **Interfaz:** HTML y CSS propio mínimo, tipografía legible y diseño adaptable a móvil y escritorio.
- **Ejecución local:** estructura estándar de Django, una app `blog` y SQLite para desarrollo; el proyecto debe funcionar con migraciones y `runserver`.

## Fuera de alcance

- Registro o autenticación de visitantes.
- Comentarios.
- Un panel de administración personalizado o complejo.
- Búsqueda, etiquetas o categorías.
- Newsletter e integración con redes sociales.
- API REST, SPA o frontend separado.
- Funciones posteriores como búsqueda, categorías, etiquetas o paginación.

## Criterios de aceptación

- `python manage.py runserver` sirve la página de inicio con el listado.
- Cada publicación del listado abre su detalle, donde se muestran título, fecha y contenido completo.
- Desde el detalle se puede volver al listado.
- Las publicaciones se pueden crear, editar y borrar desde Django Admin.
- La página de inicio muestra al menos dos publicaciones de ejemplo.
- El diseño es legible y usable en un viewport móvil de aproximadamente 375 px y en escritorio.
- Un visitante puede completar el recorrido listado → detalle → listado en un máximo de tres clics.
- El README explica cómo preparar el entorno, instalar dependencias, ejecutar migraciones, crear un superusuario y arrancar el servidor.