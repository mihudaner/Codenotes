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

```
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

## *重建二叉树

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

