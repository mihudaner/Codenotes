## 三数之和

```c
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
       
        int n = nums.size();
        vector<vector<int>> res;
        for(int first = 0;first<n;first++)
        {
            if(first!=0&&nums[first]==nums[first-1]) continue;
            int third = n-1;
            for(int second=first+1;second<third;second++)
            {
            
                if(second!=first+1&&nums[second]==nums[second-1]) continue;
                while(third>second&&nums[first]+nums[second]+nums[third]>0) third--;
                if(second==third) continue;
                if(nums[first]+nums[second]+nums[third]==0)
                {
                    res.push_back({nums[first],nums[second],nums[third]});
                    //cout << first << second << third <<endl;
                } 
            }
        }
        return res;
    }
};
```

就是3重循环，然后排序优化第三个循环

## 二维数组中的查找

```c
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        int idx =0;
        if(matrix[0][0]>target) return false;
        if(matrix[0][0]==target) return true;

        
        for(int i=0;i<m;i++)
        {
            if(matrix[i][0]>target) continue;
            if(matrix[i][n-1]>=target)
            {
                for(int j=0;j<n;j++)
                {
                    if(matrix[i][j]==target) return true;
                }
            } 
        }
        return false;
    }
};
```

直接判断最左右是否符合





```c
class Solution {
public:
    bool searchArray(vector<vector<int>> array, int target) {
        
        int n = array.size();
        if(n==0) return false;
        int m = array[0].size();
        int r = m-1;;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<=r;j++)
            {
                if(array[i][j]>target)
                {
                    r = j-1;
                    continue;
                }
                //cout << i << j<<endl;
                if(array[i][j]==target) return true;
            }
            
        }
        return false;
    }
};
```

第二遍 压缩每行右边界

**阿秀ans:**

![image-20240706231619375](/home/wangkai/codenotes_ubuntu/Leecode/img/image-20240706231619375.png)

```
    bool Find(int target, vecianzhtor<vector<int> > array) {
        if(array.empty() || array[0].empty()) return false;
        int row = array[0].size(), col = array.size();
 
        int w=row-1,h=0;
        while(w>=0&&h<col){           
            if(array[h][w]>target) w--;
            else if(array[h][w]<target) h++;
            else 
                return true;
        }
        return false;        
    }

```

从右上往左下搜





```c


class Solution {
public:
    bool hasFound(vector<int>& array, int target) {

        int l = 0, r = array.size() - 1,mid;
        while(l<r)
        {
            if(array[r]==target) return true;
            mid = (r+l)>>1;
            if(array[mid]>=target) r = mid;
            else l = mid+1;
        }
        //cout << l << r <<endl;
        if(array[r]==target) return true;
        return false;
    }

	bool hasFound(vector<int>& array, int target) {
	int start = 0, end = array.size() - 1;
	while (start + 1 < end) {
		int mid = start + (end - start) /2;
		//cout << array[mid] << " "<<start<<" "<<mid<<" "<<end<<" ";
		if (array[mid] == target) return true;
		else if (array[mid] > target) end = mid;
		else
			start = mid;
	}
	if (array[start] == target || array[end] == target) return true;
	return false;

    }

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;
        for (int i = 0; i < matrix.size(); ++i) {
            cout << i <<endl;
            if (hasFound(matrix[i], target)) return true;
        }
        return false;
    }
};

```

每一行的二分

## 替换空格

```c
class Solution {
public:
    string replaceSpaces(string &str) {
        string res = "";
        for(auto c:str)
        {
            if(c==' ') res+="%20";
            else res+=c;
        }
        return res;
    }
};
```

新建一个再push



**阿秀ans:**

```c
void replaceSpace(char *str,int length) {//int length是指当前的长度
    int spaceCount = 0;
    int totalLen = length;
    for(int i = 0; i < length; ++i){
        if(str[i] == ' ') spaceCount++;
    }

    totalLen += spaceCount*2;
    for(int i = length-1; i>=0 &&totalLen != i; --i){//当 i = totalLen的时候说明前面已经
        //都没有空格了，可以节约一部分时间，而不是一直赋值下去
        if(str[i] != ' ') str[--totalLen] = str[i];
        else{
            str[--totalLen] = '0';
            str[--totalLen] = '2';
            str[--totalLen] = '%';                
        }

    }
}
```

从后往前修改

##  从尾到头打印链表

``` c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> printListReversingly(ListNode* head) {
        vector<int> res;
        while(head!=nullptr)
        {
            res.push_back(head->val);
            head = head->next;
            
        }   
        reverse(res.begin(),res.end());
        return res;
    }
};
```

**阿秀ans:**

## *重建二叉树

**阿秀ans:**

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size()==0||inorder.size()==0) return NULL;
        TreeNode* nd = new TreeNode(preorder[0]);
        int mid = distance(inorder.begin(),find(inorder.begin(),inorder.end(),preorder[0]));
        //cout << mid <<endl;
        vector<int> left_in(inorder.begin(),inorder.begin()+mid);
        vector<int> right_in(inorder.begin()+mid+1,inorder.end());
        
        vector<int> left_pre(preorder.begin()+1,preorder.begin()+mid+1);
        vector<int> right_pre(preorder.begin()+mid+1,preorder.end());
        nd->left = buildTree(left_pre,left_in);
        nd->right = buildTree(right_pre,right_in);
        return nd;
        
    }
};
```

## 用两个栈实现队列

```c
class MyQueue {
    stack<int> st;
    stack<int> temp;
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        st.push(x);
        return;
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        while(!st.empty())
        {
            temp.push(st.top());
            st.pop();
        }
        int res = temp.top();
        temp.pop();
        while(!temp.empty())
        {
            st.push(temp.top());
            temp.pop();
        }
        return res;
    }
    
    /** Get the front element. */
    int peek() {
        while(!st.empty())
        {
            temp.push(st.top());
            st.pop();
        }
        int res = temp.top();
        while(!temp.empty())
        {
            st.push(temp.top());
            temp.pop();
        }
        return res;
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return st.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * bool param_4 = obj.empty();
 */
```

**阿秀ans:**

##  旋转数组的最小数字

```c
class Solution {
public:
    int findMin(vector<int>& nums) {
        int n  = nums.size();
        if(!n) return -1;
        int last = -1;
        int idx=-1;
        for(int i=0;i<n;i++)
        {
            int x = nums[i];
            if(x<last) idx = i;
            last = x;
        }

        if(idx==-1) return nums[0];
        return nums[idx];
    }
};
```

**阿秀ans:**

我们发现除了最后水平的一段（黑色水平那段）之外，其余部分满足二分性质：

```c

class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size() - 1;
        if (n < 0) return -1;
        while (n > 0 && nums[n] == nums[0]) n -- ;
        if (nums[n] >= nums[0]) return nums[0];
        int l = 0, r = n;
        while (l < r) {
            int mid = l + r >> 1;       // [l, mid], [mid + 1, r]
            if (nums[mid] < nums[0]) r = mid;
            else l = mid + 1;
        }
        return nums[r];
    }
};

作者：yxc
链接：https://www.acwing.com/solution/content/727/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

## 斐波那契数列

```c
class Solution {
public:
    int Fibonacci(int n) {
        int res=1,last = 1;
        if(n==0) return 0;
        if(n==1) return 1;
        n--;
        while(--n)
        {
            int t = res;
            res+=last;
            last = t;
        }
        return res;
    }
};
```

## 跳台阶

```c
#include <iostream>
#include <vector>
using namespace std;
int main()
{
    
    int n;
    cin >>n;
  
    vector<int> res(n+1,1);
    res[1] = 1;
    for(int i=2;i<=n;i++)
    {
        res[i] = res[i-1] + res[i-2];
    }
    cout << res[n];
    return  0;
}
```

**阿秀ans:**递归更耗时，更好的就是我那样的循环

```c
    int jumpFloor(int number) {
        if(number==1) return 1;
        if(number==2) return 2;
        return jumpFloor(number-1) + jumpFloor(number-2);
        
    }

```



## JZ71 跳台阶扩展问题

每次可以跳n个台阶

```c
#include <vector>
using namespace std;
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param number int整型 
     * @return int整型
     */
    int jumpFloorII(int number) {
        // write code here
       vector<int> res(number+1,1);
       int sum = 2;
       for(int i=2;i<=number;i++)
       {
            res[i] = sum;
            sum+=res[i];
       }
       return res[number];
    }
};
```



## 矩阵覆盖

```c
class Solution {
public:
    int rectCover(int number) {
        vector<int> fc(number+1,0);
        vector<int> fr(number+1,0);
        fc[1] =1;
        fc[2] =1;
        fr[2] =1;
        for(int i=3;i<=number;i++)
        {
            fc[i] = fr[i-1] + fc[i-1];
            fr[i] = fr[i-2] + fc[i-2];
        } 
        return fr[number] + fc[number];
    }
};
```

**阿秀ans:**





 自己想的如果n*m?

问了gpt特别复杂，还要状态压缩

```c
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// 计算覆盖方法数的主函数
int countWaysToCoverMxN(int m, int n) {
    int totalStates = 1 << m;  // 总状态数，2的m次方
    vector<vector<int>> dp(n + 1, vector<int>(totalStates, 0));
    
    // 初始状态，第一列全空时，有一种方法
    dp[0][0] = 1;
    
    // 遍历每一列
    for (int j = 0; j < n; ++j) {
        // 遍历当前列的所有状态
        for (int state = 0; state < totalStates; ++state) {
            if (dp[j][state] == 0) continue;  // 如果当前状态不可达，跳过
            
            // 遍历下一列的所有可能状态
            for (int nextState = 0; nextState < totalStates; ++nextState) {
                bool valid = true;
                for (int i = 0; i < m; ++i) {
                    // 检查是否存在冲突
                    if ((state & (1 << i)) && (nextState & (1 << i))) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    // 更新dp值
                    dp[j + 1][nextState] += dp[j][state];
                }
            }
        }
    }
    
    // 最终的结果是最后一列全空的状态数
    return dp[n][0];
}

int main() {
    int m, n;
    cout << "请输入矩形的行数和列数 (m n): ";
    cin >> m >> n;
    cout << "覆盖方法数: " << countWaysToCoverMxN(m, n) << endl;
    return 0;
}

```

类似题

[LCP 04. 覆盖](https://leetcode.cn/problems/broken-board-dominoes/)

也很难   不想看了    也是要状态压缩加dp 或者 没见过解法的二分图

[2132. 用邮票贴满网格图](https://leetcode.cn/problems/stamping-the-grid/)

贪心+差分：难在放的邮票m*n,容易在可以重叠所以贪心



## **二进制中1的个数**

```c
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param n int整型 
     * @return int整型
     */
    int NumberOf1(int n) {
        // write code here
        int res=0;
        for(int i=0;i<32;i++)
        {
            if(n%2) res++;
            n = n>>1;
        }
        return res;
    }
};
```

**阿秀ans:**

```c
int  NumberOf1(int n) {
	return bitset<32>(n).count();
	}
```

```c

 int NumberOf1(int n) {
        int count = 0;
        while(n!= 0){
            count++;
            n = n & (n - 1);
         }
        return count;
    }

//每一次 n & (n - 1);可以将最后一个1置为0
```

##  **数值的整数次方**

```c
class Solution {
public:
    double Power(double base, int exponent) {
        double res= base;
        bool flag = false;
        if(exponent==0) return 1;
        if(exponent<0)
        {
            exponent = -exponent;
            flag = true;
        } 
        while(--exponent) res*=base;
        if(flag) return 1/res;
        return res;
    }
};
```



**阿秀ans:**快速幂

```c
    double myPow(double x, int n) {
        if( n == 0) return 1;
        if( x == 0.0) return 0;
        long  exp = n;//
        if(n < 0) {
            exp = n* (-1.0);//，当n == INT_MIN时正数时大于INT_MAX的，所以要用一个大于 INT_MAX的类型来保存，同时在将他转正的时候， n*(-1)的结果依然是一个 int，此时的int是个隐藏类型，然后才将这个结果赋值给 exp，所以用来保存结果值的不应该是个int型，我们用double型的 -1 ,这样就可以将相乘的结果值保存为一个 double类型了，然后再进行赋值
        } 
        
        double res = 1.0;
        while(exp != 0){
            if( (exp &1) == 1 ){
                res *=x;
            }
            x *=x;
            exp >>= 1;
        }

        return n<0 ? 1/res: res;

    }

```



## 调整数组顺序使奇数位于偶数前面

```c
class Solution {
public:
    void reOrderArray(vector<int> &array) {
        int n = array.size();
        int l=0,r = n-1;
        while(l<r)
        {
            while(l<n&&array[l]%2==1) l++;
            while(r>=0&&array[r]%2==0) r--;
            if(l<r) swap(array[l++],array[r--]);
        }
        return;
    }
};
```

**阿秀ans:**

##  链表中倒数第k个节点

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* findKthToTail(ListNode* pListHead, int k) {
        int n =0;
        ListNode* Head = pListHead;
        while(Head!=NULL)
        {
            n++;
            Head=Head->next;
        }
        int cnt = n-k;
        if(cnt<0) return NULL;
        Head = pListHead;
        while(cnt-->0)
        {
             Head=Head->next;

        }
        return Head;
    }
};
```

**阿秀ans:**快慢指针

```
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
    ListNode * slowNode = pListHead;
        while(k != 0){//这里判断 k 一直走到 0 即可
            k--;
            if(pListHead != nullptr) pListHead = pListHead->next;//在其中判断是否出现k 大于链表总长度的情况，
            //比如 【1,2,3,4,5】 6这样的情况，如果出现这样的情况，返回即可
            else
                return nullptr;
        }
        
        while(pListHead != nullptr){//先走的不能为空
            slowNode = slowNode->next;
            pListHead = pListHead->next;
        }
        return slowNode;
    }


```



## 反转链表

```c
/**
 * struct ListNode {
 *	int val;
 *	struct ListNode *next;
 *	ListNode(int x) : val(x), next(nullptr) {}
 * };
 */
#include <cstddef>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param head ListNode类 
     * @return ListNode类
     */
    ListNode* ReverseList(ListNode* head) {
        // write code here

        auto* res = new ListNode(-1);
        if(head==nullptr ||head->next ==nullptr) return head;
        
        ListNode* quik = head->next;
        ListNode* slow = head;
        slow->next = nullptr;
        while(quik!=nullptr)
        {
            ListNode* temp = quik->next;
            quik->next = slow;
            slow = quik;
            quik=temp;
        } 
        return slow;

    }
};
```



**阿秀ans:**头插法，类似，三个指针来回倒

```c
struct ListNode {
	int val;
	struct ListNode* next;
	ListNode(int x) :
		val(x), next(NULL) {
	}
}; 

ListNode* ReverseList(ListNode* pHead) {

	struct ListNode* Head = NULL;
	struct ListNode* node = (ListNode*)malloc(sizeof(struct ListNode));

	while (pHead != nullptr) {
		node = pHead;
		pHead = pHead->next;

		node->next = Head;
		Head = node;
	}
	return Head;
}


```

## **合并两个排序的链表**

```c
/**
 * struct ListNode {
 *	int val;
 *	struct ListNode *next;
 *	ListNode(int x) : val(x), next(nullptr) {}
 * };
 */
#include <fstream>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param pHead1 ListNode类 
     * @param pHead2 ListNode类 
     * @return ListNode类
     */
    void insertn(ListNode* &pHead1, ListNode* &pHead2)
    {
        ListNode* temp = pHead1->next;
        pHead1->next = pHead2;
        pHead2->next = temp;
        return;
    }

    ListNode* Merge(ListNode* pHead1, ListNode* pHead2) {
        // write code here
        
        if(pHead1==nullptr) return pHead2;
        if(pHead2==nullptr) return pHead1;
        if(pHead2->val<pHead1->val)  swap(pHead1, pHead2);
        ListNode* res = pHead1;
        while(pHead1->next!=nullptr&&pHead2!=nullptr)
        {
            
            if(pHead1->next->val>pHead2->val)
            {
                //cout << pHead1->next->val <<  pHead2->val <<endl;
                ListNode* next = pHead2->next;
                insertn(pHead1,pHead2);
                pHead2 = next;
            }
            else
            {
                pHead1 = pHead1->next;
            }
            
        }
        if(pHead2!=nullptr)pHead1->next = pHead2;
        return res;
    }
};
```

憋的非递归的原地址插入的方法

**阿秀ans:**递归的是真的简洁

```c
 ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
	if (pHead1 == nullptr) return pHead2;
	if (pHead2 == nullptr) return pHead1;


  
	if (pHead1->val <= pHead2->val) {
		pHead1->next = Merge(pHead1->next, pHead2);
		return pHead1;
	}
	else {
		pHead2->next = Merge(pHead1, pHead2->next);
		return pHead2;
	}
    }

```

## **树的子结构**

```c
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
#include <cstddef>
class Solution {
public:
	bool MyHasSubtree(TreeNode* pRoot1, TreeNode* pRoot2)
	{
		if(pRoot2==nullptr) return true;
		if(pRoot1==nullptr) return false;
		if(pRoot1->val==pRoot2->val)
        {
            if(MyHasSubtree(pRoot1->left,pRoot2->left)&&MyHasSubtree(pRoot1->right,pRoot2->right)) return true;
        }
		
		return MyHasSubtree(pRoot1->left,pRoot2)|| MyHasSubtree(pRoot1->right,pRoot2);
	}
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2) {
		if(pRoot2==nullptr) return false;
		return MyHasSubtree(pRoot1,pRoot2);
    }
};

```

**阿秀ans:**一模一样

## 二叉树的镜像



## 顺时针打印矩阵

```c
class Solution {
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        typedef pair<int,int>  PII;
        int n = matrix.size();
        int m = matrix[0].size();
        if(n==0||m==0) return {};
        int i =0,j=0;
        vector<PII> dir = {
            {0,1},{1,0},{0,-1},{-1,0}
        };
        int cnt=m*n;
        vector<int> res;
        vector<vector<bool>> flag(n,vector<bool>(m));
        int idx=0;
        flag[0][0]=true;
        res.push_back(matrix[0][0]);
        while(--cnt)
        {
            //cout << matrix[i][j] << endl;
            while(i+dir[idx].first>=n||i+dir[idx].first<0||
            j+dir[idx].second>=m||j+dir[idx].second<0||
            flag[i+dir[idx].first][j+dir[idx].second]==true) 
                idx = (idx+1)%4;
            i+=dir[idx].first;
            j+=dir[idx].second;
            res.push_back(matrix[i][j]);
            flag[i][j]=true;
        }
        return res;
    }
};
```

第二遍还是写的好复杂

**阿秀ans:**

```c
vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector <int> res;
        if(matrix.empty()) return res;
        int rl = 0, rh = matrix.size()-1; //记录待打印的矩阵上下边缘
        int cl = 0, ch = matrix[0].size()-1; //记录待打印的矩阵左右边缘
        while(1){
            for(int i=cl; i<=ch; i++) res.push_back(matrix[rl][i]);//从左往右
            if(++rl > rh) break; //若超出边界，退出
            for(int i=rl; i<=rh; i++) res.push_back(matrix[i][ch]);//从上往下
            if(--ch < cl) break;
            for(int i=ch; i>=cl; i--) res.push_back(matrix[rh][i]);//从右往左
            if(--rh < rl) break;
            for(int i=rh; i>=rl; i--) res.push_back(matrix[i][cl]);//从下往上
            if(++cl > ch) break;
        }
        return res;
    }

```

## 包含min的栈

第一遍做的

```c
class MinStack {
public:
    vector<pair<int,int>> idx;
    stack<int> st;
    MinStack() {
        
    }
    
    void push(int val) {
        cout<< "push" << val <<endl;
        this->st.push(val);

        if(this->idx.empty()|| val<this->idx.back().first)  idx.push_back({val,this->st.size()});
        return;
    }
    
    void pop() {
        cout<< "pop" <<endl;
        this->st.pop();
        if(this->st.size()<this->idx.back().second) this->idx.pop_back();
    }
    
    int top() {
        cout<< "top" <<endl;
        return this->st.top();
    }
    
    int getMin() {
         cout<< "getMin" <<endl;
        return this->idx.back().first;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

记录变化的节点的Min，但是也没节省到空间，阿秀ans:更好理解

**阿秀ans:**

```c
class Solution {
public:
    void push(int value) {
        if(st.size()==0&&minSt.size()==0) {
            st.push(value);
            minSt.push(value);
        }else{
            st.push(value);
            if(value<=minSt.top()){
                minSt.push(value);
            }
            else{
                minSt.push(minSt.top());
            }
            
        }
        //st.push(value); #这里应该删除
    }
    void pop() {
        st.pop();
        minSt.pop();
    }
    int top() {
        return st.top();
    }
    int min() {
        return minSt.top();
    }
    stack<int> minSt;
    stack<int> st;
};

```

## **栈的压入、弹出序列**

没想到看了答案挺简单的

**阿秀ans:**

```c
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param pushV int整型vector 
     * @param popV int整型vector 
     * @return bool布尔型
     */
    bool IsPopOrder(vector<int>& pushV, vector<int>& popV) {
        // write code here
        stack<int> st;
        int n = pushV.size(), m =popV.size();
        if(n==0||m==0||n!=m) return false;
        int i=0,j=0;
        while(i<n)
        {
            st.push(pushV[i]);
            i++;
            while(j<m&&!st.empty()&&st.top()==popV[j])
            {
                st.pop();
                j++;
            }
        }
        if(j==m) return true;
        return false;
    }
};
```

## 从上往下打印二叉树

```c
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
#include <queue>
class Solution {
public:
    vector<int> PrintFromTopToBottom(TreeNode* root) {
		queue<TreeNode*> q;
		q.push(root);
		vector<int> res;
		while(!q.empty())
		{
			TreeNode* t= q.front();
			q.pop();
			if(t==nullptr) continue;
			res.push_back(t->val);
			q.push(t->left);
			q.push(t->right);
		}
		return res;
    }
};

```

**阿秀ans:**

##  **二叉搜索树的后序遍历序列**

```c
class Solution {
public:
    bool MyVerifySquenceOfBST(vector<int> sequence) {
        int mid=0,root;
        root = sequence.back();
        int n = sequence.size();
        if(n<=2) return true;
        while(mid<n&&sequence[mid]<root)mid++;
        //cout << n << mid<<endl;
        for(int i=mid;i<n;i++)
        {
            if(sequence[i]<root) return false;
        }
        if(!MyVerifySquenceOfBST(vector<int>(sequence.begin(),sequence.begin()+mid))) return false;
        if(!MyVerifySquenceOfBST(vector<int>(sequence.begin()+mid,sequence.end()-1))) return false;
        return true;
    }
    bool VerifySquenceOfBST(vector<int> sequence)
    {
        int n = sequence.size();
        if(n==0) return false;
        if(n<=2) return true;
        return MyVerifySquenceOfBST(sequence);
    }
};
```

**阿秀ans:**

## 复杂链表的复制

```c
/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
#include <unordered_map>
class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead) {
        unordered_map<int,RandomListNode* > mp;
        RandomListNode* res = new RandomListNode(-1);
        RandomListNode* p = res;
        while(pHead!=nullptr)
        {
            //cout <<p->label<<endl;
            if(!mp.count(pHead->label)) 
            {
                RandomListNode* ne = new RandomListNode(*pHead);
                mp[ne->label] = ne;
            }
            p->next = mp[pHead->label];
            if(p->random!=nullptr)
            {
                if(!mp.count(p->random->label))
                {
                    RandomListNode* rd= new RandomListNode(*p->random);
                    mp[p->random->label]=rd;
                }   
                p->random = mp[p->random->label];
            }
           
            pHead=pHead->next;
            p = p->next;
        }
        return res->next;
    }
};
```

**阿秀ans:**

```c
RandomListNode* Clone(RandomListNode* pHead)
{
	if (pHead == nullptr)
	{
		return nullptr;
	}

	std::unordered_map<RandomListNode*, RandomListNode*> hash_map;

	for (RandomListNode* p = pHead; p != nullptr; p = p->next)
	{
		hash_map[p] = new RandomListNode(p->label);
	}

	for (RandomListNode* p = pHead; p != nullptr; p = p->next)
	{
		hash_map[p]->next = hash_map[p->next];//这里要注意是 unmp[p->next] 千万注意，好好想想
		hash_map[p]->random = hash_map[p->random];//下同
	}

	return hash_map[pHead];
}


```

递归是差不多的

```c
class Solution {
public:

  //关键是保存住映射关系，可以说是哈希表和链表的组合吧
    unordered_map<RandomListNode*,RandomListNode*> unmp;
	RandomListNode* Clone(RandomListNode* pHead)
	{
        if(pHead == nullptr) return nullptr;
        RandomListNode* newHead = new RandomListNode(pHead->label);
        unmp[pHead] = newHead;//这里需要保存的是 pHead -》 newHead 的映射关系,必须在这里保存
        newHead->next = Clone(pHead->next);//到这一步，其实所有的点已经全部生成了
        newHead->random = nullptr;//其实默认已经是nullptr了，有没有这一步其实没什么关系
        if(pHead->random != nullptr)  newHead->random = unmp[pHead->random];//这一步，真的是灵魂所在了
        return newHead;
	}
};

```

递归很牛



## **字符串的排列**

```c
#include <iostream>
#include <unordered_map>
#include "vector"
using namespace std;

class Solution{
    unordered_map<int, bool> mp;
    unordered_map<string, bool> ed;
public:
    void nstring(string res,string s,int idx,vector<string>& resv)
    {
        
        if(res.size()==s.size())
        {
            if(!ed.count(res))
            {
                resv.push_back(res);
                ed[res] = true;
            }
            return;
        } 
        if(idx>=0) mp[idx]= true;
        for(int i=0;i<s.size();i++)
        {
            if(!mp.count(i))
            {
                res+=s[i];
                nstring(res,s,i,resv);
                res.pop_back();
            }
        }
        if(idx>=0) mp.erase(idx);
        return;
    }
    //撤回算法
    vector<string> Permutation(string str){
        vector<string> resv;
        string res;
        nstring(res,str,-1,resv);
        return resv;
    }
};
```

用哈希和回溯就不是很难，但要注意重复的字母和重复的结果

“aaa”

**阿秀ans:** next_permutation

```c
    vector<string> permutation(string s) {

    if(s.size()==0) return vector<string>();
        
	vector<string> result;
	sort(s.begin(), s.end());
	do {
		result.push_back(s);
	} while (next_permutation(s.begin(),s.end()));

	return  result;
    }

```

## **数组中出现次数超过一半的数字**

```c
#include <unordered_map>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param numbers int整型vector 
     * @return int整型
     */
    int MoreThanHalfNum_Solution(vector<int>& numbers) {
        // write code here
        unordered_map<int, int> cnt;
        int n = numbers.size();
        for(auto x:numbers)
        {
            cnt[x]++;
            if(cnt[x]>=(n+1)/2) return x;
        }
        return -1;
    }
};
```

**阿秀ans:** 

第一种就是哈希表

第二种：大概就是这最多的元素就cnt+1否则-1

```c
    int MoreThanHalfNum_Solution(vector<int> numbers) {
	//摩尔投票法，成立前提就是有出现超过一半的元素，所以最后我们需要判断找到的元素是否出现超过一半了
	int cnt = 0, num = 0;
	for (int i = 0; i < numbers.size(); ++i) {
		if (cnt == 0) {
			num = numbers[i];
			cnt = 1;
		}
		else {
			num == numbers[i] ? cnt++ : cnt--;
		}

	}
	cnt = count(numbers.begin(), numbers.end(), num);
	return cnt > numbers.size() / 2 ? num : 0;
    }

```



## 最小的k个数

nlgk

```c
#include <fstream>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param input int整型vector 
     * @param k int整型 
     * @return int整型vector
     */
    void Down(vector<int>& input,int root,int n)
    {
        int l  = root*2+1;
        while(l+1<n)
        {
            int idx;
            if(input[l]<input[l+1]) idx= l;
            else idx= l+1;
            if(input[root]>input[idx])
            {
                swap(input[root],input[idx]);
                Down(input, idx,n);
            }
            else  break;
        }
    }

    vector<int> GetLeastNumbers_Solution(vector<int>& input, int k) {
        int n = input.size();
        vector<int> res;
        for(int i=n/2-1;i>=0;i--)
        {
            Down(input,i,n);
        }
        for(int i=0;i<k;i++)
        {
            res.push_back(input[0]);
            swap(input[0],input[n-1-i]);
            Down(input,0,n-1-i);
        }
        return res;
    }
};
```

> 小根堆排序



**阿秀ans:**

```c
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
    if(k > input.size()) return vector<int>();
    priority_queue<int, vector<int>, greater<int>> pq;
	for (auto a : input)
		pq.push(a);
	vector<int> result;
	while (k--) {
		result.push_back(pq.top());
		pq.pop();
	}
	return result;
    }

```

##  ** **堆排序(升序) 大根堆代码**

```cpp
/* 
 * (最大)堆的向下调整算法
 *
 * 注：数组实现的堆中，第N个节点的左孩子的索引值是(2N+1)，右孩子的索引是(2N+2)。
 *     其中，N为数组下标索引值，如数组中第1个数对应的N为0。
 *
 * 参数说明：
 *     a -- 待排序的数组
 *     start -- 被下调节点的起始位置(一般为0，表示从第1个开始)
 *     end   -- 截至范围(一般为数组中最后一个元素的索引)
 */
void maxheap_down(int a[], int start, int end)
{
    int c = start;            // 当前(current)节点的位置
    int l = 2*c + 1;        // 左(left)孩子的位置
    int tmp = a[c];            // 当前(current)节点的大小
    for (; l <= end; c=l,l=2*l+1)
    {
        // "l"是左孩子，"l+1"是右孩子
        if ( l < end && a[l] < a[l+1])
            l++;        // 左右两孩子中选择较大者，即m_heap[l+1]
        if (tmp >= a[l])
            break;        // 调整结束
        else            // 交换值
        {
            a[c] = a[l];
            a[l]= tmp;
        }
    }
}

/*
 * 堆排序(从小到大)
 *
 * 参数说明：
 *     a -- 待排序的数组
 *     n -- 数组的长度
 */
void heap_sort_asc(int a[], int n)
{
    int i;

    // 从(n/2-1) --> 0逐次遍历。遍历之后，得到的数组实际上是一个(最大)二叉堆。
    for (i = n / 2 - 1; i >= 0; i--)
        maxheap_down(a, i, n-1);

    // 从最后一个元素开始对序列进行调整，不断的缩小调整的范围直到第一个元素
    for (i = n - 1; i > 0; i--)
    {
        // 交换a[0]和a[i]。交换后，a[i]是a[0...i]中最大的。
        swap(a[0], a[i]);
        // 调整a[0...i-1]，使得a[0...i-1]仍然是一个最大堆。
        // 即，保证a[i-1]是a[0...i-1]中的最大值。
        maxheap_down(a, 0, i-1);
    }
}
```

## 连续子数组的最大和

```c
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res=INT_MIN,sum = 0;
        int l=0,r=0;
        for(int i =0;i<nums.size();i++)
        {
            //cout <<sum<< res<<endl;
            sum+=nums[i];
            if(sum<0)
            {
                res=max(res,sum);
                sum =0;
            }
            else res=max(res,sum);
        }
        return res;
    }
};
```

**阿秀ans:**

```c
int FindGreatestSumOfSubArray(vector<int> array) {
	for (int i = 1; i < array.size(); ++i) {
	    array[i] = max(0,array[i-1]) + array[i];
	}
	return *max_element(array.begin(),array.end());
}

```

牛@

## **整数中1出现的次数（从1到n整数中1出现的次数）**

```c
class Solution {
public:
    int cnt(int n)
    {
        int res=0;
        if(n%10==1) res++;
        while(n/=10)
        {
            if(n%10==1) res++;
        }
        return res;
    }
    int NumberOf1Between1AndN_Solution(int n) {
         int res=0;
        n++;
        while(n--)
        {
                res+=cnt(n);
        }
        return res;
    }
};
```

**阿秀ans:**





## **把数组排成最小的数**

没想到

**阿秀ans:**

```
string minNumber(vector<int>& nums) {

    vector<string> temp;
    for (auto num : nums) {
        temp.push_back(to_string(num));
    }

    sort(temp.begin(), temp.end(), [](const string& a, const string& b) { return a + b < b + a; });
    string result;
    for (auto& t : temp) {
        result += t;
    }
    return result;
}

```

## 丑数

```c
#include <map>
#include <queue>
#include <vector>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param index int整型 
     * @return int整型
     */
     bool isugle(int x)
     {
        while(x%2==0) x/=2;
        while(x%3==0) x/=3;
        while(x%5==0) x/=5;
        if(x==1) return true;
        return false;
     }
    int GetUglyNumber_Solution(int index) {
        // write code here
        
        int cnt=0;
        int res=0;
        while(cnt<index)\
        {
            res++;
            if(isugle(res)) cnt++;
        }
        return res;
    }
};
```

直接超时

**阿秀ans:**三个指针一直min

```c
int GetUglyNumber_Solution(int index) {
	if(index < 7) return index;
	vector<int> result(index, 0);
	result[0] = 1;
	int indexTwo = 0, indexThree = 0,indexFive = 0;
	for (int i = 1; i < index; ++i) {
		int minNum = min(min(result[indexTwo] * 2, result[indexThree] * 3), result[indexFive] * 5);
		if (minNum == result[indexTwo] * 2) indexTwo++;
		if (minNum == result[indexThree] * 3) indexThree++;
		if (minNum == result[indexFive] * 5) indexFive++;
		result[i] = minNum;
	}
	return result[index - 1];

}

```

牛！



## **第一个只出现一次的字符**



```c
#include <unordered_map>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param str string字符串 
     * @return int整型
     */
    int FirstNotRepeatingChar(string str) {
        // write code here
        int n = str.size();
        unordered_map<char,int> cnt;
        int res=0;
        for(int i = 0;i<n;i++)
        {
            cnt[str[i]]++;
        }
        for(int i = 0;i<n;i++)
        {
            if(cnt[str[i]]==1) return i;
        }
        return -1;
    }
};
```

**阿秀ans:**



## *逆序对

笔试做到过，二刷没想起用归并，看了提示后自己做的

```c
class Solution {
  public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param nums int整型vector
     * @return int整型
     */
    
    int  merge(vector<int>&nums,int l,int  r)
    {
        int res = 0;
        if(l>=r) return 0;
        int mid = (l+r)>>1;
        int r1 = merge(nums,l,mid);
        int r2 = merge(nums,mid+1,r);
        int i = l,j = mid+1;
        vector<int> temp;
        while(i<=mid&&j<=r)
        {
            if(nums[i]<=nums[j]) 
            {   
               
                temp.push_back(nums[i]);
                i++;
            }
            else 
            {
                res+=mid - i + 1;
                res %= 1000000007;
                temp.push_back(nums[j]);
                j++;
            }
        }
        while(i<=mid) temp.push_back(nums[i++]);
        while(j<=r) temp.push_back(nums[j++]);
        i=l,j=0;
        while(i<=r) nums[i++] = temp[j++];
        return (res +r1 + r2)%1000000007;
    }
    int InversePairs(vector<int>& nums) {
        // write code here
        int l = 0, r = nums.size() - 1;
        return merge(nums, l, r);
        //for(auto x:nums) cout << x<<endl;
    }
    //先用一个归并
};
```

**阿秀ans:**



## 两个链表的第一个公共结点

想到了那个快慢指针

```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *findFirstCommonNode(ListNode *headA, ListNode *headB) {
        unordered_map<ListNode *,bool> mp;
        while(headA!=nullptr)
        {
            mp[headA] = true;
            headA=headA->next;
        }
        while(headB!=nullptr)
        {
            if(mp[headB]) return headB;
            headB=headB->next;
        }
        return nullptr;
    }
};
```

**阿秀ans:**

```c
//定义两个指针, 第一轮让两个到达末尾的节点指向另一个链表的头部, 最后如果相遇则为交点(在第一轮移动中恰好抹除了长度差)
        两个指针等于移动了相同的距离, 有交点就返回, 无交点就是各走了两条指针的长度
ListNode* FindFirstCommonNode(ListNode* pHead1, ListNode* pHead2) {
	if (pHead1 == NULL || pHead2 == NULL) return NULL;
	ListNode* p1 = (ListNode*)malloc(sizeof(ListNode));
	ListNode* p2 = (ListNode*)malloc(sizeof(ListNode));
	p1 = pHead1;
	p2 = pHead2;
	while (p1 != p2) {
		p1 = (p1 == NULL ? pHead2 : p1->next);
		p2 = (p2 == NULL ? pHead1 : p2->next);
	}
	return p1;
}


```

如果 head1 走完了就从 head2 重新开始走

确实和快慢指针那题很像

##  **数字在升序数组中出现的次数**

```c
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param nums int整型vector 
     * @param k int整型 
     * @return int整型
     */
    int GetNumberOfK(vector<int>& nums, int k) {
        // write code here
        int res=0;
        for(int num : nums)
        {
            if(num==k) res++;
        }
        return res;
    }
};
```

但是如果测试样例数量级很大应该用二分；



```c
#include <type_traits>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param nums int整型vector 
     * @param k int整型 
     * @return int整型
     */
    int GetNumberOfK(vector<int>& nums, int k) {
        // write code here
       
        int res=0,l=0,n=nums.size(),r = n-1,mid;
        if(n==0) return 0;
        while(l<r)
        {
            mid = (l+r)>>1;
            if(nums[mid]>=k) r = mid;
            else l = mid+1;
        }
        res = r;
        if(nums[res]!=k) return 0;
        //cout << res <<endl;
        l = 0;
        r = n-1;
        while(l<r)
        {
            mid = (l+r+1)>>1;
            if(nums[mid]<=k) l = mid;
            else r = mid-1;
        }
        if(nums[l]!=k) return 0;
        //cout << l <<endl;
        return l - res+1;
    }
};
```

## 二叉树的深度

```c
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};*/
class Solution {
  public:
    int res = 0;
    void dfs(TreeNode* pRoot, int&& deep) {
        if (pRoot == nullptr) {
            res = max(res, deep);
            return;
        }
		else
		{
			dfs(pRoot->left,deep+1);
			dfs(pRoot->right,deep+1);
		}
		return;
	}
    int TreeDepth(TreeNode* pRoot) {
        int deep = 0;
        dfs(pRoot, static_cast<int &&>(move(deep)));
		return res;
    }
};

```

**阿秀ans:**

## 判断是不是平衡二叉树

```c
/**
 * struct TreeNode {
 *  int val;
 *  struct TreeNode *left;
 *  struct TreeNode *right;
 *  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
#include <climits>
#include <complex>
#include <valarray>
class Solution {
  public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param pRoot TreeNode类
     * @return bool布尔型
     */
    bool dfs(TreeNode* pRoot, int& hight) {
        if (pRoot == nullptr) 
        {
            hight=0;
            return true;
        }
        int l,r;
        if(dfs(pRoot->left, l)&&dfs(pRoot->right,r)){}
        hight = max(l,r)+1;
        //cout << pRoot->val << hight <<endl;
        return abs(l -r) <= 1;
    }

    bool IsBalanced_Solution(TreeNode* pRoot) {
        int l,r;
        if(pRoot==nullptr) return true;
        if(dfs(pRoot->left, l)&&dfs(pRoot->right,r)){}
        else return false;
        return abs(l -r) <= 1;
    }
};
```

还是定义不熟

1. 左右子树也是二叉平衡树
2. 左右子树的高度差<=1

**阿秀ans:**

## 数组只出现一次的数字

影响深刻，位运算，不做了

**阿秀ans:**

## **和为S的连续正数序列**

```c
#include <queue>
#include <vector>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param sum int整型 
     * @return int整型vector<vector<>>
     */
    vector<vector<int> > FindContinuousSequence(int sum) {
        // write code here
        
        int l=1,r = 2;
        int s = 1;
        vector<vector<int> > res;
        while(r<=sum)
        {
            s+=r;
            while(s>sum) 
            {
                s-=l;
                l++; 
            } 
            //cout << l << r <<s<<endl;
            if(sum==s&&r!=l)
            {
                vector<int> t;
                for(int i=l;i<=r;i++)
                {
                    t.push_back(i);
                }
                res.push_back(t);
            }
            r++;     
        }
        return res;
    }
};
```

**阿秀ans:**就是差不多的滑动窗口，俩指针



## **和为S的两个数字**

```c
class Solution {
public:
    vector<int> FindNumbersWithSum(vector<int> array,int sum) {
        int l=0,r = array.size()-1;
        while(l<r&&r>=0&&l<array.size())
        {
            
            int a = array[l],b = array[r];\
            //cout << a << b<<endl;
            if(a+b==sum) return {a,b};
            if(a+b<sum) l++;
            else r--;
        }
        return {};
    }
};
```

**阿秀ans:**第二种方法也是滑动窗口





## 左旋字符串

```c
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param str string字符串 
     * @param n int整型 
     * @return string字符串
     */
    string LeftRotateString(string str, int n) {
        // write code here
        
        int  m = str.size();
        if(!m) return "";
        n = n %m;
        string res1 = str.substr(n,m-n);
        string res2 = str.substr(0,n);
        return res1+ res2;
    }
};
```

**阿秀ans:**



## 翻转字符串

istringstream解法 c++没有split

```c
#include <vector>
#include <algorithm>
#include <sstream>
class Solution {
public:
    string ReverseSentence(string str) {
        vector<string> tokens;
        string token;
        std::istringstream tokenStream(str);
        while (std::getline(tokenStream, token, ' '))
            tokens.push_back(token);
        reverse(tokens.begin(), tokens.end());
        string res;
        for(auto s:tokens)
        {
            res+=s;
            res+=' ';
        }
        res.pop_back();
        return res;
    }
};
```

**阿秀ans:**

最简单的反向遍历也行





## 扑克顺子

```c
#include <algorithm>
#include <queue>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param numbers int整型vector 
     * @return bool布尔型
     */
    bool IsContinuous(vector<int>& numbers) {
        // write code here
        sort(numbers.begin(),numbers.end());
       
        int cnt=0;
        for(int i=4;i>=0;i--)
        {
            if(i==0||numbers[i-1]==0) 
            {
                cnt+=i;
                break;
            }
            else if(numbers[i] - numbers[i-1]==0) return false;
            else {
                cnt-=numbers[i] - numbers[i-1]-1;
            }
        }
        if(cnt>=0) return true;
        return false;
    }
};
```

**阿秀ans:**

max-min<5 且 除0外没有重复数字







## [ 孩子们的游戏(圆圈中最后剩下的数](https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=23265&ru=%2Fpractice%2Ff78a359491e64a50bce2d89cff857eb6&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&sourceUrl=)

```c
#include <vector>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param n int整型 
     * @param m int整型 
     * @return int整型
     */
    int LastRemaining_Solution(int n, int m) {
        // write code here
        vector<bool> flag(n, false);
        int last=n;
        int idx=0;
        while(last>1)
        {
            int cnt = m%last;
            while(cnt>0)
            {
                if(!flag[idx])
                {
                   cnt--;
                }
                if(cnt==0) flag[idx] = true;
                idx=(idx+1)%n;
            }
            cout << last << idx <<endl;
            last--;
        }
        while(flag[idx]) idx=(idx+1)%n;
        return idx;
    }
};
//-----
//2 1 3
```

>  idx=(idx+1)%n;
>
> 但是下一次
>
> cnt = m%last; 
>
> 若cnt==0则没有判断flag

卡了好久的边界，还是得逻辑清楚才行

```c
#include <vector>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param n int整型 
     * @param m int整型 
     * @return int整型
     */
    int LastRemaining_Solution(int n, int m) {
        // write code here
        vector<bool> flag(n, false);
        int last=n;
        int idx = 0;
        while(last>1) //这里是1不是0
        {
            int cnt = m%last;
            if(cnt==0) cnt = last;//这里要加不然等于0就不进循环
            while(cnt>0)
            {
                cnt--;
                if(cnt<=0)
                {
                    flag[idx] = true;
                } 
                idx = (idx + 1) % n;
                while (flag[idx]) idx = (idx + 1) % n;
            }
            last--;
            //cout << last << idx <<endl;
        }
        return idx;
    }
};

```

**阿秀ans:**

1. 环链表解法

2. https://www.bilibili.com/video/BV1so4y1o7KJ?p=4&vd_source=eef102f4fb053709a57c96d0c876628a

   ![image-20240716084053617](E:\codenotes\就业\剑指offer\img\image-20240716084053617.png)

``` c
Sum_Solution（n,m,n）
{
	(m+Sum_Solution（n-1,m,n-1）) %n;
}

f(n,m）=(m+f(n-1,m）) %n;

res = 0;
for(int i = 2;i<=n;i++)
{
	res = (res + m)%n
}

```

真有点绕

## **求1+2+3+...+n**

**阿秀ans:**

利用sizeof

```c
int Sum_Solution(int n) {
    bool a[n][n+1];
    return sizeof(a)>>1;
}

```

用&&终止递归

```c
int Sum_Solution(int n) {
int sumNum = n;
bool ans = (n > 0) && ((sumNum += Sum_Solution(n - 1)) > 0);
return sumNum;
}
```



## 不用加减乘除做加法

```c
class Solution {
public:
    int Add(int num1, int num2) {
        if(!num1&&!num2) return 0; 
        int res =  Add(num1>>1, num2>>1);
        if((num1&1)&(num2&1)) res++;
        res<<=1;
        if((num1&1)^(num2&1)) res++;
        return res;
    }
};
```

想到位运算，但是负数没用

**阿秀ans:**

```c
class Solution {
public:
    int Add(int num1, int num2) {
        // add表示进位值
        int add = num2;         
        // sum表示总和       
        int sum = num1;                
        // 当不再有进位的时候终止循环
        while(add != 0) {              
            // 将每轮的无进位和与进位值做异或求和
            int temp = sum ^ add;      
            // 进位值是用与运算产生的
            add = (sum & add) << 1;    
            // 更新sum为新的和
            sum = temp;                
        }
        return sum;
    }
};

```

## 把字符串转换成整数

```c
class Solution {
public:
    int strToInt(string str) {
        long res=0,n = str.size();
        bool flag=false;
        int i=0;
        while(str[i]==' ')
        {
            i++;
        }
        if(i<n)
        {
            if(str[i]=='-')
            {
                flag = true;
                i++;
            }
            if(str[i]=='+') i++;
        }

        for(;i<n;i++)
        {
            
            if(!isdigit(str[i])) break;
            res *=10;
            res += str[i]-'0';
            if(res>INT_MAX)
            {
                if(flag)return INT_MIN;
                else return INT_MAX;
            }
        }
        if(flag)return int(-res);
        return int(res);
    }
};
```

**阿秀ans:**也挺啰嗦的

## 找出数组种重复的数字

```c
class Solution {
public:
    int duplicateInArray(vector<int>& nums) {
        int n = nums.size();
        vector<bool> cnt(n+1,false);
        int res =-1;
        for(auto x:nums)
        {
            if(x<0||x>=n) return -1;
            if(cnt[x]) res = x;
            cnt[x] = true;
        }
        return res;
    }
};
```

**阿秀ans:**差不多

## 构建乘积数组

```c
#include <cstdio>
#include <vector>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param A int整型vector 
     * @return int整型vector
     */
    vector<int> multiply(vector<int>& A) {
        // write code here

        int n = A.size();
        vector<int> res(n,1);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(i!=j) res[i]*=A[j];
            }
        }
        return res;
    }
};
```

**阿秀ans:**

```c
vector<int> multiply(const vector<int>& A) {
	int len = A.size();
	vector<int> B(len,0);
	int temp = 1;
	for (int i = 0; i <len; temp*=A[i],++i) {

		B[i] = temp;
	}

	temp = 1;
	for (int i = len-1; i >= 0; temp *= A[i], --i) {

		B[i] = B[i]*temp;
	}
	return B;
}

```

从前面遍历一遍，再从后面遍历一遍

## 正则表达式匹配

```c
class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        bool f[n];
        int j = 0, i=0;
        for(;i<m&&j<n;i++)
        {
            char sj = s[j];
            if(p[i]=='*')
            {
                int k=j;
                while(j<n&&s[j]==sj) j++;
                {

                }
                continue;
            } 
            if(p[i]=='.'||p[i]==sj) j++;
        }
        if(j>=n&&i>=m) return true;
        return false;
    }
};
```

无法让*匹配0个字符

有点难，有点绕。

**阿秀ans:**递归

```c
 bool match(char* str, char* pattern)
    {
        if (*str == '\0' && *pattern == '\0')
            return true;
        if (*str != '\0' && *pattern == '\0')
            return false;
        //if the next character in pattern is not '*'
        if (*(pattern+1) != '*')
        {
            if (*str == *pattern || (*str != '\0' && *pattern == '.'))
                return match(str+1, pattern+1);
            else
                return false;
        }
        //if the next character is '*'
        else
        {
            if (*str == *pattern || (*str != '\0' && *pattern == '.'))
                return match(str, pattern+2) || match(str+1, pattern);
            else
                return match(str, pattern+2);
        }
    }

```

动态规划

```c
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size() + 1, n = p.size() + 1;
        vector<vector<bool>> dp(m, vector<bool>(n, false));
        dp[0][0] = true;
        for(int j = 2; j < n; j += 2)
            dp[0][j] = dp[0][j - 2] && p[j - 1] == '*';
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n; j++) {
                dp[i][j] = p[j - 1] == '*' ?
                    dp[i][j - 2] || dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'):
                    dp[i - 1][j - 1] && (p[j - 1] == '.' || s[i - 1] == p[j - 1]);
            }
        }
        return dp[m - 1][n - 1];
    }
};

作者：Krahets
链接：https://leetcode.cn/problems/regular-expression-matching/solutions/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```



### 正则

0到199

([0-1]?\\d{1,2})

## 显示数字的字符串

没找到题

大概思路是一个状态机

## 字符流第一个不重复的字符

```c
#include <queue>
class Solution
{
public:
    int cnt[300];
    queue<char> q;
    string res;
    int residx=0;
    Solution()
    {
        memset(cnt,0,sizeof(cnt));
    }
  //Insert one char from stringstream
    void Insert(char ch) {
        cnt[ch]++;
        q.push(ch);
        res+=getres();
    }
  //return the first appearence once char in current stringstream
    char getres() { 
        if(q.empty()) return '#';
        //cout << q.front()<< cnt[q.front()]<<endl;
        while(!q.empty()&&cnt[q.front()]!=1) q.pop();
        if(q.empty()) return '#';
        return q.front();
    }
    char FirstAppearingOnce()
    {
        return res[residx++];
    }
};

```

**阿秀ans:**感觉不如我的

```c
class Solution
{
public:
	//Insert one char from stringstream
	void Insert(char ch)
	{
		v.push_back(ch);
        result[ch]++;
	}
	//return the first appearence once char in current stringstream
	char FirstAppearingOnce()
	{
		for (auto &ch:v) {
			if (result[ch] == 1) return ch;
		}
		return '#';
	}

	vector<char> v;
    unordered_map<char,int> result;

};

```

## 链表中环的入口结点

```c

/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution {
public:
    ListNode* EntryNodeOfLoop(ListNode* pHead) {
        ListNode* slow =new ListNode(0);
        slow->next = pHead;
        ListNode* fast =new ListNode(0);
        fast->next = pHead;
        ListNode* Pd = fast;
        while(slow!=fast)
        {
            if(fast==nullptr||fast->next==nullptr) return nullptr;
            //cout <<slow->val << fast->val <<endl;
            slow = slow->next;
            fast = fast->next->next;
            
        }
        fast = Pd;
        while(slow!=fast)
        {
            slow = slow->next;
            fast = fast->next;
        }
        return fast;
    }
};
```

**阿秀ans:**

## 删除链表中的重复节点

```c

/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
#include <unordered_map>
class Solution {
public:
    ListNode* deleteDuplication(ListNode* pHead) {
        unordered_map<int, int> mp;
        ListNode* cur = pHead;
        while(cur!=nullptr)
        {
            mp[cur->val] ++;
            cur= cur->next;
        }

        ListNode*  res = new ListNode(-1);
        res->next = pHead;
        cur = res;
        while(cur->next!=nullptr)
        {
            //cout << cur->next->val << mp[cur->next->val] <<endl;
            if(mp[cur->next->val]>1) cur->next = cur->next->next;
            else cur=cur->next;
        }
        return res->next;
    }
};
```

**阿秀ans:**

### 自定义哈希



```c
// 定义自定义哈希函数
struct pair_hash {
    template <class T1, class T2>
    std::size_t operator()(const std::pair<T1, T2>& p) const {
        auto hash1 = std::hash<T1>{}(p.first);
        auto hash2 = std::hash<T2>{}(p.second);
        return hash1 ^ (hash2 << 1); // 组合两个哈希值
    }
};

```

### 哈希冲突

```c

int find(int x)
{
    int k=(x%N+N)%N;
    while(ha[k]!=null && ha[k]!=x)//如果当前哈希值的位置有数据并且这个数不是我们正在处理的这个数，就要向后找能放它的位置
    {
        k++;
        if(k==N)k=0;
    }
    return k;

```

使用一个数组存下了所有哈希值对应的x



##  **二叉树的下一个结点**

```c
/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {
        
    }
};
*/
class Solution {
public:
    void getmidored(TreeLinkNode* pNode,vector<TreeLinkNode*> &nums)
    {
        if(pNode==nullptr) return;
        getmidored(pNode->left,nums);
        nums.push_back(pNode);
        getmidored(pNode->right,nums);
        return;
    }
    TreeLinkNode* GetNext(TreeLinkNode* pNode) {
        vector<TreeLinkNode*> nums;
        getmidored(pNode,nums);
        for(int i=0;i<nums.size();i++)
        {
            //cout << nums[i]->val << endl;
        }
        for(int i=0;i<nums.size();i++)
        {
            if(pNode==nums[i]&&i!=nums.size()-1) return nums[i+1];
        }
        //cout << pNode->next->left->val << endl;
        while(pNode->next)
        {
            TreeLinkNode* next = pNode->next;
            if(next->left&&next->left==pNode) return next;
            pNode = next;
        }
        return nullptr;
    }
};

```

​	 1

2

​	 3

 		 4

找到第一个左拐

**阿秀ans:**

## [3112. 访问消失节点的最少时间](https://leetcode.cn/problems/minimum-time-to-visit-disappearing-nodes/)

```c
class Solution {
public:
    vector<int> ans;
    vector<vector<pair<int,int&>>> neibor;
    vector<bool> flag;
    struct Compare {
    vector<int>& ans;
    Compare(vector<int>& ansRef) : ans(ansRef) {}
    bool operator()(int a, int b) {
        return ans[a] > ans[b]; // 大小反转，实现最小堆
    }
    };
    vector<int> minimumTime(int n, vector<vector<int>>& edges, vector<int>& disappear) {
        int m  = edges.size();
        for(int i=0;i<n;i++)
        {
            ans.push_back(-1);
        }
        
        neibor.resize(n+1);
        flag.resize(n+1);
        for(int i=0;i<m;i++)
        {
            neibor[edges[i][0]].push_back({edges[i][1],edges[i][2]});
            neibor[edges[i][1]].push_back({edges[i][0],edges[i][2]});
        }
       

        function<void()> func = [&](){
            priority_queue<int,vector<int>,Compare> q{Compare(ans)};
            q.push(0);
            ans[0]=0;
            while(!q.empty())
            {
                int nd = q.top();
                q.pop();
                if(flag[nd]) continue;
                flag[nd] = true;
                for(auto p:neibor[nd])
                {
                    int ne = p.first;
                    if(disappear[ne]<=ans[nd]+p.second) continue;
                    if(ans[ne]==-1)
                    {
                        ans[ne] = ans[nd]+p.second;
                    } 
                    else  ans[ne] = min(ans[nd]+p.second,ans[ne]);
                    q.push(ne);
                }
            }
        };
        func();
        return ans;
    }
};

```

#### 优先队列排序

```c
  Compare(vector<int>& ansRef) : ans(ansRef) {}
    bool operator()(int a, int b) {
        return ans[a] > ans[b]; // 大小反转，实现最小堆
    }
    };
     priority_queue<int,vector<int>,Compare> q{Compare(ans)};
```



```cpp
priority_queue<int,vector<int>,greater<int>> q
```

==则是小根堆，要记住带上greater的是小，反过来的。==







## 对称的二叉树

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isbd(TreeNode*a, TreeNode*b)
    {
        if(a==nullptr||b==nullptr)
        {
            return(a==nullptr&&b==nullptr);
        }
        if(a->val!=b->val) return false;
        return isbd(a->left,b->right)&&isbd(a->right,b->left);
        
    }

    bool isSymmetric(TreeNode* root) {
        return isbd(root->left,root->right);
    }
};
```



## 之字形打印

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> printFromTopToBottom(TreeNode* root) {
        stack<TreeNode*>  st;
        stack<TreeNode*> temp;
        st.push(root);
        vector<vector<int>>  res;
        //res.push_back({root->val});
        vector<int> row;
        bool left = true;
        while(!st.empty())
        {
            
            TreeNode* t = st.top();
            st.pop();
            if(t!=nullptr)
            {
                if(left)
                {
                    temp.push(t->left);
                    temp.push(t->right);
                }
                else {
                     temp.push(t->right);
                     temp.push(t->left);
                }
                row.push_back(t->val);
            }
            if(st.empty())
            {
                left = !left;
                res.push_back(row);
                row.clear();
                st = temp;
                temp = stack<TreeNode*>();
            }
           
        }
        res.pop_back();
        return res;
    }
};
```

## 二叉树打印成多行

```c
/**
 * struct TreeNode {
 *	int val;
 *	struct TreeNode *left;
 *	struct TreeNode *right;
 *	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
#include <vector>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param pRoot TreeNode类 
     * @return int整型vector<vector<>>
     */
    vector<vector<int> > Print(TreeNode* pRoot) {
        // write code here
        vector<TreeNode*> temp;
        vector<TreeNode*> row;
        temp.push_back(pRoot);
        vector<vector<int>> res;
        while(!temp.empty())
        {
            row = temp;
            temp.clear();
            vector<int> rowval;
            for(auto nd:row)
            {
                if(nd==nullptr) continue;
                rowval.push_back(nd->val);
                temp.push_back(nd->left);
                temp.push_back(nd->right);
            }
            res.push_back(rowval);
        }
        res.pop_back();
        return res;
    }
};
```



## 序列换二叉树

```c
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
#include <cstdio>
#include <algorithm>
#include <numeric>

class Solution {

public:
    string SerializeCode(TreeNode *root)
    {
        string res;
        if(root==nullptr) return "#!";
        string l = SerializeCode(root->left);
        string r = SerializeCode(root->right);
        res =  to_string(root->val) + "!" + l+r;
        //cout << res<< endl;
        return res;
    }
    char* Serialize(TreeNode *root) {       
        
        string s = SerializeCode(root);
        char* res = new char[s.size()+1];
        for(int i=0;i<s.size();i++)
        {
            res[i] = s[i];
        }
        return res;
    }
    TreeNode* Deserializecode(char * &str) {

        if(*str=='#')
        {   
            str++;
            return nullptr;
        }
        int val = 0;
        while(*str!='!')
        {
            val = val * 10 + *(str++) - '0';
        }
        //cout << val <<endl;
        TreeNode* head = new TreeNode(val);
        head->left  = Deserialize(++str);
        head->right = Deserialize(++str);
        return head;
    }
    TreeNode* Deserialize(char * &str) {
        return Deserializecode(str);
    }
};
```

## [二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)



```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    struct cmp
    {
        bool operator()(int a,int b)
        {
            return a>b;
        }
    };
    int kthSmallest(TreeNode* root, int k) {
        priority_queue<int,vector<int>,cmp> q;
        queue<TreeNode*> t;
        t.push(root);
        while(!t.empty())
        {
            TreeNode* nd= t.front();
            t.pop();
            if(nd==nullptr) continue;
            cout << nd->val <<endl;
            q.push(nd->val);
            t.push(nd->left);
            t.push(nd->right);
            
        }
        while(k-->1)
        {
            q.pop();
        }
        return q.top();
    }
};
```

超时了

**阿秀ans:**这是搜索树，是有序的，我当全无序做的

中序遍历

```c
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int midsearch(TreeNode* root, int &k)
    {
        if(root==nullptr||k<=0) return -1;
        int t = midsearch(root->left,k);
        if(t!=-1) return t;
        if(--k==0) return root->val;
        return midsearch(root->right,k);
    }
    int kthSmallest(TreeNode* root, int k) {
       return midsearch(root,k);
    }
};
```



## 数据流的中位数

```c
class Solution {
private:
    int count = 0;
    priority_queue<int,vector<int>,less<int>> left_big;
    priority_queue<int,vector<int>,greater<int>> right_small;
public:
    void Insert(int num)
    {
        count++;
        if(count%2 == 1){ //奇数
            right_small.push(num);
            left_big.push(right_small.top());
            right_small.pop();
        }else{
            
            left_big.push(num);
            right_small.push(left_big.top());
            left_big.pop();
        }
    }

    double GetMedian()
    { 
    
        if(count %2 == 1) return left_big.top();
        else{
            return double((left_big.top() + right_small.top())/2.0);
        }
    }

};

```

坐标大根堆，右边小根堆，但是要求左边所有数字小于右边，

所以每次插入后如果是奇数，就先插入右边小根堆，再把右顶移到左边

所以每次插入后如果是偶数，就先插入左边大根堆，再把左顶移到右边



## 滑动窗口的最大值

```c
#include <queue>
#include <utility>
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param num int整型vector 
     * @param size int整型 
     * @return int整型vector
     */
    typedef pair<int,int> PII;
    vector<int> maxInWindows(vector<int>& num, int size) {
        // write code here
        deque<PII> q;
        vector<int> res;
        if(size==0||num.size()<size) return {};
        for(int i=0;i<num.size();i++)
        {
            //for(auto x:q) cout << x.first ;
            while(!q.empty()&&q.back().first<num[i]) q.pop_back();
            while(!q.empty()&&(q.front().second<=i-size)) q.pop_front();
            q.push_back({num[i],i});
            //for(auto x:q) cout << x.first ;
            //cout << endl;
            if(i>=size-1) res.push_back(q.front().first);
        }
        return res;
    }
};
```

md!怎么一些细节不严谨的错误找不到，debug太弱了
