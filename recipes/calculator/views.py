from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe(request, recipe_name):
    recipe = DATA.get(recipe_name)
    if not recipe:
        return HttpResponse("Рецепт не найден")

    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings <= 0:
            return HttpResponse("Количество порций должно быть положительным числом")
    except ValueError:
        return HttpResponse("Количество порций должно быть целым числом")

    context = {
        'recipe': {ingredient: quantity * servings for ingredient, quantity in recipe.items()}
    }
    return render(request, 'recipe.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
