# 이것이 취업을 위한 코딩 테스트다 with 파이썬

그래프 시각화 사이트 : https://csacademy.com/app/graph_editor/

10^8 = 1초
- N <= 20 : 왠만한 알고리즘으로 모두 통과 가능
- N <= 100 : 3중 for문 통과 가능(10^6)
    - 플로이드 워셜
- N <= 1000 : 적당한 2중 for문 통과 가능(10^6)
    - 벨만 포드
- N <= 10000 : O(N) 또는 O(NlogN)
    - 동적프로그래밍
    - 이분탐색
    - 다익스트라
    - 유니온파인드
    - 세그먼트 트리
    - 투 포인트
- N <= 10^8 : 수학적 접근 필요 O(logN)
    - 유클리디안 호제법

## 1. 그리디 알고리즘
- 큰 수의 법칙
- 숫자 카드 게임
- 1이 될 때까지
- 프로그래머스 스쿨
    - 체육복
- BOJ
    - 동전
    - 회의실 배정
    - ATM
    - 잃어버린 괄호
    - 주유소(dp)

## 2. 구현
- 상하좌우
- 시각
- 왕실의 나이트
- 게임개발

## 3. 그래프탐색
- 음료수 얼려 먹기
- 미로 탈출
- BOJ
    - 알고리즘 수업 - 깊이 우선 탐색 1
    - 알고리즘 수업 - 깊이 우선 탐색 2
    - 알고리즘 수업 - 너비 우선 탐색 1
    - 알고리즘 수업 - 너비 우선 탐색 2
    - 바이러스
    - DFS와 BFS
    - 단지번호붙이기
    - 유기농 배추
    - 미로 탐색
    - 숨바꼭질
    - 나이트의 이동
    - 토마토(탐색 전 미리 익은 토마토를 한 번에 넣고 시작해야 하는 유형)
    - 토마토2
    - 뱀과 사다리 게임
    - 벽 부수고 이동하기

## 4. 정렬
- 위에서 아래로
- 성적이 낮은 순서로 학생 출력하기
- BOJ
    - 대표값
    - 커트라인
    - 수정렬하기2

## 5. 이분 탐색
- 부품찾기
- 떡볶이떡만들기
- BOJ
    - 수 찾기
    - 숫자 카드2
    - 랜선 자르기
    - 나무 자르기
    - 공유기 설치
    - K번째 수

## 6. 다이나믹 프로그래밍
- 1로 만들기
- 개미 전사
- 바닥 공사
- 효율적인 화폐 구성

## 7. 최단 경로
- 다익스트라
- 플로이드워셜
- 미래도시
- 전보
- BOJ
    - 최단 경로
    - 특정한 최단 경로
    
## 8.그래프 이론
- 유니온파인드(경로압축)
- 사이클 판별
- 크루스칼알고리즘
- 위상정렬
- 팀결성
- 도시 분할 계획
- 커리 큘럼
- BOJ
    - 여행가자
    - 친구네트워크
    - 상근이의 여행
    - 최소 스패닝 트리
    - 줄 세우기