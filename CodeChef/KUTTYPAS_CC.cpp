#include <iostream>
using namespace std;
#include <string>

int main()
{
    int n = 0;
    cin >> n;
    string L[n];
    int counter[n] = {0};
    for(int i=0;i<n;i=i+1) {
        string s = "";
        cin >> s;
        L[i] = s;
    }
    for (int i=0; i<n;i++) {
        for (int j=0;j<n;j++) {
            if (j!=i) {
                if (L[j].rfind(L[i], 0) == 0) {
                    if (L[j] != L[i]) {
                        counter[i] = counter[i] + 1;   
                    }
                }
            }
        }
        cout << counter[i] <<endl;
    }
    return 0;
}