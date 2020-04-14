from setuptools import setup, find_namespace_packages


setup(
    name='livetiming-plugin-example',
    description='Example Timing71 timing service plugin',
    author='James Muscat',
    author_email='jamesremuscat@gmail.com',
    url='https://github.com/timing71/livetiming-plugin-example',
    packages=find_namespace_packages('src', include=['livetiming.service.*'], exclude=["*/__tests__"]),
    package_dir={'': 'src'},
    long_description='''
    Example timing service plugin for Timing71.
    ''',
    install_requires=[
        'livetiming-core',
    ]
)
