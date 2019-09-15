from distutils.core import setup
import glob

script_files = ['bin/simrep']+glob.glob('bin/*.py')

setup(
    name='SimRep',
    version='2',
    author='Wolfgang Kastaun',
    author_email='physik@fangwolg.de',
    packages=['simrep', 'simrep.plugins'],
    scripts=script_files,
    license='LICENSE.txt',
    description='Automated postprocessing and report generation.',
    long_description=open('README.txt').read(),
    install_requires=[
        "PostCactus",
        "numpy", "scipy", "matplotlib", "tables","h5py"
    ],
    package_data={'simrep':['data/*']}
)

