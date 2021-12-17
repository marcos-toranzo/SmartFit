from setuptools import setup

setup(
    name="requirements",
    description="Install requirements",
    license="GPL-3.0",
    author="Marcos Toranzo Alfonso",
    install_requires=["pytest", "fastapi[all]", "uvicorn[standard]"],
)
