from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='pyMono',
    version='0.0.1',
    license='GNU License',
    author= 'Evandro Alves Nakajima; Pedro Henrique Teodoro de Mendonça',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='teste@email.com',
    keywords='isotherm particle-swarm-optimization simulator',
    description=u'Descricao',
    packages=['pyMono'],
    install_requires=['pandas', 'numpy', 'matplotlib','scipy'],)

