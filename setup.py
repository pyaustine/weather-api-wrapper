from setuptools import setup, find_packages

setup(
    name='weather_api_wrapper',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Austin Ayah',
    author_email='ayahaustine@gmail.com',
    description='A Python wrapper for the OpenWeatherMap API',
    url='https://github.com/pyaustine/weather-api-wrapper.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'weather-cli=weather_api_wrapper.cli:main',
        ],
    },
)

