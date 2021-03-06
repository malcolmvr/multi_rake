from pathlib import Path

from setuptools import find_packages, setup

requirements = Path(__file__).parent / 'requirements/core.txt'

with requirements.open(mode='rt', encoding='utf-8') as fp:
    install_requires = [line.strip() for line in fp]

readme = Path(__file__).parent / 'README.rst'

with readme.open(mode='rt', encoding='utf-8') as fp:
    readme_text = fp.read()

setup(
    name='nlp_rake',
    version='0.0.2',
    description='Multilingual Rapid Automatic Keyword Extraction (RAKE) for Python',  # noqa
    long_description=readme_text,
    keywords=['nlp', 'keywords', 'rake', 'keywords extraction'],
    license='MIT',
    author='Vitaliy Grabovets',
    author_email='vgithub@tryninja.io',
    url='https://github.com/malcolmvr/nlp_rake',
    packages=find_packages(include=['nlp_rake']),
    python_requires='>=3.5.0',
    install_requires=install_requires,
    include_package_data=True,
)
