#include <iostream>
#include <vector>
#include <sstream>
using namespace std;
vector<int> nums;
int n;
void print_vector(const vector<int> &v)
{
     // 输出数组内容
    for (int n : v)
    {
        std::cout << n << " ";
    }
    std::cout << endl;
}

// 1 冒泡排序：‌
// 时间复杂度：‌最好情况为O(n)，‌当数组完全逆序时。‌平均时间复杂度为O(n^2)。‌
// 稳定性：‌稳定。‌

// 2  快速排序：‌
// 时间复杂度：‌平均时间复杂度为O(nlogn)，‌最好情况为O(nlogn)，‌最坏情况为O(n^2)。‌
// 稳定性：‌不稳定

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

//3  直接插入排序：‌
// 时间复杂度：‌平均时间复杂度为O(n^2)，‌最好情况为O(n)。‌
// 稳定性：‌稳定。‌

void  insert_sort()
{
    vector<int> res(nums.size(),0);
    
    for(int i=0;i<nums.size();i++)
    {
        int idx = i;
        while(idx>0&&res[idx-1]>nums[i])
        {
            res[idx] = res[idx-1];
            idx--;
        }
        res[idx] = nums[i];
    }
    for(int i=0;i<nums.size();i++) nums[i] = res[i];
    return;
}

// 4 归并排序：‌
// 时间复杂度：‌平均时间复杂度为O(nlogn)。‌
// 稳定性：‌稳定。‌

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
// 5 堆排序：‌
// 时间复杂度：‌平均时间复杂度为O(nlogn)。‌
// 稳定性：‌不稳定。‌

void heapdown(int i, int max)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < max && nums[left] > nums[largest])
        largest = left;
    if (right < max && nums[right] > nums[largest])
        largest = right;

    if (largest != i)
    {
        swap(nums[i], nums[largest]);
        heapdown(largest, max);
    }
}

void build_heap()
{
    
    for(int i=n/2-1;i>=0;i--)
    {
        heapdown(i, n);
    }
    return;
}


void  heap_sort()
{
    build_heap();
    for(int i=n-1;i>=0;i--)
    {
        swap(nums[0],nums[i]);
        heapdown(0, i);
    }
}


int mains()
{
    string line;
    getline(std::cin, line); // 读取一行文本
    std::istringstream iss(line); // 将行文本放入字符串流中
    int num;
    vector<int> row_nums;
    while (iss >> num)
    {                        // 从字符串流中读取数字
        row_nums.push_back(num); // 将数字添加到向量中
    }
    n = row_nums.size();
    print_vector(row_nums);
    print_vector(nums);

    nums = row_nums;
    quiksort(0, nums.size() - 1);
    print_vector(nums);

    nums = row_nums;
    merge_sort(0, nums.size() - 1);
    print_vector(nums);

    nums = row_nums;
    insert_sort();
    print_vector(nums);

    nums = row_nums;
    heap_sort();
    print_vector(nums);
    return 0;
}

// 1 2 3 42 41















// void build_heap()
// {
    
//     for(int i=n/2-1;i>=0;i--)
//     {
//         if(nums[i]<nums[i*2+1]) swap(nums[i],nums[i*2+1]);
//         if(nums[i]<nums[i*2+2]) swap(nums[i],nums[i*2+2]);
//     }
//     return;
// }
        
// void heapdown(int max)
// {
//     if(max<=0) return;
//     int i=0;
//     while(i*2+2<max)
//     {
//         //cout << i << " "<< nums.size() <<endl;
//         if(nums[i*2+2]>nums[i]&&nums[i*2+2]>nums[i*2+1])
//         {
//             swap(nums[i*2+2],nums[i]);
//             i = i*2+2;
//         }
//         else if(nums[i*2+1]>nums[i]&&nums[i*2+1]>nums[i*2+2])
//         {
//             swap(nums[i*2+1],nums[i]);
//             i = i*2+1;
//         }
//         else return;
//     }
// }