#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string to_uppercase(string s){
    for(int i=0; i<s.size(); i++){
        if(s[i] >='a' && s[i] <='z'){
            s[i] = s[i] - 32;
        }
    }
    return s;
}

int solution(int cacheSize, vector<string> cities) {
    if(cacheSize==0) // 예외처리
        return cities.size() * 5;
    
    int answer = 5;
    vector<string>cache;
    cache.push_back(to_uppercase(cities[0]));
                                                   
    int j = 0;
    for(int i=1; i<cacheSize; i++){
        for(j=0; j<cache.size(); j++){
            if(cache[j] == to_uppercase(cities[i])){ // hit
                cache.erase(cache.begin()+j);
                cache.push_back(to_uppercase(cities[i]));
                answer++;
                break;
            }
        }
        if(j==cache.size()){ // miss
            cache.push_back(to_uppercase(cities[i]));
            answer = answer + 5;
        }
    }
    
    
    for(int i=cacheSize; i<cities.size(); i++){
        for(j=0; j<cache.size(); j++){
            if(cache[j] == to_uppercase(cities[i])){ // cache hit
                cache.erase(cache.begin()+j);
                cache.push_back(to_uppercase(cities[i]));
                answer++;
                break;
            }
        }
        if(j==cache.size()){ // cache miss
            if(cache.size()==cacheSize)
                cache.erase(cache.begin());
            cache.push_back(to_uppercase(cities[i]));
            answer = answer + 5;
        }
    }
    return answer;
}