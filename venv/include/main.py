import requests
from bs4 import BeautifulSoup



def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_prior(html):   # Количество всех приоритетов
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='tablesaw tablesaw-stack tablesaw-sortable').find('tbody').\
        find_all('tr', title='Допущено')

    tds_data_prior = []

    for tr in trs:
        td = tr.find('td').next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        tds_data_prior.append(td)
    return tds_data_prior


def get_upper_marks(html, mark):    # Количество приоритетов выше моего балла
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='tablesaw tablesaw-stack tablesaw-sortable').find('tbody').\
        find_all('tr', title='Допущено')

    tds_data_upper = []
    for tr in trs:
        td_n = tr.find('td').get_text()
        td_k = tr.find('td').next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        td_mark = tr.find('td').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        td_quota = tr.find('td').next_sibling.next_sibling.next_sibling.next_sibling.\
        next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        if float(td_mark) <= float(mark) and td_quota == '—':
            print(td_n + " <- Your number ")
            break
        tds_data_upper.append(td_k)
    return tds_data_upper


def get_upper_marks_with_my_prior(html, mark):    # Сравнение балла тех кто выше с моим с учетом моего приоритета
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', class_='tablesaw tablesaw-stack tablesaw-sortable').find('tbody').\
        find_all('tr', title='Допущено')

    tds_data_upper = []
    prior = input("Введите приоритет который вы задали")
    for tr in trs:
        td_n = tr.find('td').get_text()
        td_k = tr.find('td').next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        td_mark = tr.find('td').next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        td_quota = tr.find('td').next_sibling.next_sibling.next_sibling.next_sibling. \
            next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.get_text()
        if float(td_mark) <= float(mark) and td_quota == '—':
            break
        if td_k.strip() == 'К' or td_k.strip() <= str(prior):
            tds_data_upper.append(td_k)

    return tds_data_upper


def counter(text, list = [6] ,*args):   # Вывод значений. Значение К (означає участь заяви
    countK = [0, 0, 0, 0, 0, 0, 0, 0]   # в конкурсі тільки на контракт) выводится как 8
    for k in list:
        if k.strip() == '1':
            countK[0] += 1
        elif k.strip() == '2':
            countK[1] += 1
        elif k.strip() == '3':
            countK[2] += 1
        elif k.strip() == '4':
            countK[3] += 1
        elif k.strip() == '5':
            countK[4] += 1
        elif k.strip() == '6':
            countK[5] += 1
        elif k.strip() == '7':
            countK[6] += 1
        elif k.strip() == 'К':
            countK[7] += 1
    print(text)
    for item in countK:
        print(str(countK.index(item) + 1) + ":" + str(item))


def counterWsum(text, list = [6] ,*args):   # Вывод значений. Без учета контракта
    countK = [0, 0, 0, 0, 0, 0, 0]
    for k in list:
        if k.strip() == '1':
            countK[0] += 1
        elif k.strip() == '2':
            countK[1] += 1
        elif k.strip() == '3':
            countK[2] += 1
        elif k.strip() == '4':
            countK[3] += 1
        elif k.strip() == '5':
            countK[4] += 1
        elif k.strip() == '6':
            countK[5] += 1
        elif k.strip() == '7':
            countK[6] += 1
    print(text)
    sum = 0
    for item in countK:
        print(str(countK.index(item) + 1) + ":" + str(item))
        sum += item
    print("Sum is " + str(sum))



def main():
    # zno_url = 'http://vstup.info/2019/174/i2019i174p538556.html'
    zno_url = input("Введите ссылку на страницу статистики")

    mark = input("Введите ваш балл на эту специльность  (например вот так 167.950)")
    all_prior_data = get_all_prior(get_html(zno_url))

    all_upper_data = get_upper_marks(get_html(zno_url), mark)

    all_upper_with_prior_data = get_upper_marks_with_my_prior(get_html(zno_url),mark)

    counter("Все приоритеты", all_prior_data)

    counter("Приоритеты надо мной", all_upper_data)

    counterWsum("Приоритеты надо мной с учетом моего приоритета", all_upper_with_prior_data)






if __name__ == '__main__':
    main()
