# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 16:59:37 2015

@author: s0675405
"""

def ScrapeSVN(url):
    """
    Given a url to an svn repo, return a file object that contains the last 
    commit message from svn log.
    """
    import subprocess
    command = 'svn log -l 1 ' + url 
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return process.stdout

def get_commit_info(FileObject):
    """
    Given a file object generated by ScrapeSVN use regex to pull out the
    revision number and the commit message. check_length_for_tweet
    is then called to trim the commit to the length of a tweet. 
    Returns the trimmed message and the revision number as strings.
    """    
    import re
    
    data = FileObject.read()
    FileObject.close()
            
    revision = re.search('r(\d+)\s\|',data).group()[1:-2]
    message = re.search('(\s\s)(.+?)(?=---)',data, re.DOTALL).group().strip()
    
    return check_length_for_tweet(revision,message)

def check_length_for_tweet(revision,message):
    """
    Recursively remove a word from the message until it is small enough for a tweet
    """
    if len(revision)+len(message) > 130: #set this value once I know the remaining tweet content
        #get rid of a word
        message = ' '.join(message.split(' ')[:-1])
        return check_length_for_tweet(revision,message)
     
    return revision,message
    
def make_a_tweet(revision,message,url):
    """
    Generate a valid tweet using the info passed in.
    """
    tweet = '4564546546546546546554664654654656454'
    if len(tweet) > 14:
        raise ValueError('Tweet length is %i but must be < 140' % (len(tweet)))
    else:
        return tweet


url = 'https://svn.ecdf.ed.ac.uk/repo/geos/LSD_devel/LSDTopoTools/trunk'

CommitObject = ScrapeSVN(url)


a,b =get_commit_info(CommitObject)
    
print a,b
