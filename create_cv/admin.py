from django.contrib import admin
from .models import *




class DiplomaAdmin(admin.ModelAdmin):
    list_display  = ('m_diploma','m_user', 'm_year','view_name')
    exclude = ('m_date',)
    #fields = ('id', 'm_diploma','m_year', 'm_user')
    list_filter = ('m_year','m_diploma')
    search_fields = ('m_diploma','m_user__first_name','m_user__username',)


    site_header = 'beefirst'




    def view_name(self, obj):

        print (obj.m_user.first_name)
        return obj.m_user.first_name


        view_name.empty_value_display = '--vide--'
        view_name.admin_order_field  = 'view_name'

admin.site.register(Diploma, DiplomaAdmin)
#admin.site.register(Diploma)

class CompetenceAdmin(admin.ModelAdmin):
    list_display  = ('m_competence','m_user','view_name')
    exclude = ('m_date',)
    #fields = ('id', 'm_diploma','m_year', 'm_user')
    list_filter = ('m_competence',)
    search_fields = ('m_competence','m_user__first_name','m_user__username',)


    site_header = 'beefirst'




    def view_name(self, obj):

        print (obj.m_user.first_name)
        return obj.m_user.first_name


        view_name.empty_value_display = '--vide--'
        view_name.admin_order_field  = 'view_name'
admin.site.register(Competence, CompetenceAdmin)

#admin.site.register(Competence)


class ExperienceAdmin(admin.ModelAdmin):
    list_display  = ('m_poste','m_user','view_name')
    exclude = ('m_date',)
    #fields = ('id', 'm_diploma','m_year', 'm_user')
    list_filter = ('m_poste',)
    search_fields = ('m_poste','m_user__first_name','m_user__username',)


    site_header = 'beefirst'




    def view_name(self, obj):

        print (obj.m_user.first_name)
        return obj.m_user.first_name


        view_name.empty_value_display = '--vide--'
        view_name.admin_order_field  = 'view_name'

admin.site.register(Experience, ExperienceAdmin)
#admin.site.register(Experience)


class LoisirAdmin(admin.ModelAdmin):
    list_display  = ('m_nom','m_niveau','m_user','view_name')
    exclude = ('m_date',)
    #fields = ('id', 'm_niveau','m_year', 'm_user')
    list_filter = ('m_nom','m_niveau')
    search_fields = ('m_nom','m_niveau','m_user__first_name','m_user__username',)


    site_header = 'beefirst'




    def view_name(self, obj):

        print (obj.m_user.first_name)
        return obj.m_user.first_name


        view_name.empty_value_display = '--vide--'
        view_name.admin_order_field  = 'view_name'

admin.site.register(Loisir, LoisirAdmin)
#admin.site.register(Loisir)

#admin.site.register(Cvmodel)
admin.site.register(CvImg)




class CVFolderAdmin(admin.ModelAdmin):

    list_display  = ['view_name',]
    #fields = ('nom', 'image', 'musiques')
    exclude = ('m_date',)
    #list_filter = ('view_name',)
    search_fields = ('m_infoperso_m_profession',)
    site_header = 'beefirst'


    def view_name(self, obj):

        print (obj.m_user.username)
        return obj.m_user.username



        view_name.empty_value_display = '--vide--'
        view_name.admin_order_field  = 'view_name'

    def view_diplomes(self, obj):
        return [m for m in obj.m_diplomas]
        view_diplomes.empty_value_display = '--vide--'
        view_diplomes.admin_order_field  = 'view_diplomes'

    def view_loisirs(self, obj):
        return ",\n".join([m for m in obj.m_loisirs.all()])
        view_loisirs.empty_value_display = '--vide--'
        view_loisirs.admin_order_field  = 'view_loisirs'

    def view_competences(self, obj):
        return ",\n".join([m for m in obj.m_competences.all()])
        view_competences.empty_value_display = '--vide--'
        view_competences.admin_order_field  = 'view_competences'

    def view_references(self, obj):
        return ",\n".join([m for m in obj.m_references.all()])
        view_references.empty_value_display = '--vide--'
        view_references.admin_order_field  = 'view_references'

    def view_experiences(self, obj):
        return ",\n".join([m for m in obj.m_experiences.all()])
        view_experiences.empty_value_display = '--vide--'
        view_experiences.admin_order_field  = 'view_experiences'

    def view_photos(self, obj):
        return ",\n".join([m for m in obj.m_photos.all()])
        view_photos.empty_value_display = '--vide--'
        view_photos.admin_order_field  = 'view_photos'


admin.site.register(CVFolder, CVFolderAdmin)


#admin.site.register(CVFolder)
#admin.site.register(Cvsetting)
# Register your models here.
