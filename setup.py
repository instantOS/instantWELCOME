from setuptools import setup, find_packages

setup(
    name='instantWELCOME',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules = [ 'welcome' ],

    install_requires=['PyGObject'],

    package_data={
        "instantWELCOME": ["*.glade", "*.sh", "*.desktop"],
    },

    entry_points='''
        [console_scripts]
        welcome=instantWELCOME.welcome:main
    ''',

    # metadata to display on PyPI
    author='Paperbenni',
    description='Welcome app for instantOS',
    keywords='instantos welcome',
    url='https://github.com/instantos/instantWELCOME',
    project_urls={
        'Source Code': 'https://github.com/instantos/instantWELCOME',
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]
)
