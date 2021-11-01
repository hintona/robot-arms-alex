#include <iostream>
using namespace std;

int main (){
    cout << getRectJointAngle(0.5);
    return 0;
}

float * getRectJointAngle(float phase){
    float angles[4];
    float waist;
    float shoulder;
    float elbow;
    float wristAngle;

    waist = 0.069 + (-7.59)*phase + (244)*phase^2 + (-2870)*phase^3 + 17938*phase^4 + (-65380)*phase^5 + 144527*phase^6 + (-195854)*phase^7 + 158811*phase^8 + (-70688)*phase^9 + 13279*phase^10;
    shoulder = -1.79 + (13.2)*phase + 371*phase^2 + (-1501)*phase^3 + (-3361)*phase^4 + (42248)*phase^5 + (-140264)*phase^6 + (242354)*phase^7 + (-236407)*phase^8 + 123406*phase^9 + (-26834)*phase^10;
    elbow = 1.55 + (-0.321*phase) + (-85.6)*phase^2 + 706*phase^3 + (-2361)*phase^4 + 4076*phase^5 + (-3855)*phase^6 + 1917*phase^7 + (-396)*phase^8;
    wristAngle = 0.546 + 9.56*phase + (-159)*phase^2 + (-781)*phase^3 + (15470)*phase^4 + (-80602)*phase^5 + 217396*phase^6 + (-341511)*phase^7 + 315155*phase^8 + (-158544)*phase^9 + 33567*phase^10;

    angles[0] = waist;
    angles[1] = shoulder;
    angles[2] = elbow;
    angles[3] = wristAngles;
    
    return angles;
}