# 내부 미세먼지 값 예측 모델

외부 미세먼지, 기온, 습도 데이터의 회귀분석으로 예측모델을 생성하여 내부 미세먼지 값을 예측하는 서비스입니다.

# 구성도

* 개발 당시 AWS EC2 를 사용해 구축한 서버가 존재하지 않습니다

# 사용 스택
  Python ( Socket, Matplotlib )  
  Arduino ( C language ) - [Uno board, DHT-22(humidity, temperarture), SDS011(finedust)]  
  MongoDB ( Compass )  
  AWS EC2  
  
# 결과물 스크린샷


<div>
  
<img src="https://user-images.githubusercontent.com/50613287/93665831-99d2ae80-fab4-11ea-8deb-779e79b51e64.png"  width="30%" height="40%">

<img src="https://user-images.githubusercontent.com/50613287/93665828-97705480-fab4-11ea-964f-09786e5937d4.png"  width="30%" height="40%">

<img src="https://user-images.githubusercontent.com/50613287/93665833-9b03db80-fab4-11ea-9c0c-9375e608ccdd.png"  width="30%" height="40%">
</div>
