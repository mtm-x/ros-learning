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
    maintainer='lotus',
    maintainer_email='lotus@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            #<executable_name> = <package_name>.<file_name>:<function_name>
            "test_node_mtm = my_py_pkg.my_first_node:main",
            "number_publisher = my_py_pkg.number_publisher:main",
            "thisisexe = my_py_pkg.test_node:main",
            "thisissub = my_py_pkg.number_subscriber:main",
            "thisisstring = my_py_pkg.string_publisher:main",
            "thisisstringsub = my_py_pkg.string_subscriber:main",
            "reset_counter_client = my_py_pkg.reset_counter_client:main",
        ],
    },
)
