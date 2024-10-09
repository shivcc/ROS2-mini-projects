from launch import LaunchDescription

from launch_ros.actions import Node

  
  

def generate_launch_description():

    ld = LaunchDescription()


    turtlesim_node = Node(

        package="turtlesim",
        executable="turtlesim_node",
        name="my_turtle_field"

    )

    turtle_spawner_node = Node(

        package="catch_em_turts_py",
        executable="turtle_spwn_rm",
        name="my_turtle_spawner"

    )
    
    turtle_controller_node = Node(
        package="catch_em_turts_py",
        executable="turtle_control_node",
        name="my_turtle_controller"
    )

  

    ld.add_action(turtlesim_node)
    ld.add_action(turtle_spawner_node)
    ld.add_action(turtle_controller_node)

    return ld