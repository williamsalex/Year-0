/* C++ Lab #1 Part 2
* A.Williams
* Nobody
* Lab One
* Calculate Area and Circumference
*/
// Get libraries!
#include <iostream>
using namespace std;
#include <iomanip>
#include <cmath>
// Initialize variables!
double pi=3.14159265;
double r,c,a;
string ans = "Yes";
int main() {
    bool yes;
    while (ans == "Yes"){
        // Get the radius!
        cout<<"What's the radius of your circle?";
        // Do some math!
        cin>>r;
        c = 2*pi*r;
        a = pi*(pow(r,2));
        // Output the results!
        cout<<"The circumference is:"<<c<<", and the area is:"<<a<<"!"<<endl;
        // Request direction for next step!
        cout<<"Calculate another?"<<endl;
        cout<<"Enter 'Yes' or 'No'!"<<endl;
        // Prepare to execute next step!
        cin>> ans;
    }
    return 0;
}
