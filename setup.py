from setuptools import setup, find_packages


setup(
    name='kostka',

    version='0.0.1',

    description='A sample Python project',
    package_dir={"": "src"},
    packages=find_packages("src"),
    setup_requires=['pytest-runner'],                                              
    tests_require=['pytest'],  
)