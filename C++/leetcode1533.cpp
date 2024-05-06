
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};

class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        printf("%d", root->val);
        if(root==nullptr){
            printf("True");
            return NULL;
        };
        if(root->left != NULL && root->right != NULL){
            Node* lp = treeToDoublyList(root->left);
            Node* rp = treeToDoublyList(root->right);
            if(lp->right!=NULL){
                root->left = lp->right;
                lp->right->right = root;
            }else{
                root->left = lp;
                lp->right = root;
            };

            if(rp->left!=NULL){
                root->right = rp->left;
                rp->left->left = root;
            }else{
                root->right = rp;
                rp->left = root;
            };
        }else if(root->left != NULL){
            Node* lp = treeToDoublyList(root->left);
            if(lp->right!=NULL){
                root->left = lp->right;
                lp->right->right = root;
            }else{
                root->left = lp;
                lp->right = root;
            };
        }else if(root->right != NULL){
            Node* rp = treeToDoublyList(root->right);
            if(rp->left!=NULL){
                root->right = rp->left;
                rp->left->left = root;
            }else{
                root->right = rp;
                rp->left = root;
            };
        };
    return root;
    };
};