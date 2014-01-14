from django.test.testcases import TestCase
from django.test.utils import override_settings
from django_core.utils.loading import get_class_from_settings
from django_core.utils.loading import get_class_from_settings_from_apps
from django_core.utils.loading import get_class_from_settings_full_path
from django_core.utils.loading import get_model_from_settings

from tests.test_objects.models import TestModel


class LoadingTestCase(TestCase):
    """TestCase for loading classes."""

    @override_settings(MY_MODEL_SETTING='test_objects.TestModel')
    def test_get_class_from_settings(self):
        model = get_class_from_settings(settings_key='MY_MODEL_SETTING')
        self.assertEqual(model, TestModel)

    @override_settings(MY_MODEL_SETTING='test_objects.TestModel')
    def test_get_model_from_settings(self):
        model = get_model_from_settings(settings_key='MY_MODEL_SETTING')
        self.assertEqual(model, TestModel)

    @override_settings(MY_MODEL_SETTING='tests.test_objects.models.TestModel')
    def test_get_class_from_settings_full_path(self):
        model = get_class_from_settings_full_path(settings_key='MY_MODEL_SETTING')
        self.assertEqual(model, TestModel)

    @override_settings(MY_MODEL_SETTING='test_objects.TestModel')
    def test_get_class_from_settings_from_apps(self):
        model = get_class_from_settings_from_apps(settings_key='MY_MODEL_SETTING')
        self.assertEqual(model, TestModel)

