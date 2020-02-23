from setuptools import setup

setup(
    name='xml_from_seq',
    version='0.1.0',
    description='Generate XML from Python data structure',
    author='Nic Wolff',
    author_email='nwolff@hearst.com',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/nicwolff/xml_from_seq',
    py_modules=['xml_from_seq'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
