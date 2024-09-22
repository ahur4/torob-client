from setuptools import setup, find_packages

long_description = open('README.md', 'r').read()

setup(
    name="torob-client",
    version="1.0",
    description="A Python client for interacting with the Torob API to fetch products data.",
    author="Ahur4",
    author_email="ahur4.rahmani@gmail.com",
    url="https://github.com/ahur4/torob-client",
    packages=find_packages(include=['torob_client', 'torob_client.*']),
    install_requires=[
        "requests==2.32.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=[
        "webscraping", "crawling", "data science", "data analyse"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
