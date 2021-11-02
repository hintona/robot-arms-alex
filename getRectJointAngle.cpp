#include <iostream>
#include <cmath>
using namespace std;
double getRectJointAngle(float phase);

int main (){
    double joints = getRectJointAngle(0.5);
    cout << joints;
    return 0;
}

double getRectJointAngle(float phase){
    double angles[4];
    double waist;
    double shoulder;
    double elbow;
    double wristAngle;

    waist = 0.069 + (-7.59)*phase + (244)*pow(phase,2.0) + (-2870)*pow(phase,3.0) + 17938*pow(phase,4.0) + (-65380)*pow(phase,5.0) + 144527*pow(phase,6.0) + (-195854)*pow(phase,7.0) + 158811*pow(phase,8.0) + (-70688)*pow(phase,9.0) + 13279*pow(phase,10.0);
    shoulder = -1.79 + (13.2)*phase + 371*pow(phase,2.0) + (-1501)*pow(phase,3.0) + (-3361)*pow(phase,4.0) + (42248)*pow(phase,5.0) + (-140264)*pow(phase,6.0) + (242354)*pow(phase,7.0) + (-236407)*pow(phase,8.0) + 123406*pow(phase,9.0) + (-26834)*pow(phase,10.0);
    elbow = 1.55 + (-0.321*phase) + (-85.6)*pow(phase,2.0) + 706*pow(phase,3.0) + (-2361)*pow(phase,4.0) + 4076*pow(phase,5.0) + (-3855)*pow(phase,6.0) + 1917*pow(phase,7.0) + (-396)*pow(phase,8.0);
    wristAngle = 0.546 + 9.56*phase + (-159)*pow(phase,2.0) + (-781)*pow(phase,3.0) + (15470)*pow(phase,4.0) + (-80602)*pow(phase,5.0) + 217396*pow(phase,6.0) + (-341511)*pow(phase,7.0) + 315155*pow(phase,8.0) + (-158544)*pow(phase,9.0) + 33567*pow(phase,10.0);

    angles[0] = waist;
    angles[1] = shoulder;
    angles[2] = elbow;
    angles[3] = wristAngle;
    
    return angles[1];
}