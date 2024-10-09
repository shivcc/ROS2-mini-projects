#include "rclcpp/rclcpp.hpp"

class Mynode: public rclcpp::Node
{
public:
    Mynode(): Node("cpp_test"), counter_(0)
    {
        RCLCPP_INFO(this->get_logger(), "Hello cpp node");

        timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&Mynode::timer_callback, this));
    }

private:

    void timer_callback()
    {
        counter_++;
        RCLCPP_INFO(this->get_logger(), "Hello %d", counter_);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    int counter_;
};

int main(int argc, char **argv){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<Mynode>();
    
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}