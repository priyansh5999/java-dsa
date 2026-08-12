#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {

public:

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;

        int carry = 0;

        while (l1 != nullptr || l2 != nullptr || carry != 0) {

            int x = (l1 != nullptr) ? l1->val : 0;
            int y = (l2 != nullptr) ? l2->val : 0;

            int sum = x + y + carry;

            carry = sum / 10;

            current->next = new ListNode(sum % 10);
            current = current->next;

            if (l1 != nullptr) {
                l1 = l1->next;
            }

            if (l2 != nullptr) {
                l2 = l2->next;
            }
        }

        return dummy->next;
    }
};

void printList(ListNode* head) {
    while (head != nullptr) {
        std::cout << head->val << " ";
        head = head->next;
    }
    std::cout << std::endl;
}

int main() {
    Solution solution;

    // Example 1:
    ListNode* l1 = new ListNode(2);
    l1->next = new ListNode(4);
    l1->next->next = new ListNode(3);

    ListNode* l2 = new ListNode(5);
    l2->next = new ListNode(6);
    l2->next->next = new ListNode(4);

    ListNode* result = solution.addTwoNumbers(l1, l2);
    printList(result);

    // Example 2:
    l1 = new ListNode(0);
    l2 = new ListNode(0);

    result = solution.addTwoNumbers(l1, l2);
    printList(result);

    // Example 3:
    l1 = new ListNode(9);
    l1->next = new ListNode(9);
    l1->next->next = new ListNode(9);
    l1->next->next->next = new ListNode(9);
    l1->next->next->next->next = new ListNode(9);
    l1->next->next->next->next->next = new ListNode(9);
    l1->next->next->next->next->next->next = new ListNode(9);

    l2 = new ListNode(9);
    l2->next = new ListNode(9);
    l2->next->next = new ListNode(9);
    l2->next->next->next = new ListNode(9);

    result = solution.addTwoNumbers(l1, l2);
    printList(result);

    return 0;
}