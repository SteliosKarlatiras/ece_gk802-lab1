import requests  # εισαγωγή της βιβλιοθήκης
from datetime import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


def server_status(url):
    try:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = 'http://' + url

        r = requests.head(url)
        print("Server Software: " + r.headers.get('Server', 'N/A'))

        cookies = r.cookies
        if cookies:
            print("Cookies: ")
            for cookie in cookies:
                print('Name: ', cookie.name, end="\t\t\t")
                #print('Cookie expire: ', cookie.expires)
                if cookie.expires:
                    seconds = cookie.expires/1000
                    print('Expires: ', datetime.fromtimestamp(seconds).strftime('%Y-%m-%d   '))

        else:
            print("Cookies not found")

    except requests.exceptions.RequestException as e:
        print("Error: ", e)


def main():
    url = input("Enter a URL: ")
    server_status(url)
    # with requests.get(url) as response:  # το αντικείμενο response
    #    html = response.text
    #    more(html)


if __name__ == "__main__":
    main()

main()
