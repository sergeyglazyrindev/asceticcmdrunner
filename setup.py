import sys
from setuptools import setup

# dirty hack, always use wheel
sys.argv.append('bdist_wheel')


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='acmdrunner',
    version='0.1',
    description='Ascetic command runner. The most ease way'
    ' to power your python app with custom management commands',
    long_description=readme(),
    classifiers=[
        'Development Status :: 0.1 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Misc',
    ],
    url='https://github.com/sergeyglazyrindev/acr',
    author='Sergey Glazyrin',
    author_email='sergey.glazyrin.dev@gmail.com',
    license='MIT',
    packages=['acmdrunner', ],
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': ['nose', 'mock'],
    },
    test_suite='tests',
)
