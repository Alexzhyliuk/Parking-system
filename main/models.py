from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car_number = models.CharField("Номер машины", max_length=8)
    birthdate = models.DateField("Дата рождения", blank=True, null=True)
    is_booking = models.BooleanField("Бронирует", default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.car_number}"


class Question(models.Model):

    STATUS_CHOICES = [
        (0, "В ожидании"),
        (1, "Обработан")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField("Вопрос", max_length=500)
    status = models.IntegerField("Статус", choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}: {self.get_status_display()}"


class Parking(models.Model):

    address = models.CharField("Адрес", max_length=255)

    def __str__(self):
        return f"{self.address}"


class ParkingPlaceType(models.Model):

    is_open = models.BooleanField("Открытое", default=True)
    is_cover = models.BooleanField("Крытое", default=False)
    is_near_exit = models.BooleanField("Рядом с выездом", default=False)
    is_near_enter = models.BooleanField("Рядом со входом", default=False)
    is_for_disabled = models.BooleanField("Место для инвалидов", default=False)

    def __str__(self):
        response = f"{'Открытое' if self.is_open else 'Крытое'} - "
        response += f"{'Рядом с выездом - ' if self.is_near_exit else ''}"
        response += f"{'Рядом со входом - ' if self.is_near_enter else ''}"
        response += f"{'Для инвалидов' if self.is_for_disabled else ''}"
        return response


class ParkingPlaceStatus(models.Model):

    status = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.status}"


class ParkingPlace(models.Model):

    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name="places")
    number = models.IntegerField()
    status = models.ForeignKey(ParkingPlaceStatus, on_delete=models.SET_NULL, null=True, related_name="places")
    place_type = models.ForeignKey(ParkingPlaceType, on_delete=models.SET_NULL, null=True, related_name="places")

    def __str__(self):
        return f"{self.number} - {self.parking.address}"


class Preferences(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_any = models.BooleanField("Любое", default=True)
    is_open = models.BooleanField("Открытое", default=False)
    is_cover = models.BooleanField("Крытое", default=False)
    is_near_exit = models.BooleanField("Рядом с выездом", default=False)
    is_near_enter = models.BooleanField("Рядом со входом", default=False)
    is_for_disabled = models.BooleanField("Место для инвалидов", default=False)

    def __str__(self):
        response = f"{'Открытое' if self.is_open else 'Крытое'} - "
        response += f"{'Рядом с выездом - ' if self.is_near_exit else ''}"
        response += f"{'Рядом со входом - ' if self.is_near_enter else ''}"
        response += f"{'Для инвалидов' if self.is_for_disabled else ''}"
        return response


class Log(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="logs")
    parking_place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE, related_name="logs")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} booked {self.parking_place.number}th parking space" \
               f" at {self.parking_place.parking.address}"
