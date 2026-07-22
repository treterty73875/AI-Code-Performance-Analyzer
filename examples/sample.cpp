#include <iostream>
using namespace std;

// Function to find maximum
int maximum(int a, int b)
{
    if(a > b)
    {
        return a;
    }

    return b;
}

// Function to calculate factorial
int factorial(int n)
{
    int fact = 1;

    for(int i = 1; i <= n; i++)
    {
        fact = fact * i;
    }

    return fact;
}

// Function to print numbers
void printNumbers(int limit)
{
    int count = 0;

    while(count < limit)
    {
        cout << count << endl;
        count++;
    }

    return;
}

int main()
{
    int age = 22;
    float salary = 50000.50;
    double pi = 3.14159;
    char grade = 'A';
    bool pass = true;
    long population = 1000000;
    short year = 25;

    // Redeclared variables
    int age = 30;
    float salary = 60000;
    char grade = 'B';

    int result = maximum(age, 20);

    if(result > 20)
    {
        cout << "Result is greater than 20" << endl;
    }

    int value = factorial(5);

    printNumbers(3);

    return 0;
}