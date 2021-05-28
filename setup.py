from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='discord-py-message-components',
    author='Hostagen',
    url='https://github.com/Shturman-PS/discord-py-message-components',
    python_requires='>=3.6.0',
    license='GPL-2.0',
    install_requires=requirements
)
