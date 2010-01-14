from setuptools import setup, find_packages

setup(
    name="django-events",
    version='0.1',
    description='Simple Event Management for Django',
    author='Micah Ransdell',
    author_email='mjr578@gmail.com',
    url='http://github.com/micahr/django-events/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data = {
        'events': [
            'templates/*.html',
            'templates/partials/*.html',
        ],
        'json': [
            'templates/json/*.json',
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
