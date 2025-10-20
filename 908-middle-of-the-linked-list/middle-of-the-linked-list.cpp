/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        //count
        int nodes = 0;
        ListNode* cur = head;
        while(cur){
            nodes++;
            cur = cur->next;
        }
        //find mid
        int mid = nodes/2;
        // cout<<mid<<endl;
        // if (nodes % 2 == 0){
        //     mid++;
        // }
        // cout<<mid;
        //find the node
        cur = head;
        for (int i =0;i<mid;i++){
            cur = cur->next;
        }
        return cur;
    }
};