#!/usr/bin/env python
import lib
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(
    name='learnpython',
    description='Terminal Based Python tutorials.',
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],

    keywords='weather',
    version=lib.__version__,
    author=lib.__author__,
    author_email=lib.__author_email__,
    maintainer=lib.__maintainer__,
    maintainer_email=lib.__maintainer_email__,
    url=lib.__url__,
    license='MIT',
    packages=['lib'],
    entry_points={
        'console_scripts': [
            'learnpython = lib.tasker:main',
        ]
    },
)
