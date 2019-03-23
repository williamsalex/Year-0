    /* C++ Lab #1 Part 1
    * A.Williams
    * Nobody
    * Lab One
	* Add two numbers together
    */
#include <iostream>
using namespace std;
#include <iomanip>
    int main() {
        // Set up some variables
        float n1;
        float n2;
        float s;
        cout<<"Please enter your first value";
        cin>>n1;
        // Ask for a second number
        cout<<"Please enter your second value";
        cin>>n2;
        //Add those numbers!
        s=n1+n2;
        // Output the sum!
        cout<<fixed<<setprecision(3);
        cout<<"The sum of the values is "<<s<<"."<<endl;
        return 0;
    }
