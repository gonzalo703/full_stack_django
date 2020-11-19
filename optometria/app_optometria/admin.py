from django.contrib import admin

# Register your models here.
def test(num):
    return num, num*2, num*4



print(test(5))