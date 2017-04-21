#encoding:UTF-8
import urllib


if __name__ == "__main__":
    page = 2
    url = "http://www.qiushibaike.com/hot/"
    request = urllib.request(url)
    response = urllib.request.urlopen(request)
    print(response.read())
    print("hello pkyou. I love you baby")