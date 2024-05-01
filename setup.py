from setuptools import setup, find_packages

E = '-e .'

def get_requirements(path):
    requirements = []
    with open(path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.strip() for req in requirements]  # Remove leading/trailing whitespace
        requirements = [req for req in requirements if req != '\n']  # Remove empty lines

        if E in requirements:
            requirements.remove(E)

    return requirements

setup(
    name='ML-project',
    version='0.0.1',
    author='JJ',
    author_email='georgejoshi10@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('/Users/anshujoshi/PycharmProjects/ML-Project/Requirements.txt')
)
