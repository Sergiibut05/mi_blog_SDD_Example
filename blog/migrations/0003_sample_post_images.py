from django.db import migrations


SAMPLE_IMAGES = {
    'el-cafe-que-queria-ser-una-variable-de-entorno': (
        'posts/sample-cafe.svg',
        'Una taza de café al lado de un terminal con código.',
    ),
    'mi-primer-deploy-y-la-planta-que-hizo-qa': (
        'posts/sample-deploy.svg',
        'Una planta junto a un portátil mostrando una lista de comprobación.',
    ),
}


def attach_sample_images(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for slug, (image, image_alt) in SAMPLE_IMAGES.items():
        Post.objects.filter(slug=slug, image='').update(
            image=image,
            image_alt=image_alt,
        )


def remove_sample_images(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for slug, (image, image_alt) in SAMPLE_IMAGES.items():
        Post.objects.filter(slug=slug, image=image).update(
            image='',
            image_alt='',
        )


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_sample_posts'),
    ]

    operations = [
        migrations.RunPython(attach_sample_images, remove_sample_images),
    ]
