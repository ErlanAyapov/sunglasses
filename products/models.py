from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.utils import timezone
# category
# products
# cart product
# cart
# order

# customer
# spaceificates

class Category(models.Model):

	name = models.CharField('Имя категори', max_length = 255)
	slug = models.SlugField(unique = True)

	def __str__(self):
		return self.name


class Product(models.Model):
	BUYING_TYPE_SELF = 'Оптом'
	BUYING_TYPE_DELIVERY = 'Розница'

	BUYING_TYPE_CHOICES = (
		(BUYING_TYPE_SELF, 'Оптом'),
		(BUYING_TYPE_DELIVERY, 'Розница')
	)
	category	= models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Категрия' )
	title		= models.CharField('Именование', max_length = 255)
	slug		= models.SlugField(unique = True)
	picture		= models.CharField('Ссылка изоброжении', max_length = 255)
	description = models.TextField('Описание')
	price		= models.DecimalField(max_digits = 9, decimal_places = 2, verbose_name = 'Цена')
	prduct_type = models.CharField(max_length=100,
		verbose_name='Тип заказа',
		choices=BUYING_TYPE_CHOICES,
		default=BUYING_TYPE_SELF)
	number 		= models.CharField('Сериный номер товара', max_length = 50, blank = True)

	def __str__(self):
		return self.title


class QuantityOrder(models.Model):
	product = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = 'Продукт')
	quantity = models.CharField('Количество заказа', max_length = 255, blank = True)
	def __str__(self):
		return str(self.product) + ' ' + self.quantity


class Customer(models.Model):

	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
	phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
	address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
	orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order', blank=True)

	def __str__(self):
		return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)

class Order(models.Model):
	STATUS_NEW = 'Новый заказ'
	STATUS_IN_PROGRESS = 'Заказ в обработке'
	STATUS_READY = 'Заказ готов'
	STATUS_COMPLETED = 'Заказ выполнен'

	BUYING_TYPE_SELF = 'Самовывоз'
	BUYING_TYPE_DELIVERY = 'Доставка'

	STATUS_CHOICES = (
		(STATUS_NEW, 'Новый заказ'),
		(STATUS_IN_PROGRESS, 'Заказ в обработке'),
		(STATUS_READY, 'Заказ готов'),
		(STATUS_COMPLETED, 'Заказ выполнен')
	)

	BUYING_TYPE_CHOICES = (
		(BUYING_TYPE_SELF, 'Самовывоз'),
		(BUYING_TYPE_DELIVERY, 'Доставка')
	)

	user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Кому' )

	# client     = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Покупатель', blank = True )
	first_name = models.CharField(max_length=255, verbose_name='Имя')
	last_name  = models.CharField(max_length=255, verbose_name='Фамилия')
	phone      = models.CharField(max_length=20, verbose_name='Телефон')
	# cart       = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
	address    = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)

	status = models.CharField(
		max_length=100,
		verbose_name='Статус заказ',
		choices=STATUS_CHOICES,
		default=STATUS_NEW
	)

	buying_type = models.CharField(
		max_length=100,
		verbose_name='Тип заказа',
		choices=BUYING_TYPE_CHOICES,
		default=BUYING_TYPE_SELF
	)

	comment    = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
	created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
	# order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)
	product    = models.ManyToManyField('Product', verbose_name='Заказы на товар', related_name='related_order')
	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Cart(models.Model):
	user    = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
	product = models.ForeignKey(Product, on_delete = models.CASCADE, null=True)
	comment = models.CharField('Комментарий к заказу', max_length = 1000)

	def __str__(self):
		return str(self.user)