from setuptools import setup, find_packages


setup(
    name='stanley-outlet-control',
    version='1.0',
    url='https://github.com/coddingtonbear/gnuradio-stanley-remote-controlled-ac-outlet',  # noqa
    description=(
        'Remotely control your remotely-controlled Stanley AC outlets using '
        'a hackrf.'
    ),
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'stanley_outlet_control = stanley_outlet_control.stanley_controller.main'  # noqa
        ],
    },
)