from django.test import TestCase

{{ model_import }}


class {{ model_name }}Tests(TestCase):

    def test_create_get(self):
        url = reverse('{{ create_url }}')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_post_creates_{{ model_name|lower }}(self):
        url = reverse('{{ create_url }}')

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual({{ model_name }}._default_manager.count(), 1)

    def test_update_get(self):
        instance = {{ model_name }}._default_manager.create()
        url = reverse('{{ update_url }}', args=[instance.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_update_post_updates_{{ model_name|lower }}(self):
        instance = {{ model_name }}._default_manager.create()
        url = reverse('{{ update_url }}', args=[instance.pk])

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        updated = {{ model_name }}._default_manager.get(pk=instance.pk)

    def test_detail_get(self):
        instance = {{ model_name }}._default_manager.create()
        url = reverse('{{ detail_url }}', args=[instance.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], instance)

    def test_list_get(self):
        instance1 = {{ model_name }}._default_manager.create()
        instance2 = {{ model_name }}._default_manager.create()
        instance3 = {{ model_name }}._default_manager.create()
        url = reverse('{{ list_url }}')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertItemsEqual(list(response.context['object_list']),
                              [instance1, instance2, instance3])

    def test_delete_get(self):
        instance = {{ model_name }}._default_manager.create()
        url = reverse('{{ delete_url }}', args=[instance.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue({{ model_name }}._default_manager.filter(pk=instance.pk).exists())

    def test_delete_post_deletes_{{ model_name|lower }}(self):
        instance = {{ model_name }}._default_manager.create()
        url = reverse('{{ delete_url }}', args=[instance.pk])

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse({{ model_name }}._default_manager.filter(pk=instance.pk).exists())
