from setuptools import setup, find_packages

setup(
    name="keyword_search",
    version='0.0.2',
    packages=find_packages(),
    author="Frederico Schmitt Kremer",
    author_email="fred.s.kremer@gmail.com",
    description="A keyword search for CSV/Excel/Pandas",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    keywords="bioinformatics machine-learning data science drug discovery QSAR",
    entry_points = {'console_scripts':[
        'keyword-query = keyword_query.cli:main'
        ]},
    install_requires = [
        'pandas',
        'openpyxl'
    ]
)