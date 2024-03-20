from django.http import HttpResponseNotFound
from .models import Post, Likes
from .form import CommentsForm
from .models import Comments
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import render
from .models import CommentLike

class PostView(View):
    '''вывод записей'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/dlog.html', {'post_list': posts})


class PostDetail(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})

class AddComments(View):
    '''добавление комментариев'''
    def post(self, request, pk,):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


class EditComment(View):
    '''Редактирование комментариев'''
    def get(self, request, comment_id):
        comment = get_object_or_404(Comments, id=comment_id)
        form = CommentsForm(instance=comment)
        return render(request, 'blog/edit_comment.html', {'form': form, 'comment_id': comment_id})

    def post(self, request, comment_id):
        comment = get_object_or_404(Comments, id=comment_id)
        form = CommentsForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            # Перенаправление на страницу blog_detail.html после успешного редактирования комментария
            return redirect('post_detail', pk=comment.post_id)
        else:
            return render(request, 'blog/edit_comment.html', {'form': form, 'comment_id': comment_id})



class DeleteComment(View):
    '''удаление комментария'''

    def get(self, request, comment_id):
        comment = get_object_or_404(Comments, id=comment_id)

        # Проверяем наличие комментария
        if comment:
            # Дополнительные проверки, если необходимо
            post_id = comment.post_id
            comment.delete()
            return redirect(f'/{post_id}')
        else:
            # Обработка случая, если комментарий не найден
            return HttpResponseNotFound("Comment not found.")
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')


class AddCommentLike(View):
    def get(self, request, comment_id):
        ip_client = get_client_ip(request)
        try:
            CommentLike.objects.get(ip=ip_client, comment_id=comment_id)
            return redirect('post_detail', pk=Comments.objects.get(id=comment_id).post_id)
        except CommentLike.DoesNotExist:
            new_like = CommentLike(ip=ip_client, comment_id=comment_id)
            new_like.save()
            return redirect('post_detail', pk=Comments.objects.get(id=comment_id).post_id)

class DelCommentLike(View):
    def get(self, request, comment_id):
        ip_client = get_client_ip(request)
        try:
            lik = CommentLike.objects.get(ip=ip_client, comment_id=comment_id)
            lik.delete()
        except CommentLike.DoesNotExist:
            pass
        return redirect('post_detail', pk=Comments.objects.get(id=comment_id).post_id)


