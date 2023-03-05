# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:11:44 2023


"""

from operator import itemgetter 
from itertools import chain 
import pandas as pd
import matplotlib.pyplot as plot
import networkx as nx
import operator
import collections
from heapq import nlargest
from collections import defaultdict




def read_file(fname):
    '''
    This is a generic function with one argument to read a file 
    the name and type is passed as an argument while calling this function
    Parameter : fname is the name of the file
    variable1 data: file is saved in this variable
    variable 2 pd: panda variable
    variable 3 df: dataframe to store file
    data.plot():
    then that data is plotted just to check in the same function which shall be a line plot for most cases 
    the function returns a dataframe to be used for further visualisation
    '''
    
    data=pd.read_csv(fname)
    df = pd.DataFrame(data);
    data.plot()
    return df
    






#https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
def line_plot(fname,title): 
    '''
    A generic function for line plot of any data
    dataframe.
    readfile reads the csv file
    plot function is used to plot different graphs, here 
    .line function is used to plot a line with argument tile of the graph
    ''' 
    df=pd.DataFrame(read_file(fname))
    
    df.plot.line(title)






#barchart of Grades of students
#https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
#small dataset
def plot_specific_coloumns():
    '''
   the function is called to read the file named as grades type csv
   the second function df.plot.line is used to plot a line graph using the specific coloumn at index 2
   as the first argument and second is the title of graph
   a bar graph is also made for comparison using first coloumn x[0], and kind bar
    ''' 
    df= read_file('grades.csv')
    df.plot.line(x=df.index[2],title="Grades of students")
    df.plot(x=df.index[0], kind='bar', stacked=True,title='Grades of students')






#https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
#pie of alphabets frequency
def pie_plot():
    '''
    the function is called to read the file named as letter_frequency type csv
    the second function df.plot.pie is used to plot a pie graph using the specific coloumn
    at index 2 as the first argument 
    second is the size of the chart, third for percentage and last for title
    a bar graph is also made for comparison using first coloumn x[0], and kind bar
    ''' 
    df=read_file('letter_frequency.csv')
    plot = df.plot.pie(y=df.index[2], figsize=(10, 10), autopct='%1.2f%%',title="alphabets frequency")

#barchart of joe biden's unpopularity among rep and dem
#https://projects.fivethirtyeight.com/biden-approval-rating/
#https://projects.fivethirtyeight.com/polls/data/generic_ballot_polls.csv

def bar_plot():
    '''
    the function  reads specific coloumns of the file named as joe type csv i.e. 2,5,36,37
    variable 1 data2: to save file after reading it
    variable 2 df:data2 is then saved in the dataframe variable df
    data is plotted as line by df.plot()
    the function df.plot.pie is used to plot bar graph using the specific coloumn
    at index 0 as the first argument 
    second is the kind of the chart,  and last is the title
    ''' 
    data2 = pd.read_csv('joe.csv', usecols= [2,5,36,37])
    df = pd.DataFrame(data2);
    df.plot()
    df.plot(x=df.index[0], kind='bar', stacked=True,
    title='Stacked Bar Graph of joe biden unpopularity')
  

'''
   the function is called to read the file named as trees type csv
   title is passed in arguments while calling the second function line_plot 
   to plot the line of respective file
  
   the function is called to plot line of the file named as trees type csv
   title is passed in arguments 
    '''
df1=read_file('trees.csv')
df1.plot.line(title="Relation of tree height, volume and girth")

'''
   the function line_plot is called to read the file named as trees type csv
   title is passed in arguments 
    ''' 
#line_plot('trees.csv',title="Relation of tree height, volume and girth")
    
'''
   the function is called to plot bar and line of specific coloumns
  
    ''' 
plot_specific_coloumns()
'''
   the function is called to plot pie and line of specific coloumns
  
    ''' 
pie_plot()
'''
   the function is called to plot bar of specifically read coloumns from a sheet
  
    ''' 
bar_plot()
