#include <iostream>
using namespace std;

// Function to add two numbers
int add(int a, int b)
{
    int sum = a + b;
    return sum;
}

int main()
{
    // Variable declarations
    int age = 22;
    float salary = 35000.50;
    double pi = 3.14159;
    char grade = 'A';
    bool isPass = true;
    long population = 1500000;
    short year = 25;

    // For loop
    for(int i = 0; i < 5; i++)
    {
        cout << i << endl;
    }

    // While loop
    int count = 0;
    while(count < 3)
    {
        count++;
    }

    // If statement
    if(age > 18)
    {
        cout << "Adult" << endl;
    }

    int result = add(age, count);

    return 0;
}