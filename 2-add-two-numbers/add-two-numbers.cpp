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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result =new ListNode;
        ListNode* cur = result;
        int carry = 0;
        while(l1 && l2){
            ListNode* temp = new ListNode;
            temp->val = (l1->val + l2->val + carry);
            carry = 0;
            if(temp->val >= 10){
                temp->val -= 10;
                carry = 0;
                carry++;
            }
            cur->next = temp;
            cur = cur->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while(l1){
            ListNode* temp = new ListNode;
            temp->val = l1->val + carry;
            carry = 0;
            if(temp->val >= 10){
                temp->val -= 10;
                carry = 0;
                carry++;
            }
            cur->next = temp;
            cur = cur->next;
            l1 = l1->next;
        }
        while(l2){
            ListNode* temp = new ListNode;
            temp->val = l2->val + carry;
            carry =0;
            if(temp->val >= 10){
                temp->val -= 10;
                carry = 0;
                carry++;
            }
            cur->next = temp;
            cur = cur->next;
            l2 = l2->next;
        }
        if(carry != 0){
            ListNode* temp = new ListNode;
            temp->val = carry;
            cur->next = temp;
            cur = cur->next;
        }
        return result->next;
    }
};