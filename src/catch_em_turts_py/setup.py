from setuptools import find_packages, setup

package_name = 'catch_em_turts_py'

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
    maintainer_email='shiv@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "turtle_control_node = catch_em_turts_py.turtle_controller:main",
            "turtle_spwn_rm = catch_em_turts_py.turtle_spwn_rm:main"
        ],
    },
)
