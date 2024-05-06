
// 實現鏈棧
#define MaxSize 10
typedef struct Node{
    int val;
    int location;
    struct Node *down;
} Node;


bool initial(void){
    Node *head;
    head->val = 0;
    head->location = -1;
    head->down = NULL;
}


bool push(Node *head, int x){
    Node *top;
    top->val = x;
    top->location = ++head->location
    top->down = 

}
