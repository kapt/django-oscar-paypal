from django.contrib import admin
from paypal.express.admin import *
from paypal.payflow.admin import *
from paypal.models import PayPalFeesRate

admin.site.register(PayPalFeesRate)
