from pyflowchart import Flowchart
with open('def_probGauss.py') as f:
	code = f.read()
 
fc = Flowchart.from_code(code)
print(fc.flowchart())

#input the output expression onto http://flowchart.js.org/
#https://pypi.org/project/pyflowchart/