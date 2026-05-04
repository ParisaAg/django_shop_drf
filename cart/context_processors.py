from .cart import CartSession

def cart_processors(request):
    cart = request.session.get('cart')
    if not cart:
        cart=CartSession(request.session)
    return{"cart":cart}