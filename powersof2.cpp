/* C++ Lab 1 Homework Part 1
 * A.Williams
 * Nobody
 * Do something
 * */
// Load libraries!
#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;
double b;
int main() {
    // Welcome message and introduction to program
    cout << "Welcome User!\n";
    cout << "This program shows powers of 2!\n";
    cout << "Press any key to contine" << endl;
    cin.ignore();
    cin.get();
    cout << "Power  Value\n";
    for (double a = 0; a < 9; a = a + 1) {
        b = pow(2, a);
        cout << fixed << showpoint;
        cout << setprecision(2);
        cout << to_string(a) + "   " + to_string(b) << endl;
    }
    return 0;
}
