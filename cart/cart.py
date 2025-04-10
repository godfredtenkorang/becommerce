from decimal import Decimal, ROUND_DOWN
from store.models import Product
from .models import Coupon, ShippingFee

class Cart():
    
    def __init__(self, request):
        
        self.session = request.session
        
        # Returning user - Obtain his/her session
        
        cart = self.session.get('session_key')
        
        # New user - create new session
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        self.cart = cart
        
        self.coupon_code = self.session.get('coupon_code', None)
        self.discount_percentage = self.session.get('discount_percentage', 0)
        self.delivery_fee = Decimal(0.00)
        
    
    def add(self, product, product_qty):
        product_id = str(product.id)
        
        if product_id in self.cart:
            
            self.cart[product_id]['qty'] = product_qty
            
        else:
            self.cart[product_id] = {'final_price': str(product.final_price), 'qty':product_qty}
        self.session.modified = True
        
    def delete(self, product):
        product_id = str(product)
        
        if product_id in self.cart:
            del self.cart[product_id]
            
        self.session.modified = True
        
    def update(self, product, qty):
        product_id = str(product)
        
        product_quantity = qty
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_quantity
            
        self.session.modified = True
        
    def apply_coupon(self, coupon_code):
        try:
            coupon = Coupon.objects.get(code=coupon_code)
            self.coupon_code = coupon.code
            self.discount_percentage = coupon.discount_percentage
            self.session['coupon_code'] = coupon.code
            self.session['discount_percentage'] = coupon.discount_percentage
            self.session.modified = True
            return True
        except:
            self.remove_coupon()
            return False
                
    def remove_coupon(self):
        self.coupon_code = None
        self.discount_percentage = 0
        if 'coupon_code' in self.session:
            del self.session['coupon_code']
        if 'discount_percentage' in self.session:
            del self.session['discount_percentage']
        self.session.modified = True
        
    def set_delivery_fee(self, region):
        print(f"Setting delivery fee for region: {region}")
        try:
            delivery_fee = ShippingFee.objects.get(region=region)
            self.delivery_fee = delivery_fee.fee
            self.session['delivery_fee'] = str(delivery_fee.fee)
            self.session.modified = True
        except ShippingFee.DoesNotExist:
            print(f"No shipping fee found for region: {region}")
            self.delivery_fee = Decimal(0.00)
            
            
    def get_delivery_fee(self):
        return self.delivery_fee.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())
    
    def __iter__(self):
        all_product_ids = self.cart.keys()
        
        products = Product.objects.filter(id__in=all_product_ids)
        
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
            
        for item in cart.values():
            item['final_price'] = Decimal(item['final_price'])
            
            item['total'] = item['final_price'] * item['qty']
            
            yield item
            
    def get_total(self):
        total = sum(Decimal(item['final_price']) * item['qty'] for item in self.cart.values())
        total -= total * Decimal(self.discount_percentage / 100)
        return total.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
    
    def get_all_total(self):
        total = self.get_total() + self.get_delivery_fee()
        return total.quantize(Decimal('0.01'), rounding=ROUND_DOWN)