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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* newList = new ListNode;
        ListNode* cur = newList;
        while(list1 and list2){
            if(list1->val <= list2->val){
                cur->next = list1;
                cur = list1;
                list1 = list1->next;
            } else {
                cur->next = list2;
                cur = list2;
                list2 = list2->next;
            }
        }
        if (list1){
            cur->next = list1; 
        } else {
            cur->next = list2;
        }
        return newList->next;
    }
};