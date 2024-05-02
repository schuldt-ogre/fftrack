from setuptools import setup, find_packages

setup(
    name='fftrack',
    version='0.1.7',
    description='FFTrack is a Python-based music recognition tool that allows users to identify songs from audio input.',
    author='schuldt-ogre <nschuldt@ogre.run>',
    packages=find_packages(),
    package_data={
        'fftrack': ['config.json', 'scripts/*.csv'],
    },
    install_requires=[
        "aniso8601>=9.0.1",
        "audioread>=3.0.1",
        "blinker>=1.7.0",
        "certifi>=2024.2.2",
        "cffi>=1.16.0",
        "charset-normalizer>=3.3.2",
        "click>=8.1.7",
        "contourpy>=1.2.1",
        "cycler>=0.12.1",
        "decorator>=5.1.1",
        "exceptiongroup>=1.2.1",
        "ffmpeg>=1.4",
        "flask>=3.0.3",
        "flask-cors>=4.0.0",
        "flask-restful>=0.3.10",
        "fonttools>=4.51.0",
        "greenlet>=3.0.3",
        "idna>=3.7",
        "imageio>=2.34.1",
        "imageio-ffmpeg>=0.4.9",
        "importlib-metadata>=7.1.0",
        "importlib-resources>=6.4.0",
        "iniconfig>=2.0.0",
        "itsdangerous>=2.2.0",
        "jinja2>=3.1.3",
        "joblib>=1.4.0",
        "kiwisolver>=1.4.5",
        "lazy-loader>=0.4",
        "librosa>=0.10.1",
        "llvmlite>=0.42.0",
        "markdown-it-py>=3.0.0",
        "markupsafe>=2.1.5",
        "matplotlib>=3.8.4",
        "mdurl>=0.1.2",
        "msgpack>=1.0.8",
        "numba>=0.59.1",
        "numpy>=1.26.4",
        "packaging>=24.0",
        "pandas>=2.2.2",
        "pillow>=10.3.0",
        "platformdirs>=4.2.0",
        "pluggy>=1.5.0",
        "pooch>=1.8.1",
        "proglog>=0.1.10",
        "pyaudio>=0.2.14",
        "pycparser>=2.22",
        "pydub>=0.25.1",
        "pygments>=2.17.2",
        "pyparsing>=3.1.2",
        "pytest>=8.1.1",
        "python-dateutil>=2.9.0.post0",
        "pytube>=15.0.0",
        "pytz>=2024.1",
        "requests>=2.31.0",
        "rich>=13.7.1",
        "scikit-learn>=1.4.2",
        "scipy>=1.13.0",
        "shellingham>=1.5.4",
        "six>=1.16.0",
        "soundfile>=0.12.1",
        "soxr>=0.3.7",
        "sqlalchemy>=2.0.29",
        "threadpoolctl>=3.4.0",
        "tomli>=2.0.1",
        "tqdm>=4.66.2",
        "typer>=0.12.3",
        "typing-extensions>=4.11.0",
        "tzdata>=2024.1",
        "urllib3>=2.2.1",
        "werkzeug>=3.0.2",
        "youtube-dl>=2021.12.17",
        "zipp>=3.18.1"
    ],
    extras_require={
        'dev': ['coverage>=7.4.1']
    },
    entry_points={
        'console_scripts': [
            'fftrack=fftrack.main:app',
            'populate-database=fftrack.scripts.populate_database:main',
        ],
    },
)