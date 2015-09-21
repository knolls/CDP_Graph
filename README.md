# CDP_Graph

This takes in a CDP Crawl file and will out a graph as a png file. There are 2 examples files. ExampleFile.csv is what a the cdp crawl file should look like, and Cdp_Graph_Mon_21_Sep_2015_21:19:18.png is what the output of the ExampleFile.csv would look like.

## To Run
python cdpGraph.py CdpCrawlFile.csv

### Dependencies
The only dependency pyDot if you dont have it:
    `sudo apt-get install pydot`

### Notes
Makes sure that all the hostnames in the CDP Crawl have the domain names removed. 
Also makes sure that hostnames for the same device match up with themself and examples of this is:
switch-1.domain.com and switch-1, same switch but the one has a domain name attached. Make sure to fix this.
