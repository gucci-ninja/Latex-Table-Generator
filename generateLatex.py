def generateLatex(userinput):
    # 
    numcells = ""
    cellcontent = ""
   
    # Check for valid input

    # Separate input
    rows = userinput.split("\n")

    # Find number of columns
    for i in len(rows[0].count('x')):
        numcells += 
    for i in rows:
        cells = rows.split("|")
        
        
        
    latex = "\\begin{tabular}{"+numcells+"}\n"+cellcontent+"\\end{tabular}"

    return latex
    
