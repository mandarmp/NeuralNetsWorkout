# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 02:58:24 2019

@author: mandar
"""
#trying to implement the OR gate
import tensorflow as tf
import numpy as np

def ORact(x):
    if(x>=1) :
        return 1
    else:
        return 0

def firstnn(input1_,input2_) :
    x=np.array([[input1_,input2_]])
    w=np.array([[1.0],[1.0]])
   
    mat1=tf.constant(x)
    mat2=tf.constant(w)
    #mat1=tf.placeholder(tf.float32,)
    #mat2=tf.placeholder(tf.float32,[weight1,weight2])
    multi=tf.matmul(mat1,mat2)
    with tf.Session() as sess:
        result=sess.run(multi)
        
    return(ORact(result))

if __name__=="__main__":
    
    if(firstnn(1.0,0.0)):
        print('true')
    else:
        print('false')
    
    
    

    
    
    
    
    
    
    
    
    