from setuptools import setup


requires = ["requests>=2.14.2"]


setup(
    name='Scraping',
    version='1.0.0',
    description='Awesome library',
    url='https://github.com/whatever/whatever',
    author='Perlverity',
    author_email='your@address.com',
    license='MIT',
    keywords='sample setuptools development',
    packages=[
        "Scraping"
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)