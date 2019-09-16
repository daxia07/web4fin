from django.shortcuts import render


def recipe(request):
    return render(request, 'pg/recipe.html', {'title': 'Recipes'})


def test(request):
    return render(request, 'pg/test_svg.html')

