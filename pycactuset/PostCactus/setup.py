from distutils.core import setup
import glob

script_files = ['bin/simsync', 'bin/pardiff', 'bin/parprint']+glob.glob('bin/*.py')

setup(
    name='PostCactus',
    version='2',
    author='Wolfgang Kastaun',
    author_email='physik@fangwolg.de',
    packages=['postcactus'],
    scripts=script_files,
    license='LICENSE.txt',
    description='Read and postprocess CACTUS data',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy", "scipy",
        "tables", "h5py",
        "matplotlib",
    ],
)
