#include <ros/ros.h>
#include <iostream>
#include <interbotix_xs_sdk/JointGroupCommand.h>
#include <interbotix_xs_sdk/JointSingleCommand.h>
#include <cmath>

float getRectJointAngle(float phase, float *angles);

int main(int argc, char **argv) {
    // Initialize the ROS system and become a node.
    ros::init(argc, argv, "playback_states");
    ros::NodeHandle nh;

    // Create some publisher objects.
    ros::Publisher pub_group = nh.advertise<interbotix_xs_sdk::JointGroupCommand>("wx200/commands/joint_group", 1);
    ros::Publisher pub_single = nh.advertise<interbotix_xs_sdk::JointSingleCommand>("wx200/commands/joint_single", 1);
    
    // Publish joint position commands at 1 Hz
    int loop_hz = 1;
    ros::Rate rate(loop_hz);

    // Give a second for the user to let go of the robot arm after it is torqued on and holding its position
    ros::Duration(1.0).sleep();
    interbotix_xs_sdk::JointSingleCommand initial_pos_msg;
    //initial_pos_msg.name = "elbow";
    //initial_pos_msg.cmd = 0;
    //pub_single.publish(initial_pos_msg);
    // Give a second for the joint that will be moving during the test to get to its zero position.
    ros::Duration(1.0).sleep();

    bool thing = false;
    while(ros::ok()) {
        // Create and fill in the message.
        interbotix_xs_sdk::JointGroupCommand msg_group;
        msg_group.name = "arm";

        for(int i = 0; i < 5; i++){
            msg_group.cmd.push_back(0);
        }
        
        //interbotix_xs_sdk::JointSingleCommand msg_single;
        //msg_single.name = "elbow";
        //msg_single.cmd = 0;

        // Publish the message.
        float angles[5];
        for(double i = 0;i<1;i = i + 0.05){
            pub_group.publish(msg_group);
            ROS_INFO_STREAM("" << msg_group);
            //ROS_INFO_STREAM("" << i);
            getRectJointAngle(i,angles);
            //msg_group.cmd = {angles[0], angles[1], angles[2], angles[3], angles[4]};
            for(int x = 0; i < 5; x++){
                msg_group.cmd[x] = angles[x];
            }
            rate.sleep();
        }
        
        /*
        if (thing) {
            msg_single.cmd = 0.5;
            thing = !thing;
        } else {
            msg_single.cmd = -0.5;
            thing = !thing;
        }
        pub_single.publish(msg_single);
        
        

        for(double i = 0;i<1;i = i + 0.05){
            getRectJointAngle(i,angles);
            msg_single.cmd = ;
            pub_single.publish(msg_single);
            ROS_INFO_STREAM("" << msg_single);
            rate.sleep();
        }*/

        // Send a message to rosout with the details.
        //ROS_INFO_STREAM("" << msg_single);

        // Wait until it's time for another iteration.
        //rate.sleep();
    }
}

float getRectJointAngle(float phase, float *angles){
    
    float waist;
    float shoulder;
    float elbow;
    float wristAngle;
    float wristRotate;

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
