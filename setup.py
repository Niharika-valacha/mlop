from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list:
    '''
    This function returns a list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        requirements = [req for req in requirements if req and not req.startswith('-e')]
    return requirements

# Metadata about your package
setup(
    name='mlproject',
    version='0.0.1',
    author='niharika',
    author_email='niharika10valacha@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
