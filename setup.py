from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="image_processing",
    version="0.0.1",
    author="Claudia",
    author_email="dcastrg@gmail.com",
    description="Transformando a imagem",
    long_description=page_description,
    long_description_content_type="Mesclando a cor de duas imagens diferentes e criando uma terceira imagem com a mescla",
    url="https://github.com/ClaudiaGon",
    packages=find_packages(),
    install_requires="requeriments.txt",
    python_requires='>=3.8',
)