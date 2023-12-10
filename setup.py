from setuptools import setup

with open ('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
        name="Print name",
        version="1.0.0",
        description="It will simply print the name on to the console",
        long_description=long_description,
        author="Parimal",
        author_email="parimal@123",
        license='MIT',
        packages=['printname'],
        package_dir={ 'printname': './printname' },
        classifiers=[
            'Programming Language :: Python :: 3.8',
            "License :: OSI Approved :: MIT License",
            "Environment :: Console",
            "Operating System :: POSIX :: Linux"
        ],
        entry_points={
            'console_scripts': ['printname=printname.name.main']
        },
        data_files=[
            ('share/applications/', ['printname.desktop'])
        ],
        keywords="Print the name onto the console",
        python_requires=">= 3.8"
    )
