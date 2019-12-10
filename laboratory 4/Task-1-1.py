# Написати функцію, яка б по введеному номеру пори року в якості параметра
# (1 - зима, 2 - весна, 3 - літо, 4 - осінь)
# повертала місяці, кількість днів в кожному з місяців, що відповідають цій порі року.

jearset = {
    1: {
        "winter": {
        "december": 31,
        "january": 31,
        "february": {28, 29}
        }
    },
    2: {
        "spring": {
        "march": 31,
        "april": 30,
        "may": 31
        }
    },
    3: {
        "summer": {
        "june": 30,
        "july": 31,
        "august": 31
        }
    },
    4: {
        "autumn": {
        "september": 30,
        "october": 31,
        "november": 30
        }
    }
}

n = 0
while n != 1:
    m = int(input("Enter "))
    def search(jearset, m):
        return jearset[m]
    print(search(jearset, m))
    print("Enter 1 to stop and 0 to continue")
    n = int(input())