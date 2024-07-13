from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category
import requests


def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            url = 'http://127.0.0.1:8080/category/create'

            print(form)
            requests.post(url, json=form.cleaned_data)  # Api'ye gidecek requests olacak
            print(request)
            return redirect('categories')
    else:
        form = CategoryForm()

    return render(
        request=request,
        template_name='create.html',
        context={
            'form': form
        }
    )




def get_categories_by_id(request, id):
    url = f'http://127.0.0.1:8080/category/{id}'
    response = requests.get(url)

    try:
        if response.status_code == 200:
            print(response.json())
    except requests.RequestException as err:
        print(f'Request faild. {err}')

    return render(
        request=request,
        template_name='detail.html',
        context={
            'category': response.json()
        }
    )





def get_all_categories(request):
    url = 'http://127.0.0.1:8080/'
    response = requests.get(url)


    try:
        if response.status_code == 200:
            print(response.json())
    except requests.RequestException as err:
        print(f'Request faild. {err}')


    return render(
        request=request,
        template_name='categories.html',
        context={
            'categories': response.json()
        }
    )



def update(request, id):
    url = f'http://127.0.0.1:8080/category/{id}'
    category = requests.get(url)


    category_object = Category()
    category_object.name = category.json()['name']
    category_object.slug = category.json()['slug']
    category_object.ip_address = category.json()['ip_address']
    category_object.id = category.json()['id']
    category_object.status = category.json()['status']
    category_object.machine_name = category.json()['machine_name']


    try:
        if category.status_code == 200:
            print(category.json())
    except requests.RequestException as err:
        print(f'Request faild. {err}')

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category_object)

        if form.is_valid():
            response = requests.put(url, json=form.cleaned_data)
            print(response)

            return redirect('categories')
    else:
        form = CategoryForm(instance=category_object)

    return render(
        request=request,
        template_name='update.html',
        context={
            'form': form
        }
    )



def delete(request, id):
    url = f'http://127.0.0.1:8080/category/{id}'
    category = requests.get(url)


    try:
        if category.status_code == 200:
            print(category.json())
    except requests.RequestException as err:
        print(f'Request failed. {err}')

    if request.method == 'POST':
        response = requests.delete(url)
        print(f'Response: {response}')


        return redirect('categories')
    else:
        form = CategoryForm()

    return render(
        request=request,
        template_name='delete.html',
        context={
            'form': form
        }
    )