#include <ros/ros.h>
#include <iostream>
#include <interbotix_xs_msgs/JointGroupCommand.h>
#include <interbotix_xs_msgs/JointSingleCommand.h>
// Sometimes the messages are under interbotix_xs_msgs
// and sometimes they are under interbotix_xs_sdk.
// Not really sure why...

void getXAvgJointAngle(float phase, float *angles);

int main(int argc, char **argv) {
    // Initialize the ROS system and become a node.
    ros::init(argc, argv, "playback_states");
    ros::NodeHandle nh;

    // Create some publisher objects.
    ros::Publisher pub_group = nh.advertise<interbotix_xs_msgs::JointGroupCommand>("wx200/commands/joint_group", 1);
    ros::Publisher pub_single = nh.advertise<interbotix_xs_msgs::JointSingleCommand>("wx200/commands/joint_single", 1);
    
    // Publish joint angle commands at 2 Hz
    int loop_hz = 2;
    ros::Rate rate(loop_hz);

    // Move arm to rest position
    ros::Duration(1.0).sleep();
    interbotix_xs_msgs::JointGroupCommand msg_group_init;
    msg_group_init.name = "arm";
    msg_group_init.cmd.push_back(0);        // waist
    msg_group_init.cmd.push_back(-1.88);    // shoulder
    msg_group_init.cmd.push_back(1.5);      // elbow
    msg_group_init.cmd.push_back(0.8);      // wrist_angle
    msg_group_init.cmd.push_back(0);        // wrist_rotate
    pub_group.publish(msg_group_init);
    
    ROS_INFO_STREAM("Returning arm to home: ");
    for (int i = 5; i > 0; i--) {
        ROS_INFO_STREAM("" << i << "...");
        ros::Duration(1.0).sleep();
    }

    bool thing = false;
    float time = 0.0;
    while(ros::ok() && time < 1.0) {
        // Create message and fill with zeros.
        interbotix_xs_msgs::JointGroupCommand msg_group;
        msg_group.name = "arm";
        float angles[5];
        
        for (int i = 0; i < 5; i++) {
            msg_group.cmd.push_back(0);
        }
        
        // Decide angles to send
        getXAvgJointAngle(time, angles);

        // Insert angles into group command
        for (int i = 0; i < 5; i++) {
            msg_group.cmd[i] = angles[i];
        }

        // Publish message.
        pub_group.publish(msg_group);
        
        // Send a message to rosout with the details.
        ROS_INFO_STREAM("" << msg_group);

        // Increment time
        time += 0.01;

        // Wait until it's time for another iteration.
        rate.sleep();
    }
}

void getXAvgJointAngle(float phase, float *angles){
    double waist;
    double shoulder;
    double elbow;
    double wristAngle;
    double wristRotate;

    waist = 0.298193935*phase + (-2.20933452)*pow(phase,2.0) + (181.321972)*pow(phase,3.0) + (-1299.16696)*pow(phase,4.0) + (3775.15622)*pow(phase,5.0) + (-5400.33275)*pow(phase,6.0) + (3782.25650)*pow(phase,7.0) + (-1037.39641)*pow(phase,8.0) + (0.00887593910);
    shoulder = -0.517480276*phase + (286.572091)*pow(phase,2.0) + (-2245.69769)*pow(phase,3.0) + (7858.18885)*pow(phase,4.0) + (-15078.1055)*pow(phase,5.0) + (16503.7568)*pow(phase,6.0) + (-9705.11861)*pow(phase,7.0) + (2381.04860)*pow(phase,8.0) + (-1.87447797);
    elbow = -4.59602210*phase + (45.3207448)*pow(phase,2.0) + (-998.479177)*pow(phase,3.0) + (7910.86803)*pow(phase,4.0) + (-30077.6655)*pow(phase,5.0) + (63863.4691)*pow(phase,6.0) + (-79880.7449)*pow(phase,7.0) + (58345.6067)*pow(phase,8.0) + (-22909.8202)*pow(phase,9.0) + (3705.96620)*pow(phase,10.0) + (1.74349062);
    wristAngle = (-16.85555275)*phase + (75.9138333)*pow(phase,2.0) + (-162.73205912)*pow(phase,3.0) + (162.6355504)*pow(phase,4.0) + (-59.19042303)*pow(phase,5.0) + (0.86415913);
    wristRotate = 0;

    angles[0] = waist;
    angles[1] = shoulder;
    angles[2] = elbow;
    angles[3] = wristAngle;
    angles[4] = wristRotate;   
}
