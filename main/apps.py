from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    # 会显示在Admin后台管理系统中的左侧菜单导航中。
    verbose_name = "主要管理"
