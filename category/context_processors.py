from .models import Category


def menu_links(request):
    '''
    Function to retrieve menu links from the database.
    '''
    links = Category.objects.all()
    return dict(links=links)