
from setuptools import setup

requires = [
    'Flask',
    'Flask-SQLAlchemy',
    'oursql',
    'flask-cors',
    'flask-testing',
    'requests',
    'pyyaml'
]

setup(
    name='lds',
    version='2.0',
    install_requires=requires
)
