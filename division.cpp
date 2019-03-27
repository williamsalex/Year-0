/* C++ Lab 1 Homework Part 1
 * A.Williams
 * Nobody
 * Do something
 * */
// Load libraries!
// Incorrect spelling of iostream and lack of namespace std
#include <iostream>
using namespace std;
int main (){
  // Z not declared
    double X,Y,Z;
    // All quotation marks broken on import
    cout<< "Enter X: ";
    cin >> X;
    cout<< "Enter Y: ";
    cin >> Y;
    Z = X/Y;
    cout<< "X/Y=" << Z;
    // Lack of '<<'
    cout<< "End of program." << endl;
    cout<< "Press any key to continue" << endl;
    cin.ignore();
    cin.get();
    // Lack of function close
}
