from setuptools import setup, find_packages

setup(
    name='vorpal',
    version='3.4.1',
    description='End-to-end testing framework',
    long_description='End-to-end testing framework',
    long_description_content_type='text/markdown',
    author='i3logix, LLC',
    author_email='cemerson@i3logix.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='test automation qa',
    project_urls={
        'Owner': 'http://i3logix.com',
    },
    packages=find_packages(),
    install_requires=[
        'selenium',
        'requests'
    ],
    python_requires='>=3.6',
    package_data={},
)