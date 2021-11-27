# Ontact- BackEnd (2021.03.02 - 2021.11.30) 💻
#### 인공지능과 빅데이터 분석을 활용한 SNS 감정 분석 프로그램(온(On/溫)택트)

## 주요 기술
- SNS 감정분석 : 사용자가 트위터 ID를 통해 자신의 글을 감정분석하여 온도를 확인할 수 있다.
- 단어 분석 : 글의 단어를 온,중,냉으로 분류하여 단어의 긍정, 중립, 부정을 알 수 있다.


## 구성도
<img width="700" alt="ontact" src="https://user-images.githubusercontent.com/43837921/126651703-f2896e5b-1d1d-48f5-9e03-766308925914.png">


## 흐름도
<img width="700" alt="ontact" src="https://user-images.githubusercontent.com/43837921/126651838-c8513e64-8bfd-4dc0-8942-c92b1acca626.png">


## 주요 기능
|             Function             |                         Description                          |
| :------------------------------: | :----------------------------------------------------------: |
|         ![](https://img.shields.io/badge/검색창-pink)         | - 사용자가 트위터 아이디를 입력하면 Twitter api를 사용하여 트위터 타임라인 게시물을 가져온다.|
| ![](https://img.shields.io/badge/글감정분석-pink) | - 불러온 트위터 글로 사용자의 평균 글 온도를 알 수 있다.|
|          ![](https://img.shields.io/badge/감정에따른단어분류-pink)          | - 분석한 사용자의 글을 단어로 토큰화하여 긍정, 중립, 부정의 단어인 삼 단계로 분류할 수 있다. |
|     ![](https://img.shields.io/badge/단어빈도수확인-pink)     | - 게시글에 자주 쓰인 단어의 빈도수를 파이썬의 라이브러리를 사용하여 워드 클라우드로 시각화하여 보여준다. |
|       ![](https://img.shields.io/badge/월별온도변화그래프-pink)       | - 사용자가 월별로 정리된 글의 온도 변화 추이를 볼 수 있다.<br>- 월별 평균 온도를 확인할 수 있다.   |
|         ![](https://img.shields.io/badge/온도캘린더-pink)         |- 글을 한 번 불러오면, 글이 시작된 날짜부터 현재 불러온 날짜까지 확인할 수 있는 캘린더가 된다.<br>- 글이 올라온 날짜에 따른 글의 온도를 캘린더를 통해 일별로 확인할 수 있다.|
|    ![](https://img.shields.io/badge/내정보-pink)     |- 프로필 사진을 설정할 수 있다.<br>- 이메일과 트위터 아아디, 또한 사용자의 평균 글 온도까지 보여준다.<br>- ’정보 수정하기‘ 버튼을 수정할 수 있다. |

## 유튜브 영상
https://www.youtube.com/watch?v=FLJUJj9FRHw

## Member
- 박소은
- 김유빈

