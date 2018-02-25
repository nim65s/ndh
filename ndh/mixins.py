from django.contrib.auth.mixins import UserPassesTestMixin


class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class NDHFormMixin(object):
    template_name = 'ndh/base_form.html'
    title = ''

    def get_context_data(self, **kwargs):
        return super().get_context_data(title=self.title, **kwargs)
