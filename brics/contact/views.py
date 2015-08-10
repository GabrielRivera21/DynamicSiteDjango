from django.views.generic import FormView

from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = '/contact'

    def form_valid(self, form):
        form.send()
        context = self.get_context_data()
        context['success'] = "Successfully sent the message."
        return self.render_to_response(context=context)