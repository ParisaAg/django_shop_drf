class CartSession:
    def __init__(self,session):
        self.session = session
        self.cart = self.session.get("cart",
        {
            "item":[],
            "total_price":0,
            "total_items":0

        })
        self.session["cart"]=self.cart
        