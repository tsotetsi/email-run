from setuptools import setup, find_packages

setup(
    name='project',
    version='0.0.1',
    description='Mail Service API',
    author='Thapelo Tsotetsi',
    author_email='info@example.com',
    url='http://mail-run.com',
    install_requires=[
        'Django',
        'django-model-utils',
        'djangorestframework',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
)
