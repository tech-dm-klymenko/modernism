from wagtail.contrib.modeladmin.helpers import WagtailBackendSearchHandler
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from buildings.models import (
    AccessType,
    BuildingPage,
    BuildingType,
    City,
    ConstructionType,
    Country,
    Detail,
    Facade,
    Position,
    Roof,
    Tag,
    Window,
)


class BuildingAdmin(ModelAdmin):
    model = BuildingPage
    list_display = (
        "name",
        "city",
        "country",
        "building_type",
        "year_of_construction",
        "protected_monument",
        "building_architects",
        "building_developers",
    )
    menu_icon = "arrow-right"
    menu_order = 201
    search_handler_class = WagtailBackendSearchHandler
    list_per_page = 25

    def building_architects(self, obj):
        building_architects = obj.architects.values_list(
            "architect__last_name", flat=True
        )
        return ", ".join([name for name in building_architects])

    def building_developers(self, obj):
        building_developers = obj.developers.values_list(
            "developer__last_name", flat=True
        )
        return ", ".join([name for name in building_developers])


class ConstructionTypeAdmin(ModelAdmin):
    model = ConstructionType
    menu_label = "Construction Types"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)


class DetailAdmin(ModelAdmin):
    model = Detail
    menu_label = "Detail Types"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)


class FacadeAdmin(ModelAdmin):
    model = Facade
    menu_label = "Facade Types"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)


class PositionAdmin(ModelAdmin):
    model = Position
    menu_label = "Position Types"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)


class WindowAdmin(ModelAdmin):
    model = Window
    menu_label = "Window Types"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)


class RoofAdmin(ModelAdmin):
    model = Roof
    menu_label = "Roof Types"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)


class AccessTypeAdmin(ModelAdmin):
    model = AccessType
    menu_label = "Access Types"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)


class BuildingTypeAdmin(ModelAdmin):
    model = BuildingType
    menu_label = "Building Types"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name",)


class FeatureAdmin(ModelAdminGroup):
    menu_label = "Type Definitions"
    menu_order = 210
    items = (
        BuildingTypeAdmin,
        RoofAdmin,
        WindowAdmin,
        AccessTypeAdmin,
        PositionAdmin,
        DetailAdmin,
        ConstructionTypeAdmin,
        FacadeAdmin,
    )


class CityAdmin(ModelAdmin):
    model = City
    menu_label = "Cities"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "country")
    ordering = ["name"]


class CountryAdmin(ModelAdmin):
    model = Country
    menu_label = "Countries"
    menu_icon = "placeholder"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("country",)


class LocationAdmin(ModelAdminGroup):
    menu_label = "Locations"
    menu_order = 210
    items = (
        CityAdmin,
        CountryAdmin,
    )


class TagAdmin(ModelAdmin):
    model = Tag
    menu_label = "Tags"
    menu_icon = "tag"
    menu_order = 295
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = (
        "name",
        "slug",
    )


modeladmin_register(TagAdmin)
modeladmin_register(FeatureAdmin)
modeladmin_register(LocationAdmin)
modeladmin_register(BuildingAdmin)
