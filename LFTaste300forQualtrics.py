#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:55:04 2019

@author: Ava
"""

##modified old cr_sample script to highlight random sample of long-form texts so that they can be pulled into Qualtrics to be coded.

# --- import required modules 
#need to import a newer version in order to do precision & recall division at the end (it thinks handcoded is text)
from __future__ import division
#from collections import defaultdict

#import sys
#import requests
import os #file directory stuff
#import csv
import re
import pandas as pd
#import numpy as np
#import json
#import codecs 

def highlight_rev(text, feats):
    
#    given a text and a set of compiled regex features
#    highlight all hits 
    
    pre = '<span style="background-color: #FFFF00"><b>'
    post = '</b></span>' 

#finds the length of the word and only changes the pre and post - doesn't change the case of the word
    text = text.replace(feats, '%s\\1%s' % (pre, post), regex=True)

    return text

def rm_spaces(texts):
    '''
    Remove extra spaces/carriage returns
    texts = slice of df containing texts
    '''
    print('\n#### CLEANING TEXT by removing extra blank characters')
    
    #replace with a single space ' '
    returns = '[\n\r\t]'
    spaces = '\s{2,}'    
    space = [returns, spaces]
    
    #replacing with a single space ' '
    for s in space:
        texts = texts.str.replace(s,' ')

    return texts

def rm_dupes(df, s, fname):
    '''
    Remove duplicates, save them in a separate file html highlight coding and extra spaces/carriage returns
    df = the dataframe to be de-duped
    s = column title on which to de-dupe
    fname = original filename - will be transformed here
    '''
    print('\n#### REMOVING ANY DUPLICATES based on the cleaned text')
 
    #drop duplicate texts (gets most of them)
    docs_dedup = df.drop_duplicates(subset=s)

    #save the duplicates for later checking if there are any
    if docs_dedup.shape[0] < df.shape[0]:
        dupes = pd.concat(g for _, g in df.groupby(s) if len(g) > 1)
        print(dupes.ArticleTitle)
        dupes_filename=fname.replace('.csv','_dupes.csv')
        dupes.to_csv(os.path.join(out_dir, dupes_filename), mode='a', encoding='utf-8')

    return docs_dedup

def file_chk(df, fname):
    '''
    check that files do not have extra spaces or duplicates
    '''
    print('\n#### CHECKING FILE - remove extra spaces and dupes')

    #remove highlights and extra spaces
    df['new_text'] = rm_spaces(df.ArticleContent)
    #print one example to see what changed - I think I need a different index to make this work (they are now indexed by ArticleID)
#    print(df.ArticleContent[0])
#    print('\n',df.new_text[0])

    #remove duplicates if there are any and return de-duplicated texts
    df = rm_dupes(df, 'new_text', fname)
    print('De-duped files:\n', df.shape)

    return df

#############################
#input directory
##in_dir = 'X:/P50 - Youth Tobacco Tracking/5_Papers/ThemeSpecificBeliefOutcomes- ak/Data/'
##mturkin = '3b. LongformEcigMPMTVCSample100.txt'
in_dir = '/Users/Ava/Desktop/describing_data_git/classtest_2/Data'
mturkin = 'LFTaste300IDContent3.txt'


##change this!
out_dir='/Users/Ava/Desktop/describing_data_git/classtest_2/Data'
##change this!
mturkout = 'LFTaste300_formatted_for_Qualtrics2'
script_dir='/Users/Ava/Desktop/describing_data_git/classtest_2/Data'
##latimesf = 'latimes_list.csv'
latimesd = 'latimes_list.csv'

#############################
#############################
os.chdir(out_dir)

#regex to match for highlighting
tm=r'(\b(smoking|tobacco|smokers?|smokes?|nicotine|hookahs?|cigs?|e-?cigs?|vaping|cigars?|cigarettes?|cigarillos?|e-?cigars?|e-?cigarillos?|e-?cigarettes?|chewing|dipping|snus|snuff|smokeless)\b|\b(vape))'

# print original sample data to a .csv file - clearing out extra spaces and line feeds
# could use pandas if qualtrics could handle all those extra new line feeds, but it can't.
sample_df = pd.read_csv(os.path.join(in_dir, mturkin), sep='\t', encoding="ISO-8859-1")
sample_df['new_text'] = sample_df['ArticleContent']
sample_df['new_text'].replace(re.compile(r'\\+'),'',regex=False,inplace=True)
sample_df.new_text= highlight_rev(sample_df.new_text, re.compile(tm,flags=re.I))
sample_df.ArticleTitle = highlight_rev(sample_df.ArticleTitle, re.compile(tm,flags=re.I))

#sample randomizes, so just sample the entire df - then put in set numbers
newsample=sample_df.sample(frac=1)

#assign the sets in the sizes you want (here split into equal chunks of 369)
from itertools import repeat
sets=[]
n=25
for i in range(0,int(len(newsample)/n)):
    sets[i*n:(i+1)*n] = repeat(i,n)
newsample['set']=sets 

#for i in range(0,12):
#    sets[i*n:(i+1)*n] = repeat(i,n)
#sets[300:305]=repeat(11,5)
#newsample['set']=sets 

#print out file for Qualtrics

#this is the maximum number of characters that Qualtrics will accept in a Loop & Merge text field.
#CELL_MAX = 20000
#cols = newsample.new_text.str.len()/CELL_MAX
                          #get the maximum number of columns - not working right now
#looked at it before running the next part.
#maxcols = int(max(cols)+1)
#print(maxcols)
#newcol = ['ArticleContent1','ArticleContent2']
#print df.highlighted.str.len()
#for i in range(0,maxcols):
#   newsample[newcol[i]]= newsample.new_text.str.slice(start=CELL_MAX*i,stop=CELL_MAX*(i+1))    

##drop all text fields in this metadata file. change this to match the number of ArticleContent columns you ended up needing.
metadata = newsample.drop(['ArticleContent','new_text'],1)
metadata.to_csv('metadata.csv', encoding='utf-8', index=False)
##change this to match the number of ArticleContent columns you ended up needing.
newsample=newsample[['ArticleID','set','SourceTitle','ArticleTitle','ArticleContent']]

newsample.to_csv(mturkout + ".csv", encoding='utf-8', index=False)
#newsample.loc[newsample['set']==1].to_csv(mturkout + "set1.csv", encoding='utf-8', index=False)
#newsample.loc[newsample['set']==2].to_csv(mturkout + "set2.csv", encoding='utf-8', index=False)
#newsample.loc[newsample['set']==3].to_csv(mturkout + "set3.csv", encoding='utf-8', index=False)





