/* C++ Lab 1 Homework Part 3
 * A.Williams
 * Nobody
 * Do something
 * */
// Load libraries!
// Incorrect spelling of iostream and lack of namespace std
#include <iostream>
#include <string>
using namespace std;
int main (){
  // Creating variables
    string cont = "Yes";
    string name;
    int O,C,N,S,H;
    // Loop as long as user wants to
    do {
      // Take inputs of acid name and chemical makeup
      cout<< "Enter name of the acid:        " << endl;
      cin >> name;
      cout<< "Enter # of atoms of Oxygen:    " << endl;
      cin >> O;
      cout<< "Enter # of atoms of Carbon:    " << endl;
      cin >> C;
      cout<< "Enter # of atoms of Nitrogen:  " << endl;
      cin >> N;
      cout<< "Enter # of atoms of Sulfur:    " << endl;
      cin >> S;
      cout<< "Enter # of atoms of Hydrogen:  " << endl;
      cin >> H;
      double weight,average;
      // Calculate weight and average using user values
      weight = O*15.9994+C*12.011+N*14.00674+S*32.066+H*1.00794;
      average = weight/(O+C+N+S+H);
      // Output results
      cout<< "The total molecular weight of " + name + " is: " + to_string(weight) << endl;
      cout<< "The average atomic weight of " + name + " is: " + to_string(average) << endl;
      // Ask if user wants to continue
      cout << "Enter 'No' to end, enter 'Yes' to continue!";
      // Repeat unless told otherwise
      cin >> cont;
      cin.ignore();
    } while(cont != "No");
    return 0;
}
