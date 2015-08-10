from django.views.generic import TemplateView

from .models import Service

from ..home.models import Footer


class ServicesView(TemplateView):
    template_name = 'services/service.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_active=True).order_by('order')
        context['request'] = self.request

        footers = Footer.objects.filter(is_active=True).order_by('order')[:3]
        if len(footers) > 0:
            context['footer_col_count'] = footers
        return context
