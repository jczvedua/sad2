from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm

@login_required
def items_list(request):
    items = Item.objects.all()
    return render(request, 'items.html', {'items': items})

def create_item_view(request):
    form = ItemForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            Item.objects.create(name=name, price=price)
            return redirect('items')
    return render(request, 'create_item.html', { 'form': form})

def edit_item_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('items')
    return render(request, 'edit_item.html', { 'form': form })

def delete_item_view(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
    return redirect('items')
