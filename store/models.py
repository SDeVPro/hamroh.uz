from django.db import models
import datetime 
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod #ya'ni bu metodni funksiyani har joydan chaqirib ishlatish mumkin
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name 
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='images/products/')

    @staticmethod 
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)#
    @staticmethod 
    def get_all_products():
        return Product.objects.all()
    @staticmethod 
    def get_all_products_by_categoryid(category_id):
        if category_id:#mavjud bo'lsa category_id == "True":
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()
    @staticmethod 
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False 
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True  
        return False 

class Order(models.Model):#buyurtma 
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    def placeOrder(self):#buyurtmani tasdiqlash
        self.save()
    @staticmethod 
    def get_orders_by_customer(customer_id):#mijoz 
        return Order.objects.filter(customer=customer_id).order_by('-date')#eng oxirgi buyurtma bo'yicha 




    
