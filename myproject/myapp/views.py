# from django.shortcuts import render
# from . models import Product

# # Create your views here.

# def index(request):
#     return render(request,'index.html')


# def list_products(request):
#     '''_summary_
#     returns prdct list page
#     Args:
#         request(_type_): _description_
    
#     Returns:
#            _type_: _description_
#      '''
#     product_list=Product.objects.all()
#     context={'products':product_list}
#     return render(request,'product.html',context)



# # view a single product view


# def detail_products(request):
#     if request.POST:
#         print(request)

#     # return render(request,'product_details.html')



from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    return render(request,'index.html')

def list_products(request):
    '''Returns product list page'''
    product_list = Product.objects.order_by('priority')
    context = {'products': product_list}
    return render(request, 'product_list.html', context)

def detail_product(request, id):
    '''Returns a single product detail page'''
    product = get_object_or_404(Product, id=id)
    # or Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product_details.html', context)






