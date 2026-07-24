#include <iostream>
using namespace std;

int factorial(int n)
{
    if(n <= 1)
    {
        return 1;
    }

    return n * factorial(n - 1);
}

int add(int a, int b)
{
    int sum = a + b;
    return sum;
}

void display(int n)
{
    int i;

    for(i = 0; i < n; i++)
    {
        cout << i << " ";
    }

    while(n > 0)
    {
        n--;
    }
}

void test()
{
    int x = 10;
    int y = 20;
    int unused = 100;

    if(x < y)
    {
        x = add(x, y);
    }

    cout << x << endl;
}

int main()
{
    int number = 5;
    int result;
    int temp = 0;

    result = factorial(number);

    display(number);

    test();

    if(result > 100)
    {
        cout << "Large" << endl;
    }
    else
    {
        cout << "Small" << endl;
    }

    return 0;
}