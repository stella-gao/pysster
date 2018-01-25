from setuptools import setup

setup(
    name = 'pysster',
    version = '1.1.0',
    description = 'a Sequence/STructure classifiER for biological sequences',
    url = 'https://github.com/budach/pysster',
    author = 'Stefan Budach',
    author_email = 'budach@molgen.mpg.de',
    license = 'MIT',
    install_requires =  [
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'keras>=2.1.3',
        'tensorflow>=1.4.1',
        'h5py',
        'logging_exceptions',
        'Pillow',
        'forgi'
    ],
    packages = ['pysster'],
    python_requires = '>=3.5',
    include_package_data = True,
    zip_safe = False
)
