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
    if time_value>60:
        hour = int(time_value / 60)
        time_text = str((time_value / 60))
        minute = str(60 * int(time_text[time_text.find('.')+1:]))
        return print("Вы доберетесь за", hour, "часов", minute[:2], "минут")
    else:
        time_text = str((time_value / 60))
        minute = str(60 * int(time_text[time_text.find('.')+1:]))
        return print("Вы доберетесь за",minute[:2], "минут")



def main():
    speed(traffic_mark())
    print(speed(traffic_mark()))
    correct_time(100)


main()
# <a href="/information/probki/">Пробки:</a> 100rv 10-30 литров бензина
