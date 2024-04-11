from setuptools import setup, find_packages
import subprocess
import os

wrapper_version = (
    subprocess.check_output(['git', 'describe', '--tags'], stdout=subprocess.PIPE)
    .stdout.decode('utf-8')
    .strip()
)

if "-" in wrapper_version:
    # when not on tag, igt describe outputs: "1.3.3-22-gdf81228"
    # pip has got strict version numbers
    # so change it to: "1.3.3+.git.gdf81228"
    # see: https://www.python.org/pep-0440/#local-version-segments
    v,i,s = wrapper_version.split("-")
    wrapper_version =  v + "+" + i + ".git." + s

assert "-" not in wrapper_version
assert "." in wrapper_version

assert os.path.exists("weather_api_wrapper/version.py")
with open("weather_api_wrapper/version.py", "w") as fh:
    fh.write( "%s\n" % wrapper_version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='weather_api_wrapper',
    version=wrapper_version,
    packages=find_packages(),
    author='Austin Ayah',
    author_email='ayahaustine@gmail.com',
    description='A Python wrapper for the OpenWeatherMap API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={'weather_api_wrapper': ['VERSION']},
    url='https://github.com/pyaustine/weather-api-wrapper.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'weather-cli=weather_api_wrapper.cli:main',
        ],
    },
    install_requires=[
        'requests',
    ],
)

