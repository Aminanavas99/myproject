from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def list_products(request):
    '''_summary_
    returns prdct list page
    Args:
        request(_type_): _description_
    
    Returns:
           _type_: _description_
     '''
    return render(request,'product.html')



# view a single product view


def detail_products(request):
    return render(request,'product_details.html')





