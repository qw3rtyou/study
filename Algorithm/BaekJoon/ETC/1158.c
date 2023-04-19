#include <stdio.h>
#include <stdlib.h>

//노드 구조체 선언, 데이터는 단순 정수로 함
typedef struct node{
	int val;
	struct node* next;
}Node;

//스택처럼 맨 마지막에 값을 추가하고 헤드 리턴
Node* add(Node* head, int val) {
	Node* new_node = (Node*)malloc(sizeof(Node));

	new_node->val = val;
	new_node->next = NULL;

	if (!head) return new_node;

	Node* curr = head;

	while (curr->next) curr = curr->next;
	curr->next = new_node;

	return head;
}

//인덱스가 주어지면 그 인덱스에 있는 노드 삭제 후 헤드 리턴
Node* delete_at_index(Node* head, int index) {
	if (!head) return NULL;
	if (index == 0) {
		Node* new_head = head->next;
		free(head);
		return new_head;
	}

	Node* curr = head;

	for (int i = 0; i < index - 1; i++) {
		if (!curr) return NULL;
		curr = curr->next;
	}
	if (!curr || !curr->next) {
		return NULL;
	}

	Node* node_to_delete = curr->next;
	curr->next = curr->next->next;
	free(node_to_delete);

	return head;
}

//인덱스가 주어지면 값을 리턴
int get(Node* head, int index) {
	if (!head) return -1;

	Node* curr = head;

	for (int i = 0; i < index; i++) {
		if (!curr) return -1;
		curr = curr->next;
	}

	if (!curr) return -1;
	return curr->val;
}

int main() {
    int size,idx;

    scanf("%d %d",&size,&idx);
    
    Node* head = (Node*)malloc(sizeof(Node));
    head->val = 1;
    head->next = NULL;

    for (int i = 2; i < size+1; i++) add(head, i);

    int tmpi=0;

    printf("<");
    while(size!=1){
	    tmpi=(idx+tmpi-1)%size;
        printf("%d, ",get(head,tmpi));
        head=delete_at_index(head,tmpi);
        size--;
    }
    printf("%d>\n",get(head,0));

    return 0;
}
// 1234567