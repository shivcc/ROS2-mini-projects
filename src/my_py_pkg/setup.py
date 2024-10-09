from setuptools import find_packages, setup

package_name = 'my_py_pkg'

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
            "py_demo_node = my_py_pkg.test_py:main",
            "NewsStationNode = my_py_pkg.robot_station:main",
            "Receiver_robot = my_py_pkg.robot_receiver:main",
            "add_two_int_node = my_py_pkg.add_two_int_server:main",
            "add_two_int_no_oop = my_py_pkg.add_two_int_client_no_oop:main",
            "add_two_int_client = my_py_pkg.add_two_int_client:main"
        ],
    },
)
