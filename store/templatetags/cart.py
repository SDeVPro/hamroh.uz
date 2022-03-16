from django import template #templatega chiqarish uchun funksionalni osonlashtirish
register = template.Library() #template bilan ishlovchi hamma kutubxonani olib kelsin
@register.filter(name='is_in_cart')#filter yaratvommiz, bu filter nomi is_in_cart kartaga tushtimi? 
def is_in_cart(product,cart):#kartadami funksiyamiz
    keys = cart.keys() #kalitlar id product idsni kartada mavjud ekanligini tasdiqlaydi
    for id in keys:#keyslar ichida yuramiz va tekshiramiz
        if int(id) == product.id:#id product id ga teng bo'lsa unda hamma ma'lumotlarni olib chiqishga ruxsat beradi id=1 olma meva-cheva mahsuloti price: 15000 kg 
            return True 
    return False 

@register.filter(name='cart_quantity')#nechta product olinganligi to'g'risida
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id) #id da mavjud bo'lgan productda mavjud bo'lgan sonni olib kelsin masalan man 1 ta olishim kere bergan bo'lsam bittani qaytaradi
    return False 

@register.filter(name='price_total')
def price_total(product,cart):
    return product.price * cart_quantity(product,cart)#1 ta 15000 total  15000 
@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum = 0 
    for p in products:
        sum += price_total(p,cart) 
    return sum 



