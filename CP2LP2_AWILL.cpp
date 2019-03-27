/* C++ Lab #2 Part 2
* A.Williams
* Nobody
* Lab Two
* Calculate trajectories
*/
// Get libraries!
#include <iostream>
using namespace std;
#include <iomanip>
#include <cmath>
#include <limits>
#include <fstream>
// Initialize variables!
double angle;
string output;
int timesteps;
double velocity;
string cont;
int main() {
    do {
        // Get input!
        cout<<"Please specify output file name!" << endl;
        cin >> output;
        cout<<"Please give initial angle!" << endl;
        cin >> angle;
        cout<<"Please give an initial velocity!" << endl;
        cin >> velocity;
        cout<<"Please give number of timesteps!" << endl;
        cin >> timesteps;
        // Do some math!
        double table = [timesteps][2]
        for (int a = 0; a<timesteps+1;a=a+1){
          table[a][1] = velocity*a-.5*9.8*a^2
        }
        output.open(output);
        output << table;
        output.close();
        cout<<"Your answer is: " << input1 << " " << operation << " " << input2 << " " << "=" << " " << setprecision(5) << ans  << endl;
        cout<<"Calculate another?"<<endl;
        cout<<"Enter 'Yes' or 'No'!"<<endl;
        // Prepare to execute next step!
        cin >> cont;
    } while (cont == "Yes");
    return 0;
}
