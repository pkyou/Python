#encoding:UTF-8
import urllib.request 


if __name__ == "__main__":
    page = 2
    url = "http://tieba.baidu.com/f?kw=%B3%A4%B0%B2%B4%F3%D1%A7"
    data = urllib.request.urlopen(url).read()#
    data = data.decode('UTF-8')
    print(data)
    print("hello pkyou. I love you baby")