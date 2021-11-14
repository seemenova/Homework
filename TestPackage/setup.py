from setuptools import setup

setup(
    name='currenttime',
    version='1.0',
    author='Semenova Irina',
    packages=['currenttime'],
    description='Description',
    package_data={'': ['*.txt']},
    install_requires=['datetime'],
    entry_points={'console_scripts': ['currenttime = CurrentTime.currtime:func']},
)