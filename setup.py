from setuptools import setup, find_packages

setup(
    name='cultist-bot',
    version='1.0.0',
    url='https://github.com/jacob-swenson/cultist-bot',
    description='Cultist chat bot',
    author='m3ddl3r',
    maintainer='m3ddl3r',
    maintainer_email='jswenson91@gmail.com',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'wit',
        'discord',
        'python-dotenv',
        'lor-deckcodes>=1.1.1',
        'slackclient>=2.0.0',
        'slackeventsapi>=2.1.0',
        'Flask>=1.1.1',
        'certifi',
        'fuzzywuzzy',
        'python-Levenshtein'
    ],
)
