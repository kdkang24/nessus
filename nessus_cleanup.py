import sys
import pandas

scan = str(sys.argv[1])
print("Cleaning up file: " + scan)

data = pandas.read_csv(scan)

#strip whitespace from column headers
data.rename(columns=lambda x: x.strip(), inplace=True)
data = data.rename(columns=lambda x: x.strip())

#keep only relevant columns
keep_columns = ['CVE', 'Risk', 'Name', 'IP Address', 'FQDN', 'NetBios']
new_data = data[keep_columns]

#keep only Critical and High severity vulns
severity = ['Critical', 'High']
filtered = new_data[new_data.Risk.isin(severity)]
filtered.to_csv(str("CLEAN_" + scan), index=False)

