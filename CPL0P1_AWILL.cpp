  /* C++ Lab #0 Part 1
  * A.Williams
  * Nobody
  * First Program
  * Something
  */
  #include <iostream>
  #include <ctime>
  int main(){
    std::cout << "Hell, World!" <<std::endl;
    char* dt = std::ctime(&now);
    std::cout << "The local date and time is:" << dt << std:endl;
    return 0;
  }
