from django.shortcuts import render
from .models import User, Project
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.conf import settings
# import simplejson as json
from django.http import JsonResponse



# Create your views here.
def home(request):
    title = "john's Profile"
    projects = Project.get_all()
    image = User.objects.all()

    return render(request,'all_projects/index.html',{
        'title': title,
        'projects':projects,
        
    })

def all_repos(request):
    title = 'Repos'

#     # all_repos = requests.get('https://api.github.com/user/repos?sort=asc&access_token={}'.format(settings.GITHUB_API))
#     # repos = json.loads(all_repos.content)
#     # # print(repos)

    return render(request, 'all_projects/repos.html', {
        'title':title,

    })
