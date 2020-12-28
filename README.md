# dreamai_zizonedrone
꿈꾸는 AI 프로젝트 - zi존드론파

## 👾대회 사이트👾
[꿈꾸는아이](https://dreamai.kr/fair_intel)

## Introduction
2020 DREAM_AI Drone Competition 프로젝트 (2020/10/26 ~ 2020/12/5)
#### Lecture001-데이터모으기.ipynb
이미지 데이터 수집
#### Lecture002-이미지분류&모델트레이닝.ipynb
이미지분류 & 모델 트레이닝 코드
#### Lecture003-파일변환과 테스트.ipynb
학습한 model을 드론에 적용하기 위한 파일변환 코드
#### Lecture004-실시간 추론하기.ipynb
학습한 model 적용하여 INTEL NUC의 카메라에서 추론하기
#### Lecture005-드론으로 추론하기
학습한 model을 드론에 적용하여 객체 인식
#### imageNet.py
ImageNet(http://www.image-net.org/) 이미지 소스 얻기
#### webCrawling.py
구글 웹 크롤링 코드
#### 카메라연속촬영.py
opencv 기반 웹캠(내장/외장) 연속촬영 코드

## 대회일정
01. 사전 교육 ( 온라인 )	@2020년 10월 26일 → 2020년 11월 1일	
02. 예선 참가팀 통보	@2020년 10월 23일	
03. 드론 날리기 실습 ( 오프라인 )	@2020년 11월 2일 → 2020년 11월 7일	
04. 예선 진행 ( 오프라인 )	@2020년 11월 20일 → 2020년 11월 21일	
05. 참가 신청 마감	@2020년 10월 16일	
06. 드론 본선	@2020년 12월 4일 → 2020년 12월 5일	
07. 드론파 회의	@2020년 11월 11일 오전 11:00-오후 4:00	
08. zi존드론파 회의	@2020년 11월 15일	
09. 데이터 수집 완료	@2020년 11월 17일	
10. zi존드론파 회의	@2020년 11월 18일	
11. 드론파 드론 날리기	@2020년 11월 19일
---
##⭐Intel NUC에서 jupyter notebook 실행하기⭐
1. 전원 켜서 비밀번호 `1234`
2. 와이파이 잘 연결 됐는지 확인
3. `ctl+alt+t` : 터미널 창 켜기
4. `cd test`  : test 폴더 이동
5. `source test2/bin/activate`
6. `jupyter notebook`
---
## 💾data💾
### 구글 드라이브 링크: [꿈꾸는 ai dataset](https://drive.google.com/drive/u/0/folders/1hxpAGKJiZOvKl_rldWySJR5TYUrBb_5p)
사용여부|classname|count|in charge|
:---:|:---:|---:|:---:|
Yes|airplane|5441||Jaeyoung Lee|
Yes|car|8653|Jaeyoung Lee|
Yes|boat|2959|Jaeyoung Lee|
Yes|bottle|4931|Jaeyoung Lee|
Yes|bird||JH Si|
Yes|cat|1647|JH Si|
Yes|dog|4661|JH Si|
Yes|horse|2649|Hyeonhui JEON|
Yes|person|5139|Hyeonhui JEON|
Yes|train|1460|Hyeonhui JEON|
Yes|drone|1111|Hyeonhui JEON|
Yes|minions|335|Hyeonhui JEON|
Yes|intel|73|Hyeonhui JEON|
Yes|NVIDIA|66|Hyeonhui JEON|
Yes|GIST|43|Hyeonhui JEON|
Yes|AWS|93|Hyeonhui JEON|
Yes|LG|120|Hyeonhui JEON|
Yes|CJ Olive networks|11|Hyeonhui JEON|
Yes|KOPTI 한국광기술원|26|Hyeonhui JEON|
Yes|hamburger||JH Si|
Yes|rock|||	
Yes|paper|541||	
Yes|sissor|||
---
## 참고 강의
[1. 인공지능 overview 640](https://www.notion.so/1-overview-640-bedce244ae3d42cf8c1d93c6c22af115)

[2. Inference with OpenVINO](https://www.notion.so/2-Inference-with-OpenVINO-0dfd6af91a994046835e7752d7782309)
