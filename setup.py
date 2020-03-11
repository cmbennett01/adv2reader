from setuptools import setup
import pathlib
import Version

###################################################################

VERSION = Version.version()

NAME = "Adv2reader"

KEYWORDS = ["ADV file reader", 'Astro Digital Video version 2 file reader']

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Science/Research",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    # "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python :: 3.7",
    "Topic :: Scientific/Engineering",
]

INSTALL_REQUIRES = ['numpy']

HERE = pathlib.Path.cwd()

README = (HERE / "README.md").read_text()

setup(
    name=NAME,
    python_requires='>=3.7',
    description='Adv2reader read version 2 Astro Digital Video files.',
    license='License :: OSI Approved :: MIT License',
    url=r'https://github.com/bob-anderson-ok/pyadv2',
    version=VERSION,
    author='Bob Anderson',
    author_email='bob.anderson.ok@gmail.com',
    maintainer='Bob Anderson',
    maintainer_email='bob.anderson.ok@gmail.com',
    keywords=KEYWORDS,
    long_description=README,
    packages=["Adv2reader"],
    package_data={'': ['*.bat']},
    include_package_data=True,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
)