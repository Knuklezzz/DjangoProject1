from django.conf import settings
from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    is_approved = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    admin_comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Process the formset data, e.g. save to the database

    def __str__(self):
        return f"Order #{self.id} for {self.user}"

    def calculate_total_price(self):
        total_price = 0
        for item in self.items.all():
            total_price += item.total_price
        self.total_price = total_price + total_price / 10  # Налог 10%
        self.save()


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="items")
    article = models.CharField(max_length=20)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.article} {self.size}"

    @property
    def total_price(self):
        return self.quantity * self.price
