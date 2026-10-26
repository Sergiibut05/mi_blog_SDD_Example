# Mi Blog

Blog personal sencillo construido con Django, pensado para publicar y leer entradas de forma clara y para que el código sea fácil de entender en clase.

## Funcionalidades

- Página de inicio con publicaciones ordenadas por fecha, título, fecha y extracto.
- Página de detalle con el contenido completo y un enlace para volver al listado.
- Imagen representativa en la portada.
- Imágenes ilustrativas por publicación, gestionadas desde Django Admin.
- Administración de publicaciones mediante Django Admin. La lectura será pública; la edición requerirá autenticación.
- Diseño sencillo, legible y adaptable a móvil y escritorio.
- Dos artículos de ejemplo se crean automáticamente al aplicar las migraciones.

## Requisitos

- Python 3.10 o posterior (el proyecto se ha preparado con Python 3.12).
- Django 5.2 LTS.
- Pillow para validar imágenes subidas.

## Preparación del entorno

Desde la carpeta raíz del proyecto, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Si Windows no reconoce `python`, instala Python y añádelo al `PATH`, o crea el entorno con la ruta completa al ejecutable de Python. Si PowerShell impide activar el entorno virtual, puedes ejecutar los comandos usando directamente `.\.venv\Scripts\python.exe`.

## Arrancar el blog

Desde la raíz del proyecto:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` para visitar el blog y `http://127.0.0.1:8000/admin/` para gestionar las publicaciones. Las imágenes que subas a las entradas se guardarán en `media/posts/` durante el desarrollo.

La primera vez, `createsuperuser` te pedirá un nombre de usuario y una contraseña; no hay credenciales de administrador predefinidas. Para cambiar la contraseña más adelante, ejecuta `python manage.py changepassword <nombre_de_usuario>`. En Django Admin, marca **Publicada** para que una entrada sea visible en el blog; si no está marcada, permanece como borrador.

La base de datos de desarrollo será SQLite. Para detener el servidor, pulsa `Ctrl+C` en la terminal.

El `SECRET_KEY` de desarrollo no se debe utilizar en producción. En un despliegue, configura `DJANGO_SECRET_KEY` con una clave privada y desactiva `DEBUG`.

## Git y GitHub

El proyecto está preparado como repositorio Git. Para subirlo a GitHub, crea un repositorio vacío en tu cuenta y, desde la carpeta raíz del proyecto, configura su URL y sube la rama actual:

```powershell
git remote add origin https://github.com/<usuario>/<repositorio>.git
git push -u origin HEAD
```

GitHub puede pedirte que inicies sesión o autorices Git Credential Manager. No subas contraseñas, claves privadas ni el archivo local `db.sqlite3`.

## Documentación del producto

- [`PRD.md`](./PRD.md): requisitos, arquitectura propuesta y criterios del MVP.
- [`briefing.md`](./briefing.md): resumen del objetivo y público.
- [`spec/vision.md`](./spec/vision.md): visión y principios del producto.
- [`spec/scope.md`](./spec/scope.md): alcance incluido y excluido.
- [`spec/acceptance_criteria.md`](./spec/acceptance_criteria.md): condiciones para validar el MVP.
