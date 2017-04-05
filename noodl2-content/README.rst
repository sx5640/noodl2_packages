=====
content
=====

content is a simple Django app to conduct Web-based content. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "content" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'content',
    ]

2. Include the content URLconf in your project urls.py like this::

    url(r'^content/', include('content.urls')),

3. Run `python manage.py migrate` to create the content models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a content (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/content/ to participate in the content.
