# Election-Analysis
Practice with Python

## Overview of Election Audit: 
I was hired to help Tom, an official with the Colorado Board of Elections (CBE), with an audit of a recent congressional election. I had to write code using Python that would tabulate the votes for each candidate, calculate the percentage of the votes that each had one and to declare a winner. It also listed the three counties in the district, counted their votes, and calculated the percentage of the total vote that came from each county.

Along with the calculations, I created a script that would automatically transfer the data to a readable text document, which would update results of the count and publish them.

Previously, election data had been collected and analyzed using Excel. With Python we will be able to create code that will process huge amounts of data effeciently and reliably--one which we will be able to adapt for future CBE tallies, both large and small.

## Election-Audit Results: 

- How many votes were cast in this congressional election?
  - I counted the votes in the election by setting up a variable called _total votes_. Using a _for-loop_, I added votes for each candidate, and for each county to track the sources of each votes (should an audit be called for, the number of votes in each county would be compared to the number of registered voters).
  - Here is my for-loop: `for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]`
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Within the for-loop described above, I used an if-clause to identify the unique counties in the district, using the .append method. I coded it so that whenever a new county was found in the list, the votes would be added to its total.
  - `if county_name not in county_list: 
       county_list.append(county_name)
       county_votes[county_name] = 0
     county_votes[county_name] +=1`
  - I found the percentage of the votes from each county using a new variable, _county_vopc_, and dividing the county votes by the total votes: `county_vopc = float(votes) / float(total_votes) * 100`
  - The county votes broke down as
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- Which county had the largest number of votes?
  - I found the county with the largest number of votes by creating the _votes_ variable and making it equal to `county_votes[county_name]`
  - Then I created a _for-loop_ to add up the _votes_ of each county and the percentage of total votes (_county_vopc_)
  - An _if-clause_ will help me to identify the top county: 
  - `if votes > votes_lgturnout:
            votes_lgturnout = votes
            county_lgturnout = county_name`
  - Denver had the largest county turnout with 306,055 votes, 82.8% of the total
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana Degette won the election
  - Her winning vote count was 272,892
  - She received 73.8% of the vote

## Election-Audit Summary: 
Setting up this program in Python means that we can import any amount of data that is in csv format (comma-separated values). This means that the CBE could use it for any race, from local to statewide with few amendments.

The first area where the code would be altered for future counts would be in the file that was imported. Python has two dependencies that we can import to help import the data: _csv_ and _os_. Currently the line of code reads `file_to_load = os.path.join("Resources", "election_results.csv")`  The path which os joins to the program comes from the "Resouces" folder and is titled "election_results.csv". We would need to simply change the path to the folder containing the new data and identify the new file to import election results.

The code could also be adapted to record and tabulate results from local precincts, to counties (the current view), to congressional districts or regions (larger views). This would involve creating new variables in the for-loop to tabulate the votes in each region. In the code, 
    `for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]`
        
The _candidate_name_ would stay the same in the adapted code, but _county_name_ would be replaced with the jurisdiction voting.

The code that we have developed is a framework. From it we can build a structure to tabulate election data from a variety of sources. From this framework we can build a system for election reporting and analysis that will serve the CBE for many years to come.
