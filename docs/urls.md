# Django URLs

Django urls are used to provide access to views. Each URL a user types in a browser maps to a specific view. To map view to a url, we need to add a link to it in `urlpatterns`.  
To make a project more modular, we do not add URLs directly to project `urls` file. Instead, we **include** the URLs from a specific module using `include`.  
```python
from django.conf.urls import include
```  
After that we can include all the module URLs by adding the following entry to `urlpatterns`:  
```python
url(r'^modulename/', include('modulename.urls')),
```  
Then we are writing module-specific URLs in `urls.py` file of the corresponding module.