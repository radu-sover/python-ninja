from setuptools import setup, find_packages

setup(
    name='flaskr',
    version='0.0.1dev',
    packages=find_packages(),
    install_requires=[
        'flask',
        'sqlalchemy'
    ]
)
