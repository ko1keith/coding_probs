class MergeTwoSortedLists:
    def merge_two_sorted_lists(self, list1, list2):
        print(list1)
        print(list2)
        new_list = []
        for num in list2:
            print(num)
            # new_list.append(list1[i])
            # print(new_list)
            # for j in range(len(list2)):
            #     if list2[j] > list1[j]:
            #         new_list.append(list2[j])
            #     else:
            #         new_list.insert(j, list2[j])
        return new_list
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next