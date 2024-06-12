from django.contrib import admin
from .models import ChaiVarity, ChaiReview, Store, ChaiCertificate



class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2


class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'type', 'offer')
    inlines = [ChaiReviewInline ]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)
    search_fields = ('name', 'location')

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date', 'valid_until')
    search_fields = ('chai__name', 'certificate_number')
    date_hierarchy = 'issued_date'

admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)