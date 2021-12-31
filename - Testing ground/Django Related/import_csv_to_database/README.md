# Import Export With Django

This will demonstrate some of the ways to do import and export in Django that I use for this particular case.

## Via Django shell
The most straightforward way to import your data into Django database is by using `manage.py shell`. This is good especially if all you want to do is one time importing, and pretty simple to do. Just open Django shell and type (this is pseudo-code for example only, but the logic is the same):
```
import csv
from .models import YourModel
with open('path_to_csv') as f:
    reader = csv.reader(f)
    for column in reader:
        if column[0] != 'name_of_your_first_header':
            _, created = YourModel.objects.get_or_create(
                db_column_1 = column[0],
                db_column_2 = column[1],
                ...
            )
```
After that double enter and let the script run its courses. Note that you **need to exclude the header completely to avoid unnecessary error** while importing, hence `if column[0] != ...` code exist.


## `django-import-export`
```
pip install django-import-export
```
Link: [GitHub]('https://github.com/django-import-export/django-import-export') | [Docs]('https://django-import-export.readthedocs.io/en/latest/index.html')

This dependencies handle both import and export, and can be integrated to Admin Page. It support multiple formats, such as:
- .csv
- .xls and .xlsx
- .json
- .tsv, and any other formats that [tablib]('https://github.com/jazzband/tablib') support

It could also preview the data that you importing, to make sure nothing wrong in the end-result. And can also export the data in respect to admin filters. Based on my understanding, this dependencies best for **admin-level import and export** rather than client-level.
