=====
analytics
=====

analytics is a simple Django app to conduct Web-based analytics. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "analytics" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'analytics',
    ]

2. Include the analytics URLconf in your project urls.py like this::

    url(r'^analytics/', include('analytics.urls')),

3. Run `python manage.py migrate` to create the analytics models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a analytics (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/analytics/ to participate in the analytics.
