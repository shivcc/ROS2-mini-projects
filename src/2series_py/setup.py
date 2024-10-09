from setuptools import find_packages, setup

package_name = '2series_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shiv',
    maintainer_email='shivamchudasama08@gmail.com',
    description='This package is a demo project named Plus 2 project',
    license='Creative commons (cc)',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "series_gen = 2series_py.series_gen:main",
            "modify_series = 2series_py.modify_series:main",
            "final_series = 2series_py.final_series:main"
        ],
    },
)
