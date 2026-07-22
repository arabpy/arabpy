"""
Setup configuration for ArabPy package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="arabpy",
    version="1.0.0",
    author="ArabPy Contributors",
    author_email="info@arabpy.org",
    description="Write Python completely in Arabic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arabpy/arabpy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Internationalization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Natural Language :: Arabic",
    ],
    python_requires=">=3.8",
    keywords="python arabic translation localization i18n l10n",
    project_urls={
        "Bug Reports": "https://github.com/arabpy/arabpy/issues",
        "Source": "https://github.com/arabpy/arabpy",
        "Documentation": "https://arabpy.readthedocs.io/",
    },
)
