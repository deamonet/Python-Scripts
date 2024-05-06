// for a node *p
// postOrder

typedef struct threadNode
{
    int val;
    struct threadNode *lchrild, *rchrild;
    int lflag, rflag;
}threadNode, *threadTree;


threadNode firstNode(threadNode *p)
{
    if(p->lflag == 0) // if left chrild exist
    {
        p = p->lchrild
        while(p->rflag == 1){p = }
        return p->lchrild;
    }
    else{while }
}