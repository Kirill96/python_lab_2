from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='lab2',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__),'README.txt')).read(),
    entry_points={
        'console_scripts':
            ['lab2_task1_2 = task1_2.task1:main',
             'lab2_task3 = task3.to_json:main',
             'lab2_task4 = task4.vector:main',
             'lab2_task5 = task5.logger:main',
             'lab2_task6 = task6.defaultdict:main',
             'lab2_task7 = task7.metaclass:main',
             'lab2_task8 = task8.cached:main',
             'lab2_task9 = task9.xrange:main',
             'lab2_task10 = task10.filter:main']
    }
)