# PRD — Blog de tecnología (Django)

## 1. Resumen
Blog personal mínimo construido con **Django**, para publicar y leer entradas de texto (título, fecha y contenido). Enfoque didáctico: código simple, fácil de explicar en clase y de mantener.

## 2. Problema / oportunidad
Hace falta un blog funcional sin complejidad innecesaria: listar posts, abrirlos y leerlos. Django aporta estructura (modelo–vista–plantilla), panel de admin listo y un flujo estándar para un MVP de clase.

## 3. Objetivos
| Objetivo | Métrica de éxito |
|---|---|
| Visitante lee posts sin fricción | Home → detalle → volver a home en ≤ 3 clics |
| Código entendible en clase | Una app `blog`, pocas vistas/plantillas, modelo claro |
| Arranque local simple | `migrate` + `runserver` y el blog funciona |
| Contenido de prueba | ≥ 2 posts visibles en la home |

## 4. Fuera de alcance (MVP)
- Autenticación de visitantes / registro
- Comentarios
- Panel de admin personalizado o complejo (se usa el admin por defecto de Django)
- Buscador, etiquetas, categorías
- Newsletter, redes sociales, imágenes obligatorias
- API REST, SPA o frontend separado

## 5. Usuarios
| Rol | Necesidad |
|---|---|
| **Visitante** (anónimo) | Ver listado y leer posts |
| **Autor / admin** (local) | Crear y editar posts vía Django Admin |

## 6. Requisitos funcionales

### RF-01 — Listado de posts (home)
- Ruta: `/`
- Muestra posts ordenados por fecha descendente
- Cada ítem: título, fecha de publicación, extracto del contenido
- El título enlaza a la página de detalle

### RF-02 — Detalle de post
- Ruta: `/posts/<slug>/` (o `/posts/<id>/` si se prefiere simplicidad)
- Muestra: título, fecha, cuerpo completo
- Enlace “Volver al listado” hacia `/`

### RF-03 — Datos del post
Campos mínimos del modelo:
- `title` (CharField)
- `slug` (SlugField, único) — opcional si se usa `id` en la URL
- `content` (TextField)
- `published_at` (DateTimeField)
- `created_at` / `updated_at` (opcionales, auto)

### RF-04 — Gestión de contenido
- Crear/editar/borrar posts con **Django Admin**
- No hay formularios públicos de escritura en el MVP

### RF-05 — Contenido inicial
- 2–3 posts de ejemplo (fixtures, data migration o creación manual en admin)
- Nombre del blog: “Mi Blog” (configurable en plantilla/settings)

## 7. Requisitos no funcionales
- **Stack**: Python + Django (versión LTS o la usada en clase)
- **UI**: HTML + CSS propio (o plantillas Django + CSS mínimo); tipografía legible; responsive
- **Rendimiento**: sin dependencias front innecesarias; páginas estáticas de lógica simple
- **Mantenibilidad**: una app `blog`; estructura estándar de proyecto Django
- **Acceso**: lectura pública; escritura solo vía admin autenticado

## 8. Arquitectura propuesta (Django)

```
proyecto/
├── manage.py
├── config/          # settings, urls, wsgi/asgi
│   ├── settings.py
│   └── urls.py
└── blog/
    ├── models.py    # Post
    ├── views.py     # listado + detalle
    ├── urls.py
    ├── admin.py     # registro del modelo Post
    └── templates/blog/
        ├── base.html
        ├── post_list.html
        └── post_detail.html
```

### Flujo
1. Visitante entra en `/` → vista `post_list` → plantilla con queryset de `Post`
2. Clic en un post → vista `post_detail` → plantilla con el objeto
3. Autor inicia sesión en `/admin/` → gestiona `Post`

### Datos
- Base de datos: SQLite en desarrollo (por defecto en Django)
- Sin servicios externos en el MVP

## 9. Diseño / UX
- Una composición limpia: cabecera con nombre del blog + listado o artículo
- Tipografía legible; contraste adecuado
- Extracto en home (p. ej. primeras ~160 caracteres o `truncatewords`)
- Responsive: legible en móvil y escritorio
- Sin cards decorativas innecesarias; foco en lectura

## 10. Criterios de aceptación
- [ ] `python manage.py runserver` sirve la home con el listado
- [ ] Cada post del listado abre su detalle con título, fecha y contenido
- [ ] Desde el detalle se puede volver a la home
- [ ] Posts se crean/editan desde Django Admin
- [ ] Al menos 2 posts de ejemplo visibles
- [ ] Layout usable en viewport móvil (~375px) y desktop
- [ ] README con: entorno virtual, `pip install`, `migrate`, `createsuperuser`, `runserver`

## 11. Entregables
1. Código fuente del proyecto Django
2. `briefing.md` y este `PRD.md`
3. `README.md` con instrucciones de ejecución
4. Posts de ejemplo incluidos o documentados

## 12. Riesgos y mitigaciones
| Riesgo | Mitigación |
|---|---|
| Scope creep (comentarios, tags…) | Mantener fuera de alcance; iterar después del MVP |
| URLs con slug mal generados | Autogenerar slug desde el título en `save()` o usar `id` |
| Estilos rotos en móvil | CSS simple + prueba en viewport estrecho |

## 13. Roadmap sugerido (post-MVP, opcional)
1. Imágenes destacadas
2. Categorías o tags
3. Búsqueda por título
4. Paginación del listado
5. Markdown en el contenido

## 14. Decisiones abiertas
- ¿Slug en URL o solo `id`? → Recomendación: **slug** (más didáctico y URLs legibles)
- ¿Nombre final del blog? → Por defecto **“Mi Blog”**
- ¿CSS a mano o framework (p. ej. Pico.css)? → Recomendación: **CSS propio mínimo** para no oscurecer el aprendizaje de Django
