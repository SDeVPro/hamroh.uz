from django import template 
register = template.Library() 
@register.filter(name='currency')
def currency(number):
    return "UZS"+str(number) #templateda narxni chiqaramiz shu narx oldiga UZS ni qo'yib qo'yadi

@register.filter(name='multiply')
def multiply(number,number1):
    return number*number1 
    