from django.views.generic import TemplateView


class ProductHomeView(TemplateView):
    template_name = 'product/_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün Süreç Yönetimi'
        context['app_name'] = 'product'
        return context


class ProductDetailGenelView(TemplateView):
    template_name = 'product/product_detail_general.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün Detay - Genel'
        context['app_name'] = 'product'
        context['active_tab'] = 'genel'
        return context


class ProductDetailNotlarView(TemplateView):
    template_name = 'product/product_detail_notes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün Detay - Notlar'
        context['app_name'] = 'product'
        context['active_tab'] = 'notlar'
        return context


class ProductDetailSmmView(TemplateView):
    template_name = 'product/product_detail_smm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün Detay - SMM'
        context['app_name'] = 'product'
        context['active_tab'] = 'smm'
        return context


class ProductDetailKaliteView(TemplateView):
    template_name = 'product/product_detail_quality.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün Detay - Kalite'
        context['app_name'] = 'product'
        context['active_tab'] = 'kalite'
        return context


class ProductDetailKampanyaView(TemplateView):
    template_name = 'product/product_detail_campaign.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün Detay - Kampanya'
        context['app_name'] = 'product'
        context['active_tab'] = 'kampanya'
        return context


class ProductDetailHareketView(TemplateView):
    template_name = 'product/product_detail_logs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün Detay - Hareket'
        context['app_name'] = 'product'
        context['active_tab'] = 'hareket'
        return context

class ProductAddNewView(TemplateView):
    template_name = 'product/product_add_new.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Yeni Ürün Ekle'
        context['app_name'] = 'product'
        return context
    
class ProductKategoriView(TemplateView):
    template_name = 'product/product_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün Kategorileri'
        context['app_name'] = 'product'
        return context

class ProductSuppliersView(TemplateView):
    template_name = 'product/product_suppliers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün Tedarikçileri'
        context['app_name'] = 'product'
        return context
    
class ProductSmmExpensesView(TemplateView):
    template_name = 'product/smm_expenses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Ürün SMM Yıllık Giderler'
        context['app_name'] = 'product'
        return context
