import requests


def execute():
    # the required first parameter of the 'get' method is the 'url':
    x = requests.get('https://w3schools.com/python/demopage.htm')

    # print the response text (the content of the requested file):
    print(x.text)


if __name__ == "__main__":
    execute()
