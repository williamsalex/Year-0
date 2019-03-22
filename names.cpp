/* C++ Lab 2 Homework Part 1
 * A.Williams
 * Nobody
 * Do something
 * */
// Load libraries!
#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
using namespace std;
string filename;
ifstream File;
int main() {
    int a,b;
    // Welcome messages, explicating purpose to the user.
    cout<<"Welcome User!\n";
    cout<<"This program shows you the most popular female and male baby names per input year!\n";
    cout<<"Please input the name of the file which you would like to use (Retrieving from Downloads folder):\n";
    // Get input, read file specified and assign it to a variable
    getline(cin,filename);
    ifstream File("C:\\Users\\Alex\\Downloads\\"+filename);
    while (File >> a >> b){
        cout<<a;
        cout<<b;
    }
    return 0;
}
