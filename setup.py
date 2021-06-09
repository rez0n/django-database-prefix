import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='django-database-prefix',
    version='0.1.0',
    keywords='django',
    author=u'Denis Verbin <den.verbin@gmail.com',
    packages=['django_database_prefix'],
    url='https://github.com/rez0n/django-database-prefix',
    license='Apache licence, see LICENCE',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    requires=[
        'Django',
    ],
    classifiers=[
        'Framework :: Django',
        'Topic :: Database',
    ]
)