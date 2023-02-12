#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    map<string, int>map;
    int i = 1;
    for(i=1; i<= 26; i++){
        string str = "";
        str = 'A' + i-1;
        map.insert(make_pair(str,i));
    }
    // 길이가 1인경우 조건에 맞게 사전 생성
    
    string compare = "";
    for(int j=0; j<msg.size(); j++){
        compare = compare + msg[j];
        if(map.count(compare) == 0){ // 현재 입력과 일치치하는 가장 긴 문자열 w이 없다면
            map.insert(make_pair(compare, i++)); // 해당 값을 사전에 등록
            compare.erase(compare.end()-1); // 맨 마지막 글자를 삭제
            answer.push_back(map.at(compare)); // 입력값을 제외한 이전 문자열에 대한 사전값 등록
            compare = msg[j]; // 문자 갱신
        }        
    }
    answer.push_back(map.at(compare));
    return answer;
}