from django.db import models


# Create your models here.


class BotUser(models.Model):
    tg_id = models.CharField(max_length=128)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True, null=True)
    user_name = models.CharField(max_length=256, blank=True, null=True)
    is_bot = models.BooleanField(default=False)
    steep = models.CharField(max_length=128, blank=True, null=True)
    last_query = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tg_id} , {self.first_name},{self.user_name},{self.last_name},{self.is_bot}"


class Cars(models.Model):
    car_name = models.CharField(max_length=128)
    car_number = models.CharField(max_length=128)
    tex_passport_number = models.CharField(max_length=128)
    year = models.CharField(max_length=128, null=True, blank=True)
    car_color = models.CharField(max_length=128, null=True, blank=True)
    car_transmission = models.CharField(max_length=128, null=True, blank=True)
    car_km = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return f"{self.car_number},{self.car_name}"


class CarImg(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    img = models.ImageField()

    def __str__(self):
        return f"{self.car.name}"


class CarsLessee(models.Model):
    lessee_first_name = models.CharField(max_length=128)
    lessee_last_name = models.CharField(max_length=128)
    lessee_passport_seria = models.CharField(max_length=128)
    lessee_birth_date = models.CharField(max_length=128, blank=True, null=True)
    lessee_phone_one = models.CharField(max_length=128)
    lessee_phone_two = models.CharField(max_length=128, blank=True, null=True)
    lessee_adress = models.TextField()

    def __str__(self):
        return f"{self.lessee_first_name},{self.lessee_last_name},{self.lessee_phone_two}"


class LesseeImg(models.Model):
    lessee = models.ForeignKey(CarsLessee, on_delete=models.CASCADE)
    img = models.ImageField()
    def __str__(self):
        return f"{self.lessee.name}"

class RentalConditions(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    lessee = models.ForeignKey(CarsLessee)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    starting_price = models.CharField(max_length=256)
    monthly_payment = models.CharField(max_length=258)
    def __str__(self):
        return f"{self.car.name},{self.lessee.name}"


class MonthlyPayment(models.Model):
    rental = models.ForeignKey(RentalConditions,on_delete=models.CASCADE)
    lessee = models.ForeignKey(CarsLessee,on_delete=models.CASCADE)
    month = models.DateTimeField()
    month_payment = models.CharField(max_length=256)
    def __str__(self):
        return f"{self.lessee.name},{self.month},{self.month_payment}"

