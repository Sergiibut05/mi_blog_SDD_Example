from django.db import migrations, models


SAMPLE_POST_SLUGS = [
    'el-cafe-que-queria-ser-una-variable-de-entorno',
    'mi-primer-deploy-y-la-planta-que-hizo-qa',
]


def publish_sample_posts(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.filter(slug__in=SAMPLE_POST_SLUGS).update(is_published=True)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_sample_post_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(
                default=False,
                help_text='Activa esta opción para mostrar la publicación a los visitantes.',
                verbose_name='publicada',
            ),
        ),
        migrations.RunPython(
            publish_sample_posts,
            migrations.RunPython.noop,
        ),
    ]
