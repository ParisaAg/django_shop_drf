class CartSession:
    def __init__(self,session):
        self.session = session
        self.cart = self.session.setdefault("cart",
        {
            "item":[],
            "total_price":0,
            "total_items":0

        })
        self.add_product("100")
    def add_product(self,product_id):
        for item in self.cart["items"]:
            if product_id== item["product_id"]:
                item["quantity"]+=1
                break
            else:
                new_item={
                    "product_id":product_id,
                    "quantity":1, 
                }
                self.cart["items"].append(new_item)
            self.save()

    def clear(self):
        self.cart = self.session["cart"]={
            "item":[],
            "total_price":0,
            "total_items":0
        }

    def get_cart_items(self):
        return self.cart["items"]
        self.save()
    def save(self):
        self.session.modified = True