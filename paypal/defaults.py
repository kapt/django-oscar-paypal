from django.conf import settings

PAYPAL_SOURCE_TYPE_NAME = getattr(settings, 'PAYPAL_SOURCE_TYPE_NAME', 'PayPal')
