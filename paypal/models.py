from decimal import Decimal as D
from decimal import ROUND_UP

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from paypal.express.models import *
from paypal.payflow.models import *


class PayPalFeesRate(models.Model):
    min_sales_amount = models.DecimalField(_("Min sales amount"), decimal_places=2, max_digits=12,)
    percentage = models.DecimalField(_("Fees percentage"), decimal_places=4, max_digits=12,)
    fixed_amount = models.DecimalField(_("Fees fixed amount"), decimal_places=2, max_digits=12,)


    class Meta:
        verbose_name = _(u"PayPal fees rate")
        verbose_name_plural = _(u"PayPal fees rates")
        ordering = ["min_sales_amount"]

    def __unicode__(self):
        return u"%s - %s%s + %s%s" % (self.min_sales_amount,
                                    self.percentage * 100,
                                    "%",
                                    self.fixed_amount,
                                    settings.OSCAR_DEFAULT_CURRENCY)

    def compute_fees(self, price_without_fees):
        fees_amount = D('0.00')
        percentage_amount = D(price_without_fees * self.percentage).quantize(D('0.01'), ROUND_UP)
        fees_amount += percentage_amount + self.fixed_amount

        return fees_amount
