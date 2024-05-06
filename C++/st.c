class Solution {
public:
    int myAtoi(string str) {
        int len = size(str);
        if(len==0){return 0;};
        int cnt = 0;
        int res = 0;
        int num;
        for(int i=0; i<len; i++){
            num = (int)str[i] - 48;
            printf("%d", i);
            if(str[i]==' '){
                continue;
            }else if(str[i]=='-'){
                if(cnt > 0){
                    return res;
                }else{
                    cnt =cnt + 13;
                };

            }else if(str[i]=='+'){
                if(cnt > 0){
                    return res;
                }else{
                    cnt = cnt + 17;
                };
            }else if(num>=0 && num<=9){
                printf("Ture");
                printf("%d\n", num);
                printf("%d\n", res);
                if(cnt == 17 || cnt == 0){
                    if(res <= (INT_MAX - num) / 10){
                        res = res * 10 + num;
                    }else{
                        return INT_MAX;
                    };  
                }else if(cnt == 13){
                    if(res > 0){res = 0 - res;};

                    if(res >= (INT_MIN + num) / 10){
                        res =  res * 10 - num;
                    }else{
                        return INT_MIN;
                    };
                }else{
                    if(cnt==13 && res > 0){res = 0-res;}
                    else{return res;};
                };
            }else{
                if(cnt==13 && res > 0){res = 0-res;}
                return res;
            };
        };
        if(cnt==13 && res > 0){res = 0-res;}
        return res;
    };
};