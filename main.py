import urllib.request

def traffic_mark():
    """Вытаскивает значение пробок с сайта Екатеринбурга"""
    url = "http://www.ekburg.ru/information/probki/"
    f = urllib.request.urlopen(url)
    s = f.read()
    text = str(s)
    value_litter = text.find('road')
    value = int(text[text.find('</a>', value_litter)+4:text.find('</a>', value_litter)+5])
    print(value)
    return value

def speed (value):
    list_of_speed = [90, 82, 76, 66, 55, 45, 35, 18, 10, 3]
    return int(list_of_speed[value])

def time (distance):
    return 60*float((distance/speed(value)))

     #<a href="/information/probki/">Пробки:</a> 100rv 10-30 литров бензина