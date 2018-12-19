from django.contrib import admin
from .models import UserProjects, UserExperiments, ExpSupplies, ExpToDo, ExpEquip, ProjectDocs, LastSeen, ProjectMember

admin.site.register(UserProjects)
admin.site.register(UserExperiments)
admin.site.register(ExpSupplies)
admin.site.register(ExpToDo)
admin.site.register(ExpEquip)
admin.site.register(ProjectDocs)
admin.site.register(LastSeen)
admin.site.register(ProjectMember)

