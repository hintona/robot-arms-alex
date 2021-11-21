#include <iostream>
#include <cmath>
using namespace std;
double getXAvgJointAngle(float phase, double *angles);

int main (){
    double joints[6];
    getXAvgJointAngle(0.5, joints);
    cout << joints[0];
    return 0;
}

double getXAvgJointAngle(float phase, double *angles){
    double waist;
    double shoulder;
    double elbow;
    double wristAngle;
    double wristRotate;

    waist = 0.298193935 + (-2.20933452)*phase + (181.321972)*pow(phase,2.0) + (-1299.16696)*pow(phase,3.0) + (3775.15622)*pow(phase,4.0) + (-5400.33275)*pow(phase,5.0) + (3782.25650)*pow(phase,6.0) + (-1037.39641)*pow(phase,7.0) + (0.00887593910)*pow(phase,8.0);
    shoulder = -0.517480276 + (286.572091)*phase + (-2245.69769)*pow(phase,2.0) + (7858.18885)*pow(phase,3.0) + (-15078.1055)*pow(phase,4.0) + (16503.7568)*pow(phase,5.0) + (-9705.11861)*pow(phase,6.0) + (2381.04860)*pow(phase,7.0) + (-1.87447797)*pow(phase,8.0);
    elbow = -4.59602210 + (45.3207448)*phase + (-998.479177)*pow(phase,2.0) + (7910.86803)*pow(phase,3.0) + (-30077.6655)*pow(phase,4.0) + (63863.4691)*pow(phase,5.0) + (-79880.7449)*pow(phase,6.0) + (58345.6067)*pow(phase,7.0) + (-22909.8202)*pow(phase,8.0) + (3705.96620)*pow(phase,9.0) + (1.74349062)*pow(phase,10.0);
    wristAngle = -16.85555275 + (75.9138333)*phase + (-162.73205912)*pow(phase,2.0) + (162.6355504)*pow(phase,3.0) + (-59.19042303)*pow(phase,4.0) + (0.86415913)*pow(phase,5.0);
    wristRotate = 0;

    angles[0] = waist;
    angles[1] = shoulder;
    angles[2] = elbow;
    angles[3] = wristAngle;
    angles[4] = wristRotate;   
}