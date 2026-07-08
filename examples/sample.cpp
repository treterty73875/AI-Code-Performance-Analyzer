#include<iostream>
using namespace std;

int add(int a, int b)
{
    return a + b;
}

void display()
{
    cout << "Welcome to C++ Analyzer" << endl;
}

int factorial(int n)
{
    int result = 1;

    for(int i = 1; i <= n; i++)
    {
        result = result * i;
    }

    return result;
}

int main()
{
    int number = 5;

    if(number > 0)
    {
        cout << "Positive Number" << endl;
    }

    while(number > 0)
    {
        cout << number << endl;
        number--;
    }

    for(int i = 0; i < 3; i++)
    {
        cout << i << endl;
    }

    display();

    int answer = add(10,20);

    cout << "Sum = " << answer << endl;

    cout << "Factorial = " << factorial(5) << endl;

    return 0;
}