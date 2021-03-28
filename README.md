# Election Analysis

----

### Overview of Election Audit

A Colorado Elections Board employee called Tom has requested for an audit on a Colorado congressional precinct to report on the election results. The reporting and audit is usually done in Excel. However, Tom would like to know if the tabulation can be automated. This audit will explore whether the reporting process can be automated and applied accross other elections in the future.


### Election-Audit Results:

*Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.*

*How many votes were cast in this congressional election?
Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
Which county had the largest number of votes?
Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Which candidate won the election, what was their vote count, and what was their percentage of the total votes?*

After running the election analysis audit, the results below are as follows (or refer to screenshot image below):

*  A total of 369,11 votes were cast in this congressional election. To calculate the total number of votes casted, a *for* loop was used to iterate through each             row of the CSV file containing the election data and then incremented and stored in the *total_votes* variable. The *total_votes* variable is initialised to 0 before the *for* loop begins.
*  Votes by county:
    * Jeffersson County accounted for 10.5% votes (38,855)
    * Denver County accounted for 82.8% votes (306,055)
    * Arapahoe County accounted for 6.7% votes (24,801)
* Denver County had the largest number of votes accounting for 82% of total votes.

* Number of votes each candidate received:  
    * Charles Casper Stockham received 23.0% of the vote (85,213)
    * Diana DeGette received 73.8% of the vote (272,892)
    * Raymon Anthony Doane received 3.1% of the vote (11,606)
* Candidate Diana DeGette won the election. She received the highest number of votes **272,892** and accounted for 73.8% of the votes.



![screenshot terminal output](https://github.com/YanLuong/Election_Analysis/blob/main/Resources/Terminal%20Output%20Of%20Results.png)


### Election-Audit Summary: 

*In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. 
Give at least two examples of how this script can be modified to be used for other elections.
