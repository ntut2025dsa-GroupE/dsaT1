from django.http import HttpResponse


def home_page_view(request):
    abc = ("Welcome to Group E Page!\nGroup Members:\n— 余俊明 (112370117)\n— 朱庭寬 (112370210)\n— 林彥廷 (112370219)\n— 黃昭亮 (112370232)")
    
    return HttpResponse(abc, content_type="text/plain; charset=utf-8")

    # ("Welcome to Group E Page!")
    # ("Group Members:")
    # ("— 余俊明 (112370117)")
    # ("— 朱庭寬 (112370210)")
    # ("— 林彥廷 (112370219)")
    # ("— 黃昭亮 (112370232)")
    
    
