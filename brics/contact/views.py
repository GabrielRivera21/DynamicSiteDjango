from django.views.generic import FormView

from .forms import ContactForm

from ..home.models import Footer

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = '/contact'

    def form_valid(self, form):
        form.send()
        context = self.get_context_data()
        context['success'] = "Successfully sent the message."
        return self.render_to_response(context=context)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['request'] = self.request

        footers = Footer.objects.filter(is_active=True).order_by('order')[:3]
        if len(footers) > 0:
            context['footer_col_count'] = footers
        return context
