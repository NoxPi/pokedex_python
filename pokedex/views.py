from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {}
    return render(request, "index.html", context)


def pokemon(request, pokemon):
    from pokedex.models import Pokemon
    result = Pokemon.objects.filter(english_full_name__iexact=pokemon)
    if result:
        context = {'pokemon': result[0]}
        return render(request, "single_pokemon.html", context)
    else:
        return render(request, "index.html", status=404)


def typeahead(request, pokemon):
    from pokedex.models import Pokemon
    import json

    dummy = request
    result = Pokemon.objects.filter(english_full_name__istartswith=pokemon)

    print result
    response = {}
    for poke in result:
        response[poke.id] = poke.english_full_name

    print json.dumps(response)

    return HttpResponse(json.dumps(response), content_type='application/json')

