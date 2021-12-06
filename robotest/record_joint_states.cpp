#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <iostream>
#include <fstream>

std::ofstream file;

void jointMessageReceived(const sensor_msgs::JointState &msg) {
    // Write msg to console and position only to file
    // ROS_INFO_STREAM(msg);
    file << msg.position[0] << "," << msg.position[1] << "," << msg.position[2] << "," << msg.position[3] << "," << msg.position[4] << "," << msg.position[5] << "," << msg.position[6] << "," << msg.position[7] << "\n";
}

int main(int argc, char **argv) {
    // Initialize the ROS system and become a node.
    ros::init(argc, argv, "subscribe_to_pose");
    ros::NodeHandle nh;

    // Open csv for recording joint states and insert headers
    file.open("JointStates.csv");
    file << "waist,shoulder,elbow,wrist_angle,wrist_rotate,gripper,left_finger,right_finger\n";

    // Create a subscriber object.
    ros::Subscriber sub = nh.subscribe("wx200/joint_states", 1000, &jointMessageReceived);
    
    // Let ROS take over.
    ros::spin();

    // Close csv
    file.close();
}