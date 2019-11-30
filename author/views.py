from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm


# Create your views here.
def home(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        # return render(request, "base.html", {"title": "home"})
        return redirect('/authors/')
    else:
        return redirect("/logout/")


def author(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        if request.method == "POST":
            author = Author()
            form = AuthorForm(request.POST, request.FILES, instance=author)
            if form.is_valid():
                form.save()
            authors = Author.objects.all()
            return render(request, "authors.html", {"title": "Author", "records": authors})
        else:
            form = AuthorForm()
            return render(request, "create_author.html", {"form": form})
    else:
        return redirect("/logout/")


def author_details(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        authors = Author.objects.all()
        return render(request, "authors.html", {"title": "Event", "records": authors})
    else:
        return redirect("/logout/")


def author_display(request, id):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        print(request.user)
        author = Author.objects.filter(pk=id).first()
        return render(request, "display_author.html", {"title": "Event", "record": author})
    else:
        return redirect("/logout/")



def contact_page(request):
    #! /usr/bin/env python
    from bs4 import BeautifulSoup
    import re
    import difflib
    from urllib.request import urlopen
    import re 
    import itertools
    if request.method == "POST":
        print("Hello")
        base_url = request.POST['url']
        if base_url:
        
            # urls = ['https://en.xlpat.com/','https://www.zapbuild.com/','http://www.ultratechcement.com/','https://www.chicmic.in/']
            # base_url = urls[3]
            # html_page = urlopen("https://arstechnica.com")
            html_page = urlopen(base_url)

            # for link in soup.find_all('a'):    # extract link url from the anchor    anchor = link.attrs[“href”] if “href” in link.attrs else ‘’

            soup = BeautifulSoup(html_page)
            links = []

            for link in soup.findAll('a', attrs={'href': re.compile("^")}):
                links.append(link.get('href'))

            contact_url = []
            for link in links:
                if 'contact' in link: 
                    contact_url.append(link)

            contact_urls = list(set(contact_url))

            print("=========================")
            print(contact_urls)
            print("=========================")


            from nltk import ne_chunk, pos_tag, word_tokenize
            from nltk.tree import Tree
            import nltk
            # nltk.download('punkt')
            # nltk.download('averaged_perceptron_tagger')
            nltk.download('maxent_ne_chunker')

            contact_url = []
            for contact in contact_urls:
                regex1 = re.compile(r'^(?:http|ftp)s?://', re.IGNORECASE) # http or https
                regex2 = re.compile(r'(?:/?|[/?]\S+)$', re.IGNORECASE) # internal links
                print(re.match(regex1, contact) is not None)
                if re.match(regex1, contact) is not None:
                    contact_url = contact
                
                if re.match(regex2, contact) is not None:
                    contact_url = base_url + ""+ contact.replace("/", "")
                # if re.match("")
                    # contact_url = base_url
                
            print("contact_url ==>> : " + str(contact_url))
            return render(request, "authors.html", {"contact_url": contact_url, "url": base_url})
    return render(request, "authors.html", {"title": "Event", "url": ''})

    # words = ['Addesses', 'Address', 'Office']
    # if contact_url:
    #     html_page = urlopen(contact_url)
    #     soup = BeautifulSoup(html_page)
    #     rows = soup.find_all('div')
    #     print("====================")
    #     addresses = []
    #     for row in rows:          
    #         # print(row.get_text())
    #         if any(word in row.get_text() for word in words):
    #             # print("Shiv Shankar")
    #             # print(get_continuous_chunks(row.get_text()))
    #             addresses.append(get_continuous_chunks(row.get_text()))
    #                     # # print(row.get_text())

    # print (addresses)
    # print ("")
    # addresses.sort()
    # addresses = list(k for k,_ in itertools.groupby(addresses))
    # # addresses = set(addresses)
    # print(addresses)
    # return True


def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk

