#include <ros/ros.h>
#include <iostream>
#include <interbotix_xs_msgs/JointGroupCommand.h>
#include <interbotix_xs_msgs/JointSingleCommand.h>
// Sometimes the messages are under interbotix_xs_msgs
// and sometimes they are under interbotix_xs_sdk.
// Not really sure why...

void getRectAvgJointAngle(float phase, float *angles);

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
        getRectAvgJointAngle(time, angles);

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


void getRectAvgJointAngle(float phase, float *angles){
    double waist;
    double shoulder;
    double elbow;
    double wristAngle;
    double wristRotate;

    waist = 0.069 + (-7.59)*phase + (244)*pow(phase,2.0) + (-2870)*pow(phase,3.0) + 17938*pow(phase,4.0) + (-65380)*pow(phase,5.0) + 144527*pow(phase,6.0) + (-195854)*pow(phase,7.0) + 158811*pow(phase,8.0) + (-70688)*pow(phase,9.0) + 13279*pow(phase,10.0);
    shoulder = -1.79 + (13.2)*phase + 371*pow(phase,2.0) + (-1501)*pow(phase,3.0) + (-3361)*pow(phase,4.0) + (42248)*pow(phase,5.0) + (-140264)*pow(phase,6.0) + (242354)*pow(phase,7.0) + (-236407)*pow(phase,8.0) + 123406*pow(phase,9.0) + (-26834)*pow(phase,10.0);
    elbow = 1.55 + (-0.321*phase) + (-85.6)*pow(phase,2.0) + 706*pow(phase,3.0) + (-2361)*pow(phase,4.0) + 4076*pow(phase,5.0) + (-3855)*pow(phase,6.0) + 1917*pow(phase,7.0) + (-396)*pow(phase,8.0);
    wristAngle = 0.546 + 9.56*phase + (-159)*pow(phase,2.0) + (-781)*pow(phase,3.0) + (15470)*pow(phase,4.0) + (-80602)*pow(phase,5.0) + 217396*pow(phase,6.0) + (-341511)*pow(phase,7.0) + 315155*pow(phase,8.0) + (-158544)*pow(phase,9.0) + 33567*pow(phase,10.0);
    wristRotate = 0;

    angles[0] = waist;
    angles[1] = shoulder;
    angles[2] = elbow;
    angles[3] = wristAngle;
    angles[4] = wristRotate;   
}

