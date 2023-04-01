#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

bool com(string a, string b){
    return a.length()<b.length();
}

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end(), com);
    map<string, int>M;
    int size = phone_book[0].length(); //최소 길이 저장
    int idx =0;
    bool check = true;
    while(phone_book[idx].length() <= size && idx<phone_book.size())
    {   M.insert(make_pair(phone_book[idx], idx));
        idx++;
    }
    
    for(int i= idx; i<phone_book.size(); i++){
        string str = "";
        for(int j=0; j<size; j++)
            str += phone_book[i][j];
        
        if(M.count(str) == 0){
            M.insert(make_pair(str, i));
        }
        else{
            int tmp = M[str];
            int tmp_sz = phone_book[tmp].length();
    
            for(int k=size; k<tmp_sz; k++){
                if(phone_book[tmp][k] != phone_book[i][k]){
                    check = false;
                    break;
                }
                else check = true;
            }
            
            if(check == false){
                answer = true;
            }
            else{
                return false;
                
            }
           
        }
    }

    return answer;
}