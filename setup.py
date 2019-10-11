from setuptools import setup
import os

def read(*names):
    return open(os.path.join(os.path.dirname(__file__), *names)).read()

setup(
    name="dfly-breathe",
    version="0.1.0",
    description="Dragonfly command API",
    author="Mike Roberts",
    author_email="mike.roberts.2k10@googlemail.com",
    license="LICENSE.txt",
    url="https://github.com/mrob95/Breathe",
    long_description = read("README.md"),
    long_description_content_type='text/markdown',
    packages=["breathe"],
    install_requires=["dragonfly2"],
    classifiers=[
                   "Environment :: Win32 (MS Windows)",
                   "Environment :: X11 Applications",
                   "Development Status :: 3 - Alpha",
                   "License :: OSI Approved :: "
                   "GNU Library or Lesser General Public License (LGPL)",
                   "Operating System :: Microsoft :: Windows",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.7",
                  ],
)

