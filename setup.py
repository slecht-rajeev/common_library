from setuptools import find_packages, setup

setup(
    name='infoane-django',
    packages=find_packages(),
    description='This is a Django helper library for dait common functionality accross services',
    license='MIT',
    version='0.0.8',
    url='https://github.com/wokengineers/wokengineers-django.git',
    author='infoane',
    install_requires=[ 
        "PyJWT==2.6.0"
    ],
    keywords=['pip','infoane','library',"django","loggers","middleware"]
    )
