from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Order


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'onlinestore/detail.html',
                  {'order': order})