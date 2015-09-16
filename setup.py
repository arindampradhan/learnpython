#!/usr/bin/env python
import learnpython
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
    package_data={'': ['license.txt']},
    include_package_data=True,
    keywords='weather',
    version=learnpython.__version__,
    author=learnpython.__author__,
    author_email=learnpython.__author_email__,
    maintainer=learnpython.__maintainer__,
    maintainer_email=learnpython.__maintainer_email__,
    url=learnpython.__url__,
    license='MIT',
    packages=['learnpython','learnpython.lib','learnpython.problems','learnpython.solutions'],
    entry_points={
        'console_scripts': [
            'learnpython = learnpython.lib.tasker:main',
        ]
    },
)
