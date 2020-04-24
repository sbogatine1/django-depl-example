from django.contrib import admin
from first_app.models import accessRecord, topics, webPage
# Register your models here.
admin.site.register(accessRecord)
admin.site.register(topics)
admin.site.register(webPage)
