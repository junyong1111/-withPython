#include <string>
#include <algorithm>
#include <vector>

using namespace std;

string to_uppercase(string str){
    for(int i=0; i<str.length(); i++){
        if(str[i] >= 'a' && str[i] <= 'z')
            str[i] = str[i] - 32;
    }
    return str;
}

int clustering(vector<string>&s1, vector<string>&s2)
{
    // 있으면 새로운 교집합 
    // 없으면 s1 + 합집합
    if(s1.size() < s2.size()){
        vector<string>tmp = s1;
        s1  = s2;
        s2 = tmp;
    }
    vector<string>v1;
    vector<string>v2 = s1;
    int j = 0;
    for(int i=0; i<s2.size(); i++){
        string key = s2[i];
        bool check = false;
        for(j=0; j<s1.size(); j++){
            if(s1[j] == key){ // 교집합
                s1.erase(s1.begin() + j);
                v1.push_back(key);
                check = true;
                break;
            }
        }
        if(check == false) // s1+ 합집합
            v2.push_back(key);
    }
    return ((double)v1.size() / (double)v2.size()) * 65536;;
}


vector<string> cut_str(string from){
    vector<string>s;
    
    for(int i=0; i<from.length()-1; i++){
        string temp = "";
        if(from[i] >= 'A' && from[i] <='Z'){
            if(from[i+1] >= 'A' && from[i+1] <='Z'){
                temp += from[i];
                temp += from[i+1];
                s.push_back(temp);
            }
        }
    }
    return s;
}

int solution(string str1, string str2) {
    int answer = 0;
    str1 = to_uppercase(str1);
    str2 = to_uppercase(str2);
    vector<string>s1 = cut_str(str1);
    vector<string>s2 = cut_str(str2);
    if(s1.size() == 0 && s2.size()==0)
        return 65536;
    if(s1.size() == 0 || s2.size()==0)
        return 0;
    answer = clustering(s1, s2);
    return answer;
}