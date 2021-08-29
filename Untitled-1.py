#!/usr/bin/env python3
# -*-coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen 
import pandas as pd

#empty lists to store the elements
jobtitle= []
companyname= []
joblocation= []
html=urlopen("https://www.indeed.com/jobs?q=data+science+entry+level&l=College+Park%2C+MD")

bs=BeautifulSoup(html,'html.parser')
result_containers = bs.find_all('div', {'class':{'job_seen_beacon'}})

for container in result_containers:
    #job title 
    jt=container.find_all('h2',{'class':{'jobTitle-color-purple'}})    
    #iterating through the job title list     
    for j in jt:        
        jobtitle.append(j.text)    
        
    #company name    
    cn=container.find_all('span',{'class':{'companyName'}})    
    #iterating through the company list    
    for n in cn:        
        companyname.append(n.text)  

    #job location     
    jl=container.find_all('div',{'class':{'companyLocation'}})    
    #iterating through the job location list in div    
    for l in jl:        
        joblocation.append(l.text)   

#Converting the list object to pandas format as each list has a different length
l1=pd.Series(jobtitle,name="Job Title")
l2=pd.Series(companyname,name="Company")
l3=pd.Series(joblocation,name="Job Location")

#concatenating all the lists into a dataframe
ex1_data=pd.concat([l1,l2,l3],axis=1)
print(ex1_data)

#ex1_data.to_csv("/Users/Pang/Downloads/ex1_data.csv")