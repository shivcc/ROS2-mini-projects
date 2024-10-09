#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"
 
class Robot_receiver_cpp : public rclcpp::Node 
{
public:
    Robot_receiver_cpp() : Node("robot_receiver_cpp") 
    {
        subscriber_ = this->create_subscription<example_interfaces::msg::String>("robot_news", 10, 
            std::bind(&Robot_receiver_cpp::callback_robot_news, this, std::placeholders::_1));
        RCLCPP_INFO(this->get_logger(), "receiver have started receiving");
    }
 
private:
    void callback_robot_news(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());

    }
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;

};
 
int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<Robot_receiver_cpp>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}