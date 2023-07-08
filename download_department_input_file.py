import sys
import subprocess


department_postal_code = sys.argv[1]

subprocess.Popen(
    "curl "
    + "-s "
    + "-L "
    + "https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-"
    + department_postal_code 
    + ".csv.gz "
    + "| gzip -d > input/" + department_postal_code + "-addresses.csv"
    , shell=True
)

