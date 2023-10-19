from register.models import CustomUser
from datetime import date


user = CustomUser.objects.get(id=1)

joined = user.date_joined
str_date = joined.strftime("%m:%d:%Y-%H:%M:%S")

today = date.today()
str_today = today.strftime("%m:%d:%Y-%H:%M:%S")

if str_today > str_date:
    print('deu')
else:
    print('nao deu')


'''from datetime import date
today = date.today()
print(today)'''