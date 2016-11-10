# App initial design and description

### System Architecture

The app will have a **database** use **search API** to get data from the web.  
Data manipulation will be done via Django **models** and **views**.  
On the client side, Django **templates** will be used (with HTML and CSS).

### Wireframes

1. Main page  
    Main page will contain top-5 Categories and Pages, as well as search input field.

2. Category page  
    List of pages in a particular category, search for a page input field.

### URLs

Main page will be accessed via sitename/ or sitename/rango  
Categories will be accessed via sitename/category/< category-name >/

### Entity-Relationship 

The app will have **Categories** that contain **Pages**, so we will have one-to-many relationship between categories and pages.  
Future dev: Probably need to have many-to-many relationship, since a given page can belong to several different categories.  
A user can create and rank categories (and rank pages), so there probably will be some king of relationship between users and categories (and pages).

### Packages for Rango

- Django 1.9.10
- Pillow 
