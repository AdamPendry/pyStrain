from distutils.core import setup
import glob

script_files = ['bin/simvideo']+glob.glob('bin/*.py')

setup(
    name='SimVideo',
    version='2',
    author='Wolfgang Kastaun',
    author_email='physik@fangwolg.de',
    packages=['simvideo', 'simvideo.video'],
    scripts=script_files,
    license='LICENSE.txt',
    description='Infrastructure for making movies from Cactus data.',
    long_description=open('README.txt').read(),
    install_requires=[
        "PostCactus", "h5py",
        "numpy", "scipy", "matplotlib"
    ],
    package_data={}
)

