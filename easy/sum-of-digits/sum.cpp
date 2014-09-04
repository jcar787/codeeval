#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char* argv[]) 
{
    ifstream file;
    string line;
    file.open(argv[1]);
    while (!file.eof()) 
    {
        getline(file, line);
        if (line.length() > 0)
        {
            int result = 0;
            for(int i=0; i<line.length();i++)
            {
                result += line[i]-48;
            }

            cout << dec << result << endl;
        }
    }
    return 0;
}
