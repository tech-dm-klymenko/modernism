from django.db.models.query import Prefetch
from django.http.request import MultiValueDict, QueryDict
from django.shortcuts import render
from el_pagination.decorators import page_template
from rest_framework.decorators import api_view

from mia_buildings.forms import BuildingsFilterForm
from mia_buildings.models import Building, BuildingImage


def _get_filtered_buildings(cleaned_form_data, buildings):
    architects = cleaned_form_data.get("architects")
    if architects.exists():
        buildings = buildings.filter(
            architects__id__in=architects.values_list("id", flat=True)
        )
        if not buildings:
            return buildings.none()

    developers = cleaned_form_data.get("developers")
    if developers.exists():
        buildings = buildings.filter(
            developers__id__in=developers.values_list("id", flat=True)
        )
        if not buildings:
            return buildings.none()

    countries = cleaned_form_data.get("countries")
    if countries.exists():
        buildings = buildings.filter(
            country_id__in=countries.values_list("id", flat=True)
        )
        if not buildings:
            return buildings.none()

    cities = cleaned_form_data.get("cities")
    if cities.exists():
        buildings = buildings.filter(city_id__in=cities.values_list("id", flat=True))
        if not buildings:
            return buildings.none()

    positions = cleaned_form_data.get("positions")
    if positions.exists():
        buildings = buildings.filter(
            positions__id__in=positions.values_list("id", flat=True)
        ).distinct()
        if not buildings:
            return buildings.none()

    details = cleaned_form_data.get("details")
    if details.exists():
        buildings = buildings.filter(
            details__id__in=details.values_list("id", flat=True).distinct()
        )
        if not buildings:
            return buildings.none()

    windows = cleaned_form_data.get("windows")
    if windows.exists():
        buildings = buildings.filter(
            windows__id__in=windows.values_list("id", flat=True).distinct()
        )
    roofs = cleaned_form_data.get("roofs")
    if roofs.exists():
        buildings = buildings.filter(
            roofs__id__in=roofs.values_list("id", flat=True).distinct()
        )
        if not buildings:
            return buildings.none()

    facades = cleaned_form_data.get("facades")
    if facades.exists():
        buildings = buildings.filter(
            facades__id__in=facades.values_list("id", flat=True).distinct()
        )
        if not buildings:
            return buildings.none()

    construction_types = cleaned_form_data.get("construction_types")
    if construction_types.exists():
        buildings = buildings.filter(
            construction_types__id__in=construction_types.values_list(
                "id", flat=True
            ).distinct()
        )
        if not buildings:
            return buildings.none()

    years = cleaned_form_data.get("years")
    if years:
        buildings = buildings.filter(year_of_construction__in=years)
        if not buildings:
            return buildings.none()

    building_type = cleaned_form_data.get("building_types")
    if building_type:
        buildings = buildings.filter(building_type=building_type)
        if not buildings:
            return buildings.none()

    access_type = cleaned_form_data.get("access_type")
    if access_type:
        buildings = buildings.filter(access_type=access_type)
        if not buildings:
            return buildings.none()

    is_protected_monument = cleaned_form_data.get("protected_monument")
    if is_protected_monument != "":
        buildings = buildings.filter(protected_monument=is_protected_monument)
        if not buildings:
            return buildings.none()

    storey = cleaned_form_data.get("storey")
    if storey != "":
        buildings = buildings.filter(storey=storey)
        if not buildings:
            return buildings.none()

    return buildings.distinct()


@page_template("mia_buildings/building_list.html")
def get_building_list(
    request, template="mia_buildings/building_index.html", extra_context=None
):
    building_list = (
        Building.objects.filter(is_published=True)
        .select_related("city")
        .select_related("country")
        .prefetch_related(
            Prefetch(
                "buildingimage_set",
                queryset=BuildingImage.objects.filter(is_feed_image=True),
                to_attr="feed_image",
            )
        )
        .order_by("-created")
    )
    context = {}
    search_query = request.GET.get("q", None)

    if request.method == "POST":
        building_form = BuildingsFilterForm(request.POST)
        request.session["filter-request"] = dict(request.POST)

        if building_form.is_valid():
            context["form"] = building_form
            building_list = _get_filtered_buildings(
                building_form.cleaned_data, building_list
            )

    else:
        current_filter_settings = request.session.get("filter-request")
        context["form"] = BuildingsFilterForm()

        if current_filter_settings is not None:
            for setting, value in list(current_filter_settings.items()):
                try:
                    if value[0] == "":
                        del current_filter_settings[setting]
                except KeyError:
                    continue

            filter_query_dict = QueryDict("", mutable=True)
            filter_query_dict.update(MultiValueDict(current_filter_settings))
            building_form = BuildingsFilterForm(filter_query_dict)

            if building_form.is_valid():
                context["form"] = building_form
                building_list = _get_filtered_buildings(
                    building_form.cleaned_data, building_list
                )

        # if search_query:
        #     search_backend = get_search_backend()
        #     all_buildings = search_backend.search(search_query, all_buildings)

    context["buildings"] = building_list
    context["search_term"] = search_query

    if extra_context is not None:
        context.update(extra_context)

    return render(request, template, context)


@api_view(["GET"])
def get_building_details(
    request,
    id_or_slug,
    template="mia_buildings/building_details.html",
    extra_context=None,
):

    if isinstance(id_or_slug, int):
        building = (
            Building.objects.filter(is_published=True, id=id_or_slug)
            .select_related("city")
            .select_related("country")
            .select_related("access_type")
            .prefetch_related("architects")
            .prefetch_related("developers")
            .prefetch_related("building_types")
            .prefetch_related("positions")
            .prefetch_related("details")
            .prefetch_related("windows")
            .prefetch_related("roofs")
            .prefetch_related("facades")
            .prefetch_related("construction_types")
            .prefetch_related("sources")
            .first()
        )
    else:
        building = (
            Building.objects.filter(is_published=True, slug=id_or_slug)
            .select_related("city")
            .select_related("country")
            .select_related("access_type")
            .prefetch_related("architects")
            .prefetch_related("developers")
            .prefetch_related("building_types")
            .prefetch_related("positions")
            .prefetch_related("details")
            .prefetch_related("windows")
            .prefetch_related("roofs")
            .prefetch_related("facades")
            .prefetch_related("construction_types")
            .prefetch_related("sources")
            .first()
        )

    context = {"building": building}

    if extra_context is not None:
        context.update(extra_context)

    return render(request, template, context)

