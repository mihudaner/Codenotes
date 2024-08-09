#include <iostream>
#include <vector>
#include <sstream>
using namespace std;
vector<int> nums;

void print_vector(const vector<int> &v)
{
     // 输出数组内容
    for (int n : v)
    {
        std::cout << n << " ";
    }
    std::cout << endl;
}

void quiksort(int l, int r)
{
    if(l>=r) return;
    int i = l-1, j = r+1, mid = (l + r)/2;
    int target = nums[mid];
    while (i < j)
    {
        do i++; while (nums[i] < target);
        do j--; while (nums[j] > target);
            
        if (i < j)
            swap(nums[i], nums[j]);
        //cout << i << " " <<  j << endl;
    }
    quiksort(l, j);
    quiksort(j+1, r);
    return;
}


void merge_sort(int l, int r)
{
    if(l>=r) return;
    int mid = (l+r)/2;
    merge_sort(l,mid);
    merge_sort(mid+1,r);
    vector<int> temp;
    int i=l,j=mid+1;
    while(i<=mid&&j<=r)
    {
        if(nums[i]<=nums[j]) temp.push_back(nums[i++]);
        else temp.push_back(nums[j++]);
    }
    
    while(i<=mid) temp.push_back(nums[i++]);
    while(j<=r) temp.push_back(nums[j++]);
    int idx = 0;
    while(idx<temp.size()) 
    {
        nums[l++]=temp[idx++];
    }
    return;
}

void    insert_sort()
{
    ////
}
void    heap_sort()
{
    
}


int main()
{
    string line;
    getline(std::cin, line); // 读取一行文本
    std::istringstream iss(line); // 将行文本放入字符串流中
    int num;
    while (iss >> num)
    {                        // 从字符串流中读取数字
        nums.push_back(num); // 将数字添加到向量中
    }

    print_vector(nums);

    //quiksort(0, nums.size() - 1);
    //merge_sort(0, nums.size() - 1);
    insert_sort();
    heap_sort();

    // 输出数组内容
    print_vector(nums);
    return 0;
}

// 1 2 3 42 41