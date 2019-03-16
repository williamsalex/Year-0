/*
PROGRAM additionCalculator
Ask user for the first numbers
Ask them for the second numbers
Add the numbers
Output the numbers using a set precision and fixed notation
 END
 */
 #include <iostream>
 #include <iomanip>
 #include <cmath>
 #include <string>

double pi=3.14159265;
double r,c,a;
string ans;

int main() {
  // Introduce the user to the program and its purpose
  do{
    //Ask user for a radius value
    cout<<"What's the value of the radius?";
    cin>>r;
    // Calculate the circumference - 2*pi*r
    a=pi*pow(r,2);
    //Output the values using a set setprecision
    cout<<fixed<<setprecision(2);
    cout<<"The cirumference is "<<c<<"and the area is"<<a<<endl;
    //
    cout<<"Would you like to calculate again? Yes or No ";
    cin>>ans;
  } while (ans!="No"):
  return 0;
}
