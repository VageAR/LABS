#include <iostream>
#include <stack>
#include <list>
using namespace std;

int met[100000];  
int times[100000]; 
list<int> mass[100000];
int n; 
long long ans = 0; 
int col = 0; 
stack<int> stk; 

void DFS(int v)
{ 
met[v] = 1; 
     ans+= times[v];
     col++; 

      
      list<int>::iterator iter = mass[v].begin();
      while (iter != mass[v].end())
      {
           if (met[*iter] != 1)
                 DFS(*iter); 
           iter++; 
        }
        stk.push(v); 
}
void Out() 
{
         
          stack<int> stk1;
          while (stk.size() > 0)
          {
                 stk1.push(stk.top());
                 stk.pop();
           }
           while (stk1.size() > 0)
            {
                    cout << stk1.top() + 1 << " ";
                    stk1.pop();
             }
}
int main()
{
      freopen("input.txt", "r", stdin);
      
       cin >> n;
       for (int i = 0; i < n; ++i)
             cin >> times[i];
       for (int i = 0; i < n; ++i)
       {
             int k;
             cin >> k;
             for (int j = 0; j < k; ++j)
             {
                  int g;
                  cin >> g;
                  g--;
                  mass[i].push_back(g);
              }
        } 

DFS(0);

cout << ans << " " << col << endl; 
Out();
 return 0;
}  
