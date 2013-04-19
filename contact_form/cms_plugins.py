from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class ContactApp(CMSApp):
    name = _("Django Contact Form Apphook")
    urls = ["contact_form.urls"]

apphook_pool.register(ContactApp)
