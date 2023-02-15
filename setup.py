from setuptools import find_packages, setup

with open('requirements/base.txt') as f:
    required = f.read().splitlines()

packages = [
    "pytest<7,>=5",
    "pytest-sugar",
    "pytest-timeout",
]

setup(
    name="aiven",
    version="1.1.0",
    author="AmirBahador",
    author_email="amirbahador.develop@gmail.com",
    packages=find_packages(),
    python_requires=">=3.10",
    include_package_data=True,
    zip_safe=False,
    install_requires=packages
    + required + [
        "factory-boy==2.12",
        "faker==15.3.1",
        "pycountry==22.3.5",
        "python-dateutil==2.8.2",
        "pytz==2022.6",
        "wheel",
    ],
    setup_requires=["pytest-runner"],
    tests_require=packages,
)
