from django.views.generic import TemplateView

from .models import CarouselImage, Feature, AboutUs


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        carousels = CarouselImage.objects.filter(is_active=True).order_by('order')
        if len(carousels) > 0:
            context['carousel'] = carousels
            context['carousel_count'] = range(1, len(carousels))

        features = Feature.objects.filter(is_active=True).order_by('order')[:3]
        if len(features) > 0:
            context['feature'] = features
            context['feature_count'] = len(context['feature'])

        return context


class AboutUsView(TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['abouts'] = AboutUs.objects.filter(is_active=True).order_by('order')

        return context
