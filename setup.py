import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weiboo",
    version="0.0.6",
    author="Yunzhi Gao",
    author_email="gaoyunzhi@gmail.com",
    description="Plain txt DB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaoyunzhi/weiboo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pyyaml',
        'cached_url',
    ],
    python_requires='>=3.0',
)