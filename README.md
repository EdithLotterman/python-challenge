# python-challenge

Background: This assignment was to create two scripts in Python, one analyzing banking data, and the other analyzing election data.

##PyBank

The assignment was to read in the csv file in the Resources and then prepare an analysis showing:

|Total Months| shows total number of months in analysis
|Total Profit and Loss| Cumulative total of the indivdual month's profit or loss
|Average Change in Profit and Loss|The average of the change in profit/loss month over month
|Greatest Increase in Profits|Returns the month and amount of the greatest increase in month-over-month profits and/or losses
|Greatest Decrease in Profits|Returns the month and amount of the greatest decrease in month-over-month profits and/or losses 

This analysis should print in the terminal and to a csv file in the Analysis folder.

The objective was accomplished by looping through each row, and storing variables in lists for the month, profit_loss, cumulative profits_losses, and the monthly change.
Calculations were performed in order to store some variables. The month over month increase(decrease) in profits were stored in a dictionary in order to retrieve max 
and min amounts.

###PyPoll

The assignment was to read in the csv file in the Resources and then prepare an analysis showing:

|Header| Text Election Results
|Total Number of Ballots|The numbers of ballots cast
|Candidate 1 Name|Candidate 1 % of Total Ballots|Candidate 1 Total Ballots|A line for each candidate showing their name, what percent of the total vote they received,
|Candidate n Name|CAndidate n % of Total Ballots|Candidate n Total Ballots|and the total number of votes received
|Winner| The name of the person who received the most ballots

This analysis should print in the terminal and to a csv file in the Analysis folder.

The objective was accomplished by looping through the csv file and writing every candidate name to a new list. The length of that list is equal to the total number 
of votes cast. The counter from the collections module was brought in, which stored the unique names and the number of times they occured in a dictionary as key and values,
respectively. The percent of the total vote was calculated by looping through the values, and dividing by the total votes cast.

Two zipped lists were created because I couldn't find a way to loop through and print the rows for both the terminal and csv with one list.

Candidate votes and names were stored in a new dictionary to retrieve the max numbers of votes received and return the name.   