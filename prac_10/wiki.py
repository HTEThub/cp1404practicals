import wikipedia

search_phrase = input("What do you want to search on wiki? (Enter blank to end search) >>> ")
while search_phrase.strip() != "":
    print("This may take some time...")
    search_results = wikipedia.search(search_phrase, results=3)
    print(search_results)
    try:
        result_page = wikipedia.page(search_results[0])
        print(result_page.title)
        print(wikipedia.summary(result_page, sentences=1))
        print(result_page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.PageError:
        print("Page not found.")
    search_phrase = input("What do you want to search on wiki? >>> ")
