from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Anasayfa'
        return context


class HomeView(TemplateView):
    template_name = 'app_toplanti/_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Anasayfa'
        context['app_name'] = 'app_toplanti'
        return context


class MeetingDetailView(TemplateView):
    template_name = 'app_toplanti/meeting_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Toplantı Detayı'
        context['app_name'] = 'app_toplanti'
        return context


class MeetingCreateView(TemplateView):
    template_name = 'app_toplanti/meeting_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Yeni Toplantı'
        context['app_name'] = 'app_toplanti'
        return context


class MeetingActiveView(TemplateView):
    template_name = 'app_toplanti/meeting_active.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Aktif Toplantılar'
        context['app_name'] = 'app_toplanti'
        return context


class MeetingCompletedView(TemplateView):
    template_name = 'app_toplanti/tasks_completed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Tamamlanan Toplantılar'
        context['app_name'] = 'app_toplanti'
        return context


class TasksView(TemplateView):
    template_name = 'app_toplanti/tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Görevler'
        context['app_name'] = 'app_toplanti'
        return context


class TaskCompletedView(TemplateView):
    template_name = 'app_toplanti/tasks_completed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Tamamlanan Görevler'
        context['app_name'] = 'app_toplanti'
        return context


class TaskCreateView(TemplateView):
    template_name = 'app_toplanti/task_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Görev Oluştur'
        context['app_name'] = 'app_toplanti'
        return context
