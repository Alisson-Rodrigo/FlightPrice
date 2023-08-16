from setuptools import setup, find_packages

authors = [
    {'name': 'Jorge Luis', 'email': 'jorgeluuis504@gmail.com', 'github': 'https://github.com/JorgeLuis8'},
    {'name': 'Alisson Rodrigo','email': 'alissorodrigo098@gmail.com', 'github': 'https://github.com/Alisson-Rodrigo'},
]

setup(
    name='testevoo',
    version='0.0.1',
    packages=find_packages(),
    license='MIT',
    description='Pacote para obter o menor preço de passagens aéreas',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['selenium','Chorme'],
    authors=authors,
    keywords=['flight', 'price', 'web scraping'],
)
