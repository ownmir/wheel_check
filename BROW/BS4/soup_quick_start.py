from bs4 import BeautifulSoup


if __name__ == '__main__':
    with open("D://Work//Py3proj//BS4//alice.html", 'r', encoding='UTF-8') as html:
        for line in html:
            print('Line', line)
        soup = BeautifulSoup (html, 'html.parser')
        print(soup.title)

