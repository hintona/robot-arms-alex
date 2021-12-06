cmake_minimum_required(VERSION 3.0.2)
project(robotest)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find another catkin packages
find_package(catkin REQUIRED COMPONENTS
    interbotix_xsarm_control
    interbotix_xs_sdk
    interbotix_xs_msgs
    roscpp
    sensor_msgs
    std_msgs
)

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
catkin_package()

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(include
    ${catkin_INCLUDE_DIRS}
)

## Declare a C++ executable
## Specify libraries to link a library or executable target against
## Add cmake target dependencies of the executable
add_executable(record_joint_states record_joint_states.cpp)
add_executable(playback_joint_states playback_joint_states.cpp)
add_executable(drawAvgRect drawAvgRect.cpp)
add_executable(replayX replayX.cpp)
add_executable(drawAvgX drawAvgX.cpp)

target_link_libraries(record_joint_states ${catkin_LIBRARIES})
target_link_libraries(playback_joint_states ${catkin_LIBRARIES})
target_link_libraries(drawAvgRect ${catkin_LIBRARIES})
target_link_libraries(drawAvgX ${catkin_LIBRARIES})
target_link_libraries(replayX ${catkin_LIBRARIES})

