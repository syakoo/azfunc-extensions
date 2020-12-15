import setuptools


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    name="azfunc-extensions",
    version="0.1",
    author="syakoo",
    author_email="sakodata0318@gmail.com",
    description="Azure functions' extension tools for Python.",
    url="https://github.com/syakoo/azfunc-extensions",
    packages=["azfunc-extensions"],
    package_dir={"azfunc-extensions": "src"},
    install_requires=_requires_from_file('requirements.txt'),
    python_requires=">=3.8"
)