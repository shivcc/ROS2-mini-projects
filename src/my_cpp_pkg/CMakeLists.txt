cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

add_executable(cpp_node src/my_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(cpp_publisher src/robot_news_station.cpp)
ament_target_dependencies(cpp_publisher rclcpp example_interfaces)

add_executable(cpp_subscriber src/robot_receiver.cpp)
ament_target_dependencies(cpp_subscriber rclcpp example_interfaces)

add_executable(add_two_int_server_node src/add_two_int_server.cpp)
ament_target_dependencies(add_two_int_server_node rclcpp example_interfaces)

add_executable(add_two_int_client_no_oop src/add_two_int_client_no_oop.cpp)
ament_target_dependencies(add_two_int_client_no_oop rclcpp example_interfaces)

add_executable(add_two_int_client src/add_two_int_client.cpp)
ament_target_dependencies(add_two_int_client rclcpp example_interfaces)

install(TARGETS 
  cpp_node
  cpp_publisher
  cpp_subscriber
  add_two_int_server_node
  add_two_int_client_no_oop
  add_two_int_client
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
