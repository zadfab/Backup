class ProductDetails(models.Model):
    """
    A model used for storing products of specific order.
    Fields:
        quantity : quantity of product.
                   It should be minimum 1 so we have put validation for that.
    """
    order_id = models.ForeignKey(BoxReceivingDetails, to_field='order_id', db_column='order_id',
                                 related_name="product_details", on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1),])
    unit_price = models.FloatField()
    custom_charge = models.FloatField(default=0)
    category = models.ForeignKey(CategoryDetails, to_field='category_id', db_column="category_id",
                                 related_name='products', on_delete=models.CASCADE)
    # custom_duty = models.FloatField()
    # vat_charge = models.FloatField()
    inspection_status = models.CharField(max_length=20)
    status = models.CharField(max_length=50, default="Active")
    flag = models.IntegerField(default=1)

    def save(self,*args,**kwargs):

        if self._state.adding:
            try:
                country = BoxReceivingDetails.objects.get(order_id=self.order_id.order_id)
                country = country.ezz_id.country.country_id
                category_obj = CategoryDetails.objects.get(category_name=self.category ,country=country)
                custom_duty = category_obj.custom_duty
                vat = category_obj.vat
                custom_charge = ((self.unit_price*custom_duty)/100 + (self.unit_price*vat)/100)*self.quantity
                self.custom_charge = round(custom_charge,2)
            except:
                self.custom_charge=0.0
        return super(ProductDetails,self).save(*args,**kwargs)

        # if  self._state.adding :
        #     self.ezz_id = f"EZ{self.country.fedex_code}{self.ezz_id:05}"
        # return super(CustomerDetails, self).save(*args, **kwargs)


    class Meta:
        db_table = 'PRODUCT_DETAILS'
        ordering = ["-id"]

    def __str__(self):
        return f"OrderId: {self.order_id} | Category: {self.category}"
