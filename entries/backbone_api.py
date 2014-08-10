import backbone
from backbone.views import BackboneAPIView
from models import Entry


class EntryAPIView(BackboneAPIView):
    def date(self, obj):
        return 'Fecha: %s/%s/%s' % (obj.pub_date.day, obj.pub_date.month, obj.pub_date.year)

    def user(self, obj):
        try:
            return 'Usuario: %s' % obj.user.username
        except:
            return 'Usuario: Anonimo'

    def body(self, obj):
        return '%s...' % obj.body[:150]

    model = Entry
    display_fields = ('date', 'title', 'slug', 'body', 'user',) # Campos para solicitudes GET
    fields = ('title', 'slug', 'body', 'user', 'pub_date',)# Campos que permiten POST o PUT
    ordering = ('id',) # Orden en que se recuperara la Coleccion
    paginate_by = 10 # Numero maximo de objectos que retornara por peticion GET

    def queryset(self, request):
        return Entry.objects.all().order_by('-pub_date')

    def has_delete_permission(self, request, obj):
        return False

backbone.site.register(EntryAPIView)


class DetailEntryView(BackboneAPIView):
    def date(self, obj):
        return 'Fecha: %s/%s/%s - %s:%s:%s' % (obj.pub_date.day, obj.pub_date.month, obj.pub_date.year, obj.pub_date.hour, obj.pub_date.minute, obj.pub_date.second)

    def user(self, obj):
        try:
            return 'Usuario: %s, %s %s. %s' % (obj.user.username, obj.user.first_name, obj.user.last_name, obj.user.email)
        except:
            return 'Usuario: Anonimo'

    model = Entry
    display_fields = ('date', 'title', 'slug', 'body', 'user',) # Campos para solicitudes GET
    fields = ('title', 'slug', 'body', 'user', 'pub_date',)# Campos que permiten POST o PUT
    ordering = ('id',) # Orden en que se recuperara la Coleccion
    url_slug = 'entry1'

backbone.site.register(DetailEntryView)
