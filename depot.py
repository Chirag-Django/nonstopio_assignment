locations = ['pune','mumbai','delhi','chennai']
sizes = ['s','l','m','xl']
shapes = ['circle','triangle','square','rectangle']

def extract_info(search_query):
    words = search_query.lower().split()
    for word in words:
        if word in locations:
            loc = word
        elif word in sizes:
            size = word
        elif word in shapes:
            shape = word
        elif word.isdigit():
            price = int(word)
    return loc,size,shape,price
print(extract_info('s circle in pune in 10 rs'))