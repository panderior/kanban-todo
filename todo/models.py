from django.db import models

'''
    This is the model for Column
    It has 3 atttributes which are:
        1. title: used to specify the title
        2. icon: used to specify which material-icon is used when the column is displayed
        3. pallette: used to specify the type of color bar the column has when displayed (also uses material-pallette)
'''
class Column (models.Model):
    title = models.CharField(max_length=20)
    icon = models.CharField(max_length=20, blank=True, default="filter_none")
    palette = models.CharField(max_length=20, blank=True, default="kanban To-do")

    def __str__(self):
        return self.title


'''
    This is the model for Todo
    It has 6 attributes which are:
        1. title: used to specify the title of the todo
        2. description: used to specify the description of the todo
        3. column: used to specify to which column object the todo instance belongs to (Foriegn Key)
        4. pallette: used to specify the color bar of the todo when displayed (uses material)
        5. link: used to store the external link which corresponds to the todo
        6. attachement: used to specify the file associated with the todo 
'''
class Todo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    palette = models.CharField(max_length=20, blank=True)
    link = models.URLField(max_length=100, blank=True)
    attachment = models.FileField(upload_to="files", blank=True)

    def __str__(self):
        return self.title 