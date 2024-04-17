import json

def get_articles():
    # открываем файл для чтения
    with open("articles.json", "r", encoding="utf-8") as json_file:
        articles_data = json.load(json_file)
        
    # возвращаем данные
    return articles_data

def save_articles(name, text):
    # получаем все статьи
    articles = get_articles()

    # добавить статью в словарь по ключу name
    
    articles[name] = text

    # открываем файл для записи и переписываем

    with open("articles.json", "w", encoding="utf-8") as json_file:
        json.dump(articles, json_file, ensure_ascii=False)

def delete_articles(name):

    articles = get_articles()

    del articles[name]

    with open("articles.json", "w", encoding="utf-8") as json_file:
        json.dump(articles, json_file, ensure_ascii=False)




if __name__ == "__main__":
    
    print(save_articles("имя", "текст текст текст"))
    print(get_articles())
    print(delete_articles("Персидская кошка"))