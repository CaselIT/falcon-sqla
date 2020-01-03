import imp
import os.path
from setuptools import setup, find_packages


HERE = os.path.abspath(os.path.dirname(__file__))

VERSION = imp.load_source(
    'version', os.path.join(HERE, 'falcon_sqla', 'version.py'))
VERSION = VERSION.__version__

DESCRIPTION = 'Middleware for integrating Falcon applications with SQLAlchemy.'
with open(os.path.join(HERE, 'README.rst')) as readme_file:
    LONG_DESCRIPTION = readme_file.read()

REQUIRES = [
    'falcon >= 2.0.0',
    'SQLAlchemy >= 1.3.0',
]
EXTRAS_REQUIRE = {
    'test': [
        'pytest',
        'pytest-cov',
    ],
}


setup(
    name='falcon_sqla',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='falcon wsgi database middleware orm sqlalchemy',
    author='Vytautas Liuolia',
    author_email='vytautas.liuolia@gmail.com',
    url='https://github.com/vytas7/falcon-sqla',
    license='Apache 2.0',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.5',
    install_requires=REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
