from django.shortcuts import render

def main_page(request):
    content_data = {}
    return render(
            request,
            'index.html',
            content_data
        )
