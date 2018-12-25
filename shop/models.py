from django.db import models
from django.urls import reverse

class user(models.Model):
    username = models.CharField(max_length = 50,verbose_name='用户名')
    password = models.CharField(max_length = 50,verbose_name='密码')
    gender = models.CharField(max_length=10, choices=(('M','男'),('F','女')), default='男', verbose_name='性别')
    phonenumber = models.CharField(max_length=50,verbose_name='电话号码')
    email = models.CharField(max_length=50,verbose_name='邮箱')
    #img = models.ImageField(upload_to='photos',height_field='height', width_field='width',default='static/no_image.png',verbose_name='头像')
    signature = models.CharField(max_length=200,verbose_name='个人签名')
    
    def __str__(self):
        return self.username
    
class market(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    activityTXT = models.CharField(max_length=200,verbose_name='活动信息')
    countTXT = models.CharField(max_length=200,verbose_name='折扣信息')
    image = models.ImageField(upload_to='markett', blank=True)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    addressTXT = models.CharField(max_length=200,verbose_name='地址')
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'market'
        verbose_name_plural = 'markets'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_market',args=[self.slug])
    
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])


class Product(models.Model):
    market = models.ForeignKey(market, related_name='market', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])
    def get_absolute_url2(self):
        return reverse('shop:product2_detail',args=[self.id,self.slug])