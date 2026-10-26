from io import BytesIO
import tempfile

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from PIL import Image

from .models import Post


class PostPagesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.older_post = Post.objects.create(
            title='Una publicación anterior',
            content='Texto anterior.',
            published_at='2025-01-01T10:00:00Z',
            is_published=True,
        )
        cls.newer_post = Post.objects.create(
            title='Una publicación reciente',
            content='Texto reciente.',
            published_at='2025-02-01T10:00:00Z',
            is_published=True,
        )

    def test_home_lists_posts_newest_first_with_excerpt_and_cover(self):
        response = self.client.get(reverse('blog:post_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Una publicación reciente')
        self.assertContains(response, 'Texto reciente.')
        self.assertContains(response, 'blog/images/cover.svg')
        self.assertLess(
            response.content.index(b'Una publicaci\xc3\xb3n reciente'),
            response.content.index(b'Una publicaci\xc3\xb3n anterior'),
        )

    def test_detail_shows_content_and_link_back_home(self):
        response = self.client.get(
            reverse('blog:post_detail', args=[self.newer_post.slug]),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Una publicación reciente')
        self.assertContains(response, 'Texto reciente.')
        self.assertContains(response, reverse('blog:post_list'))
        self.assertContains(response, 'class="back-link"')
        self.assertNotContains(response, 'article-back-link')

    def test_detail_has_only_one_back_to_list_link(self):
        response = self.client.get(
            reverse('blog:post_detail', args=[self.newer_post.slug]),
        )

        self.assertEqual(response.content.count(b'class="back-link"'), 1)

    def test_unknown_slug_returns_not_found(self):
        response = self.client.get(
            reverse('blog:post_detail', args=['no-existe']),
        )

        self.assertEqual(response.status_code, 404)

    def test_unpublished_post_is_hidden_from_list_and_detail(self):
        draft = Post.objects.create(
            title='Borrador privado',
            content='Este texto todavía no es público.',
            is_published=False,
        )

        list_response = self.client.get(reverse('blog:post_list'))
        detail_response = self.client.get(
            reverse('blog:post_detail', args=[draft.slug]),
        )

        self.assertNotContains(list_response, 'Borrador privado')
        self.assertEqual(detail_response.status_code, 404)

    def test_published_post_is_visible_to_anonymous_visitors(self):
        post = Post.objects.create(
            title='Publicación visible',
            content='Este texto ya es público.',
            is_published=True,
        )

        list_response = self.client.get(reverse('blog:post_list'))
        detail_response = self.client.get(
            reverse('blog:post_detail', args=[post.slug]),
        )

        self.assertContains(list_response, 'Publicación visible')
        self.assertContains(detail_response, 'Este texto ya es público.')

    def test_missing_image_does_not_render_broken_image(self):
        response = self.client.get(
            reverse('blog:post_detail', args=[self.newer_post.slug]),
        )

        self.assertNotContains(response, 'article-image')

    def test_migrations_seed_two_example_posts(self):
        sample_posts = Post.objects.filter(
            slug__in=[
                'el-cafe-que-queria-ser-una-variable-de-entorno',
                'mi-primer-deploy-y-la-planta-que-hizo-qa',
            ],
        )

        self.assertEqual(sample_posts.count(), 2)
        self.assertTrue(all(post.is_published for post in sample_posts))
        self.assertTrue(all(post.image for post in sample_posts))
        self.assertTrue(all(post.image_alt for post in sample_posts))


class PostAdminTests(TestCase):
    def test_admin_requires_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('admin:blog_post_changelist'))

        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def setUp(self):
        user = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='test-password',
        )
        self.client.force_login(user)

    def test_staff_can_create_post_without_an_image(self):
        response = self.client.post(
            reverse('admin:blog_post_add'),
            {
                'title': 'Publicación desde admin',
                'slug': '',
                'content': 'Contenido creado desde el panel.',
                'published_at_0': '2025-03-01',
                'published_at_1': '12:00:00',
                'is_published': 'on',
                'image': '',
                'image_alt': '',
                '_save': 'Guardar',
            },
        )

        self.assertEqual(response.status_code, 302)
        post = Post.objects.get(title='Publicación desde admin')
        self.assertEqual(post.slug, 'publicacion-desde-admin')
        self.assertFalse(post.image)
        self.assertTrue(post.is_published)

    def test_staff_can_upload_post_image(self):
        image_content = BytesIO()
        Image.new('RGB', (1, 1), color='red').save(image_content, format='PNG')

        with tempfile.TemporaryDirectory() as media_root:
            with override_settings(MEDIA_ROOT=media_root):
                response = self.client.post(
                    reverse('admin:blog_post_add'),
                    {
                        'title': 'Artículo con imagen',
                        'slug': '',
                        'content': 'Contenido ilustrado.',
                        'published_at_0': '2025-03-01',
                        'published_at_1': '12:00:00',
                        'is_published': 'on',
                        'image': SimpleUploadedFile(
                            'cafe.png',
                            image_content.getvalue(),
                            content_type='image/png',
                        ),
                        'image_alt': 'Una taza de café junto al ordenador',
                        '_save': 'Guardar',
                    },
                )

                self.assertEqual(response.status_code, 302)
                post = Post.objects.get(title='Artículo con imagen')
                self.assertTrue(post.image)
                self.assertEqual(
                    post.image_alt,
                    'Una taza de café junto al ordenador',
                )
                detail = self.client.get(
                    reverse('blog:post_detail', args=[post.slug]),
                )

                self.assertEqual(detail.status_code, 200)
                self.assertContains(
                    detail,
                    'alt="Una taza de café junto al ordenador"',
                )
                self.assertContains(detail, post.image.url)
