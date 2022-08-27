from setuptools import setup, find_packages

setup(
    name='project',
    version='0.0.1',
    description='Project Description',
    author='Thapelo Tsotetsi',
    author_email='info@example.com',
    url='http://example.com',
    install_requires=[
        'Django',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
)
