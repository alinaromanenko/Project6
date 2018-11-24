import urllib.request


def traffic_mark():
    """Вытаскивает значение пробок с сайта Екатеринбурга"""
    url = "http://www.ekburg.ru/information/probki/"
    f = urllib.request.urlopen(url)
    s = f.read()
    text = str(s)
    value_litter = text.find('road')
    value = int(text[text.find('</a>', value_litter) + 4:text.find('</a>', value_litter) + 5])
    return value


def speed(value):
    list_of_speed = [90, 82, 76, 66, 55, 45, 35, 18, 10, 3]
    return int(list_of_speed[value - 1])


def time(distance):
    return 60 * float((distance / speed(traffic_mark())))


def correct_time(distance):
    time_value = time(distance)
    hour = int(time_value / 60)
    time_text = str((time_value / 60))
    minute = str(60 * int(time_text[time_text.find('.')+1:]))
    return hour, int(minute[:2])


def correct_case(distance):
    hour, minute_ = correct_time(distance)
    minute = int(str(minute_)[1])
    if minute == 2 or minute == 3 or minute == 4:
        minute_case='минуты'
    elif minute == 1:
        minute_case='минуту'
    else:
        minute_case='минут'
    if hour==0:
        return print("Вы доберетесь за", minute_, minute_case)
    else:
        if hour == 2 or hour == 3 or hour == 4:
            hour_case = 'часа'
        elif hour == 1:
            hour_case = 'час'
        else:
            hour_case = 'часов'
        return print("Вы доберетесь за", hour, hour_case, minute_, minute_case)


def main():
    speed(traffic_mark())
    print(speed(traffic_mark()))
    correct_case(100)



main()
# <a href="/information/probki/">Пробки:</a> 100rv 10-30 литров бензина
