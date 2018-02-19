from django.shortcuts import render

# Create your views here.

def customer_details(request):
    """
    """
    customers = ['1', '2', '3', '4', '5']
    context = {
        'customers': customers,
    }
    return render(request, 'customer_details.html', context)
