import pydot # 
import sys
from time import gmtime, strftime

def createGraph(cdpFile):  
    graph = pydot.Dot(graph_type='graph')
    file = open(cdpFile,"r")
    file_r = file.read()
    file.close()
    
    file_r=file_r.split('\n')
    file_f = []
    for i in file_r:
        file_f.append(i.split(",")) 
    del file_f[0]
    edgeList = []
    for i in file_f:
        if len(i) > 1:
            if [i[1],i[3]] not in edgeList:
                if [i[3],i[1]] not in edgeList:
                    edgeList.append( [i[1],i[3]] )  
    for i in edgeList:
        if len(i) > 1:        
            graph.add_edge(pydot.Edge(i[0],i[1]))
    currentTime = strftime("%a %d %b %Y %X", gmtime())
    currentTime = currentTime.replace(" ", "_")
    graph.write_png('Cdp_Graph_' + currentTime + '.png') 
    print "Graph made!!!"
       
def main():
    try:
        cdpFile = sys.argv[1]
        createGraph(cdpFile)
    except:
        print "Something went wrong, your csv file is probably messed up, or you spelled it wrong."
    
if __name__ == "__main__":
    main()