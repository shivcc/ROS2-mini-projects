#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"
 
class Robot_station_node : public rclcpp::Node 
{
public:
    Robot_station_node() : Node("Robot_news_station") 
    {
        RCLCPP_INFO(this->get_logger(), "Node has started");
        publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);
        timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&Robot_station_node::timer_callback, this));
    }
 
private:
    void timer_callback()
    {
      auto message = example_interfaces::msg::String();
      message.data = "Hello, world! " + std::to_string(count_++);
      RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
      publisher_->publish(message);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
    int count_;
};
 
int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<Robot_station_node>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}