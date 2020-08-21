import webbrowser as wb

def webauto():

    URLS = (
        'https://www.youtube.com',
        "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox",

    for url in URLS:
        print("Opening "+url)
        wb.open(url)


webauto()        