import requests
import random
from django.http.response import JsonResponse

items_count = 50
external_color_api = f'http://www.colr.org/json/colors/random/{items_count}'


def load_colors():
    response = requests.get(external_color_api).json()
    return [f"#{color['hex']}" for color in response['colors'] if color['hex']]


COLORS = load_colors()


def get_random_color_code():
    return random.choice(COLORS)


def get_labels():
    return ['January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December']


def get_random_data():
    return [random.randint(10, 100) for _ in range(len(get_labels()))]


def generate_response():
    labels = get_labels()
    datasets = []
    for label in ['Jerin', 'Peter', 'George']:
        ds = dict(
            label=label,
            data=get_random_data(),
            fill=False,
            borderColor=get_random_color_code(),
        )
        datasets.append(ds)
    return dict(labels=labels, datasets=datasets)


def get_random_chart_data(request):
    return JsonResponse(generate_response())
