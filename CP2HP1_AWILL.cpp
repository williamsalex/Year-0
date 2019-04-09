/* C++ Lab #2 Homework Part 1
* A.Williams
* Nobody
* Lab Two Homework
* Find baby names
*/
// Get libraries!
#include <iostream>
using namespace std;
#include <iomanip>
#include <cmath>
#include <limits>
#include <fstream>
#include <string>
// Initialize variables!
string file,year,gender;
ifstream myfile;
//
int main(){
  cout << "Welcome user! This program outputs the most popular baby name of an inputted year and gender!" << endl;
  cout << "Please input file name!" << endl;
  cin >> file;
  myfile.open(file);
  if(myfile.is_open()) {
    cout << "Please enter a year!" << endl;
    cin >> year;
    cout << "Please enter a gender!" << endl;
    cin >> gender;
    while (getline(myfile, line))
    {
      cout << line << '\n';
    }
  } else {
    cout << "Invalid file!!! Ending!!!" << endl;
    break;
  }
  return 0;
}
