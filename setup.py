from distutils.core import setup

setup(
    name='django-decorators',
    version='0.1.2',
    author='Julian Amaya, Allan James Vestal',
    author_email='ajvestal@journalsentinel.com',
    packages=['django_decorators'],
    url='http://github.com/datahub/django-decorators',
    license='LICENSE.md',
    description='A bunch of django extra decorators.',
    long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.1.1",
    ],
)
