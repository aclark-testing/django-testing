from django.shortcuts import render

# Create your views here.

def customer_details(request):
    """
    """
    context = {
        'customers': 5,
    }
    return render(request, 'customer_details.html', context)
