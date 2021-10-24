from django.db import models
from django_countries.fields import CountryField
from taggit.managers import TaggableManager


class Feature(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ConstructionType(Feature):
    pass


class Facade(Feature):
    pass


class Roof(Feature):
    pass


class Window(Feature):
    pass


class Detail(Feature):
    pass


class Position(Feature):
    pass


class BuildingType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Building types"


class AccessType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Access types"


class BuildingImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    image = models.ImageField(null=True, blank=True)
    building = models.ForeignKey(
        "mia_buildings.Building", on_delete=models.SET_NULL, null=True, blank=True
    )
    is_feed_image = models.BooleanField(default=False)
    title = models.CharField(max_length=250, blank=True)
    photographer = models.ForeignKey(
        "mia_facts.Photographer", on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField(blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return f"{self.title}"


class Building(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=250, unique=True)
    subtitle = models.CharField(max_length=250, blank=True)
    todays_use = models.CharField(max_length=300, blank=True)
    year_of_construction = models.CharField(max_length=4, blank=True)
    history = models.TextField(blank=True)
    description = models.TextField(blank=True)

    directions = models.TextField(blank=True)
    address = models.TextField(blank=True)
    zip_code = models.CharField(max_length=16, default="00000")
    city = models.ForeignKey(
        "mia_facts.City", on_delete=models.SET_NULL, null=True, blank=True
    )
    country = models.ForeignKey(
        "mia_facts.Country", on_delete=models.SET_NULL, null=True, blank=True
    )
    latitude = models.DecimalField(max_digits=23, decimal_places=20)
    longitude = models.DecimalField(max_digits=23, decimal_places=20)

    protected_monument = models.BooleanField(default=False)
    storey = models.IntegerField(null=True, blank=True)
    access_type = models.ForeignKey(
        AccessType, on_delete=models.SET_NULL, null=True, blank=True,
    )
    building_types = models.ManyToManyField("mia_buildings.BuildingType", blank=True)
    positions = models.ManyToManyField("mia_buildings.Position", blank=True)
    details = models.ManyToManyField("mia_buildings.Detail", blank=True)
    windows = models.ManyToManyField("mia_buildings.Window", blank=True)
    roofs = models.ManyToManyField("mia_buildings.Roof", blank=True)
    facades = models.ManyToManyField("mia_buildings.Facade", blank=True)
    construction_types = models.ManyToManyField(
        "mia_buildings.ConstructionType", blank=True
    )

    architects = models.ManyToManyField("mia_people.Architect", blank=True)
    developers = models.ManyToManyField("mia_people.Developer", blank=True)

    sources = models.ManyToManyField("mia_facts.Source", blank=True)

    def __str__(self):
        return f"{self.name}"
