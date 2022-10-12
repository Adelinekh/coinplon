from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Temoignage


@modeladmin_register
class TemoignageAdmin(ModelAdmin):
    model = Temoignage 
    menu_label = "Témoignage"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu =  False
    exclude_from_explorer = False

#@modeladmin_register = modeladmin_registrer(TemoinageAdmin)