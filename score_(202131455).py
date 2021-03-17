# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:54:09 2021

@author: User
"""

data = input('1회차, 2회차,3회차,4회차, ... 13회차,14회차,15회차 점수입력')
exam1 = int(input('중간고사'))
exam2 = int(input('기말고사'))
print(data.split())
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15=map (int,data.split())
sam_a = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15
di = sam_a/15
mu = di*0.4
mu1 = exam1*0.3
mu2 = exam2*0.3
score = mu+mu1+mu2 
if 100>= score >=90:
    grade='A'
elif 90>score>=80:
    grade='B'
elif 80>score>=70:
    grade='C'
elif 70>score>=60:
    grade='D'
elif score<60:
    grade='F'
print ('%3d/ %3d/ %3d/ %3d/ %3d/ %3d/ %3d/ %3d/ %3d/ %3d/ %3d/ %3d/ %3d/ %3d/ %3d/ 총합 %3d/ 평균값 %6.2f/ 비중값 %6.2f ' 
       %(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,sam_a, di, mu)) 
print ('과제평균(40%) :' ,mu, '중간평균 (30%):',mu1,'기말평균(30%):',mu2,'총합:',mu+mu1+mu2)
print ('등급은',grade, '입니다.')   
