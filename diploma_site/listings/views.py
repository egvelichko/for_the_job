from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import EmptyPage, Paginator
from .choices import price_choices, bedroom_choices, state_choices
# from django.views import View #начали
# from django.http import JsonResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    listings = Estate.objects.order_by('-date_add').filter(archive=0)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, id_estate):
    listing = get_object_or_404(Estate, pk=id_estate)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    query_results = Region.objects.all()
    location_list = RegionView()

    context = {
        'query_results': query_results,
        'location_list': location_list,

    }
    return render(request,'listings/search.html', context)

#     outRegions = Region.objects.all()
#     return render(request, 'listings/search.html', {'Region': outRegions})



# def search(request):
#
#     queryset_list = Estate.objects.order_by('-date_add').filter(archive=0)
#     regions = Region.objects.all()
#     cities = City.objects.all()
#
#     # if 'keywords' in request.GET:
#     #     keywords = request.GET['keywords']
#     #     if keywords:
#     #         queryset_list = queryset_list.filter(description__icontains=keywords)
#
#
#     # state
#     if 'id_region' in request.GET:
#         id_region = request.GET['id_region']
#         if id_region:
#             queryset_list = queryset_list.filter(id_region__id_region__iexact=id_region)
#
#         # city
#     if 'id_city' in request.GET:
#         id_city = request.GET['id_city']
#         if id_city:
#             queryset_list = queryset_list.filter(id_city=id_city)
#
#         # area
#     if 'id_area' in request.GET:
#         id_area = request.GET['id_area']
#         if id_area:
#             queryset_list = queryset_list.filter(id_area=id_area)
#
#     # bedrooms
#     if 'bedrooms' in request.GET:
#         bedrooms = request.GET['bedrooms']
#         if bedrooms:
#             queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
#
#     # price
#     if 'price' in request.GET:
#         price = request.GET['price']
#         if price:
#             queryset_list = queryset_list.filter(price__lte=price)
#
#     context = {
#         'cities': cities,
#         'regions': regions,
#         'queryset_list': queryset_list,
#         'values': request.GET
#     }
#     return render(request, 'listings/search.html', context)

def search(request):

    listings = Estate.objects.order_by('-date_add').filter(archive=0)

    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    regions = Region.objects.all()
    cities = City.objects.all()
    areas = Area.objects.all()
    obj = Objects.objects.all()

    queryset_list = Estate.objects.order_by('-date_add').filter(archive=0)
    # # Keywords
    # if 'keywords' in request.GET:
    #     keywords = request.GET['keywords']
    #     if keywords:
    #         queryset_list = queryset_list.filter(description__icontains=keywords)


    if request.method == 'POST':
        #gives list of id of inputs
        list_of_input_ids=request.POST.getlist('obj')
        # if list_of_input_ids:
        #     for i in list_of_input_ids:
        #         queryset_list = queryset_list.filter(id_objects__id_objects__iexact=list_of_input_ids)

    #  # obj
    # if 'Obj' in request.GET:
    #     objects = request.GET['Obj']
    #     if objects:
    #         for i in objects:
    #             queryset_list = queryset_list.filter(id_objects__id_objects__iexact=objects)


    # City
    if 'id_city' in request.GET:
        city = request.GET['id_city']
        if city:
            queryset_list = queryset_list.filter(id_city__id_city__iexact=city)

    # state
    if 'id_region' in request.GET:
        state = request.GET['id_region']
        if state:
            queryset_list = queryset_list.filter(id_region__id_region__iexact=state)

    # bedrooms
    if 'id_area' in request.GET:
        area = request.GET['id_area']
        if area:
            queryset_list = queryset_list.filter(id_area__id_area__iexact=area)

    # price
    if 'priceOT' in request.GET or 'priceDO' in request.GET:
        priceOT = request.GET['priceOT']
        priceDO = request.GET['priceDO']
        if priceOT:
            queryset_list = queryset_list.filter(price_estate__gte=priceOT)
        elif priceDO:
            queryset_list = queryset_list.filter(price_estate__lte=priceDO)
        else:
            queryset_list = queryset_list.filter(price_estate__gte=priceOT, price_estate__lte=priceDO)

    context = {
        # 'state_choices': state_choices,
        # 'bedroom_choices': bedroom_choices,
        # 'price_choices': price_choices,
        'listings': queryset_list,
        'listingss': paged_listings,
        'name_region': regions,
        'name_cities': cities,
        'name_areas': areas,
        'name_obj': obj,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
# AJAX
# def load_cities(request):
#     id_region = request.GET.get('id_region')
#     cities = City.objects.filter(id_region=id_region).all()
#     return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})
