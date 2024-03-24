import requests


def cat():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
    return data.get('image')

    if __name__ == '__main__':
        cat()


#на самом деле хотел чтобы здесь показывался кот, а не лиса. надеюсь смогу исправить в дальнейщем.

#def brave():
    #url = 'https://random.onl/superhero-generator/flof/'
    #response = requests.get(url)
    #if response.status_code:
        #data = response.json()
    #return data.get('image')





