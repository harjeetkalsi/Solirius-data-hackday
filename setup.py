from setuptools import setup, find_packages

setup(
    name='data-hackday',
    version='0.0.1',

    packages=find_packages(),
    description='Hackday analysis environment',
    url='https://github.com/pelucid/mripython',
    install_requires=[
        'ipywidgets',
        'ipython',
        'matplotlib~=2.2.3',
        'notebook~=5.7.0',
        'jupyterlab~=2.1.2',
        'numpy',
        'pandas',
        'seaborn~=0.9.0',
        'jupyter_contrib_nbextensions~=0.5.1',
        'matplotlib-venn',
    ]
)