from django.apps import AppConfig


class CmsConfig(AppConfig):
    name = 'CMS'
    def ready(self):
        import CMS.signals