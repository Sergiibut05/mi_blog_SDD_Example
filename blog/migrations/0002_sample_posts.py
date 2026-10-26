from datetime import timedelta

from django.db import migrations
from django.utils import timezone


def add_sample_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    now = timezone.now()
    Post.objects.bulk_create([
        Post(
            title='El café que quería ser una variable de entorno',
            slug='el-cafe-que-queria-ser-una-variable-de-entorno',
            content=(
                'Todo empezó cuando mi aplicación dejó de funcionar justo antes de la entrega. '
                'El error decía que faltaba una variable de entorno. Yo también: concretamente, '
                'una variable que controlara el nivel de cafeína.\n\n'
                'Después de revisar tres veces el código, descubrí que había escrito DATABASE_URL '
                'como DATABASE_UR. Una letra se había tomado el día libre. La aplicación volvió '
                'a arrancar y el café, por fin, dejó de recibir la culpa.'
            ),
            published_at=now - timedelta(days=1),
        ),
        Post(
            title='Mi primer deploy y la planta que hizo QA',
            slug='mi-primer-deploy-y-la-planta-que-hizo-qa',
            content=(
                'Publiqué mi primera versión un viernes por la tarde, convencido de que todo '
                'estaba perfecto. La planta de mi escritorio, responsable de calidad no oficial, '
                'parecía poco impresionada.\n\n'
                'A los dos minutos encontré un botón que no llevaba a ninguna parte. La planta '
                'no dijo nada, pero una hoja cayó justo sobre el teclado. Corregí el enlace, '
                'volví a publicar y decidí que la próxima revisión incluiría también a la planta.'
            ),
            published_at=now - timedelta(days=2),
        ),
    ])


def remove_sample_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(
        slug__in=[
            'el-cafe-que-queria-ser-una-variable-de-entorno',
            'mi-primer-deploy-y-la-planta-que-hizo-qa',
        ],
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_posts, remove_sample_posts),
    ]
