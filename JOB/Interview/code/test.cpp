
#include <atomic>
#include "mingw.thread.h"
#include <iostream>
#include <sstream>
using namespace std;
// enum type
// {
//     Txt,
//     Picture,
//     Video,
// };

// class ISplitter
// {

// };
// class TxtSplitter: public ISplitter {

// };

// class PictureSplitter: public ISplitter {

// };

// class VideoSplitter: public ISplitter {

// };

// class Factory
// {
//     ISplitter* getsplit(type type)
//     {
//         switch(type)
//         {
//             case Txt:
//                 return new TxtSplitter();
//             case Picture:
//                 return new TxtSplitter();
//             case Video:
//                 return new TxtSplitter();
//             default:
//                 return nullptr;
//         }
//     }
// };
#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#include<set>
using namespace std;
vector<int> findNext(vector<int> A, int n)
{
	set<int> ss;
	vector<int> result;
	for (int i = n - 1; i >= 0; --i) {
		auto pos = ss.lower_bound(A[i]);
		if (pos != ss.end() && *pos == A[i])
			++pos;
 
		if (pos == ss.end()) {
			result.push_back(-1);
		}
		else {
			result.push_back(*pos);
		}
		ss.insert(A[i]);
	}
	reverse(result.begin(), result.end());
	return result;
}
 
void printVector(vector<int>mat, int n)
{
	for (int j = 0; j < n; j++)
	{
		cout << mat[j] << " ";
	}
	cout << endl;
}
 
int main()
{
	vector<int> v;
	int m;
	int temp;
	while (cin >> m)
	{
		v.clear();
		for (int j = 0; j < m; j++)
		{
			cin >> temp;
			v.push_back(temp);
		}
		printVector(findNext(v, m), m);
	}
	return 0;
}
