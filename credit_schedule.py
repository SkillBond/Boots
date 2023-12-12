import datetime as dt
from prettytable import PrettyTable

def validate(amount, percent, time, date):
    try:
        if type(amount) == bool:
            return "Сумма должна быть числом"
        float(amount)
        if amount < 0:
            return "Сумма должна быть больше нуля"
    except ValueError:
        return "Сумма должна быть числом"
    except TypeError:
        return "Сумма должна быть числом"
    try:
        if type(percent) == bool:
            return "Процент должен быть числом"
        float(percent)
        if percent < 0:
            return "Процент должен быть больше нуля"
    except ValueError:
        return "Процент должен быть числом"
    except TypeError:
        return "Процент должен быть числом"
    try:
        if type(time) == bool:
            return "Время должно быть числом"
        int(time)
        if time < 0:
            return "Время должно быть больше нуля"
    except ValueError:
        return "Время должно быть числом"
    except TypeError:
        return "Время должно быть числом"
    try:
        date = dt.datetime.strptime(date, "%d-%m-%Y")
    except:
        return "Неверная дата"
    return True

def credit_schedule(amount, percent, time, date):
    validation = validate(amount, percent, time, date)
    if validation == True:
        date = dt.datetime.strptime(date, "%d-%m-%Y")
        remainder = amount
        data = []
        for month in range(time):
            overpayment = round((remainder/percent)/12, 2)
            payment = round(amount/time, 2)
            fee = round(payment + overpayment, 2)
            remainder = round(remainder - payment, 2)
            date += dt.timedelta(days=30)
            if remainder < 0.05:
                remainder = 0
            data.append({"date": dt.datetime.strftime(date, "%d-%m-%Y"), "overpayment": overpayment, "payment": payment, "fee": fee, "remainder": remainder})
    else:
        return validation
    return data

def table_view(data):
    table = PrettyTable()
    table.field_names = list(data[0].keys())
    for element in data:
        table.add_row(element.values())

    return table
