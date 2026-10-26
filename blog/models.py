from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(
        default=False,
        verbose_name='publicada',
        help_text='Activa esta opción para mostrar la publicación a los visitantes.',
    )
    image = models.ImageField(upload_to='posts/', blank=True)
    image_alt = models.CharField(
        max_length=200,
        blank=True,
        help_text='Describe la imagen; déjalo vacío solo si la imagen es decorativa.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'publicación'
        verbose_name_plural = 'publicaciones'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title) or 'publicacion'
            candidate = base_slug
            suffix = 2
            while Post.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f'{base_slug}-{suffix}'
                suffix += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
