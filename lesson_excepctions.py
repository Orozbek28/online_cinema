# try:
#     print(5/0)
#
# except ZeroDivisionError:
#     print('на ноль делить невзя')
#
# num = input('введите число от 1 до 7: ')
#
# if int(num) > 7 or int(num) < 1:
#     raise Exception("ведитье дни недельи от одного до семьи")
#
# days_of_week = {
#     '1':'mon',
#     '2':'tu',
#     '3':'we',
#     '4':'th',
#     '5':'fr',
#     '6':'sa',
#     '7':'sun'
# }
# print(days_of_week[num])
import datetime


class PersonAgeException(Exception):
    def __init__(self,age,message=None):
        self.age = age
        self.messege = message


    def __str__(self):
        if self.messege:
            return self.messege
        return f'ведёный вами  возраст {self.age} не соатвецтвует реальному возросту  {self.age} не должно быть менше 0'



def get_birth_year(age):
    age = int(age)
    if age < 0:
        raise PersonAgeException(age)
    this_year = datetime.date.today()
    birt_year = this_year.year - age
    return birt_year



if __name__=='__main__':
    errors = dict()
    while True:
        age = input('ведитье ваш возрост: ')
        try:
            birth_year = get_birth_year(age)
        except PersonAgeException as e:
           errors['error'] = e
        except ValueError:
            print('водитье числовые значения')
        else:
            print(birth_year)
            break
        finally:
            print(errors)