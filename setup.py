import setuptools

setuptools.setup(
    name="adt_cache",
    version="0.0.1",
    license='MIT',
    author="cheddars",
    author_email="nezahrish@gmail.com",
    description="abstract cache with in memory cache or redis (sentinel)",
    long_description=open('README.md').read(),
    url="https://github.com/cheddars/adt_cache",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)