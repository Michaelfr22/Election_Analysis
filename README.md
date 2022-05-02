# Election_Analysis

## Overview of the Election Audit

  The purpose of this Election Audit is to build a deeper understanding of the Election Results data. At first glance, the reader sees 300,000+ rows of data; meaning there were 300,000+ votes casted in this election. To eliminate the smoke surrounding the data, I constructed a program (Election Analysis) that reads the Election Results file and builds a list for the Counties and Candidate nominees represented by the voters, respectively. The output of the Election Analysis displayed the distribution of votes that fell into the different County (Jefferson, Denver, Arapahoe) and Candidate (Stockham, Degette, Doane) buckets.

## Election-Audit Results
### How many total votes?
  
  There were 369,712 votes casted in this election.

### Breakdown of county vote distribution

  The 369,712 votes were distributed between the three counties as such:
    1. Jefferson - 10.5% - 38,855 votes
    2. Denver - 82.8% - 306,055 votes
    3. Arapahoe - 6.7% - 24,801 votes

### Which County had largest number of votes?

  Denver County had the biggest voter turnout, representing 82.8% of the vote pool.

### Breakdown of candidate vote distribution

  The 369,712 votes were distributed between the three candidates as such:
    1. Charles Casper Stockham - 23.0% - 85,213 votes
    2. Diana DeGette - 73.8% - 272,892 votes
    3. Raymon Anthony Doane - 3.2% - 11,609 votes

### Who won the election?

  Diana DeGette received the most votes between the three candidates to win the election by over 50% (195,000+ votes)! of second place!

## Election-Audit Summary

  In order for the script provided in the Election Analysis to be used in future elections, the guidelines below must be followed:
    1. File to Load - Remember to update the new csv file to that election's data file to be used for analysis
    2. Headers - Ensure that the second and third columns in the new csv file are the County and Candidate data, respectively.
    3. Data Cleaning - The new csv file must be with acceptable County / Candidate responses AND without multiple ID's (duplicate voters)
