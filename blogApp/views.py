import datetime
from django.http import HttpResponse, HttpResponseRedirect

from blogApp.forms import EditPost
from .models import Post, Category
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic.dates import MonthArchiveView
from django.utils.decorators import method_decorator
from blog.decorators import group_required


@login_required
def index(request):
    context = {'post_list': Post.published.all()}
    return render(request, 'blogApp/index.html', context)


@login_required
def post(request, post_id):
    p = get_object_or_404(Post, id = post_id, status = 2)
    output = p
    context = {'post': p}
    return render(request, 'blogApp/post.html', context)


@login_required
def category(request, category_id):
    c = get_object_or_404(Category, id = category_id)
    posts = c.post_set.filter(status=2)
    context = {'category': c, 'post_list': posts}
    return render(request, 'blogApp/category.html', context)


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.filter(status=2)
    date_field = "pub_date"
    allow_future = True
    template_name = "blogApp/posts_by_month.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@login_required
@group_required('admin')
def draft(request):
    context = {'post_list': Post.drafted.all(), 'draft': True}
    return render(request, 'blogApp/index.html', context)


@login_required
@group_required('admin')
def editPost(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    post_instance = get_object_or_404(Post, pk=pk)
    form_return = ""

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = EditPost(instance=post_instance, data=request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #post_instance.due_back = form.cleaned_data['renewal_date']
            form.save()

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = EditPost(instance=post_instance)

    context = {
        'form': form,
        'book_instance': post_instance,
    }

    return render(request, 'BlogApp/edit.html', context)
