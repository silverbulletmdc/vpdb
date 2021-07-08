from setuptools import setup, find_packages
import glob

setup(
    name="vpdb",
    version="1.0.0",
    author="Dechao Meng",
    author_email="dechao.meng@vipl.ict.ac.cn",
    url="https://github.com/silverbulletmdc/vpdb",
    # keywords=("pytorch", "vehicle", "ReID"),
    description="Python debug configuration generator for vscode",
    scripts=glob.glob('scripts/*'),
    install_requires=["jstyleson"],
    # long_description="",
    packages=find_packages(exclude=('examples', 'examples.*')),
)
