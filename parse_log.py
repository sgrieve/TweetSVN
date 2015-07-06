# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 16:59:37 2015

@author: s0675405
"""

def get_commit_info(filename):
    
    import re

    with open(filename,'r') as f:
        data = f.read()
            
    revision = re.search('r(\d+)\s\|',data).group()[1:-2]
    
    message = re.search('(\s\s)(.+?)(?=---)',data, re.DOTALL).group().strip()
    
    return check_length_for_tweet(revision,message)

def check_length_for_tweet(revision,message):
    
    if len(revision)+len(message) > 130: #set this value once I know the remaining tweet content
        #get rid of a word
        message = ' '.join(message.split(' ')[:-1])
        #print message
        return check_length_for_tweet(revision,message)
     
    return revision,message
    

def make_a_tweet(revision,message,url):
    tweet = '4564546546546546546554664654654656454'
    if len(tweet) > 14:
        raise ValueError('Tweet length is %i but must be < 140' % (len(tweet)))
    else:
        return tweet


make_a_tweet(1,1,1)

a,b =get_commit_info('test.txt')
    
print a,b



