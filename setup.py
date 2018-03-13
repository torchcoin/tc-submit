from setuptools import setup

setup(
    name='tcsubmit',
    version='0.1',
    py_modules=['tcsubmit'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        tcsubmit=tcsubmit:cli
    ''',
)
