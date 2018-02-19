from django.shortcuts import render

# Create your views here.

def customer_details(request):
    """
    """
    context = {}
    return render(request, 'customer_details.html', context)
