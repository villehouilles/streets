# Houilles' streets

Get the latest data from the Yvelines department.  
https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-78.csv.gz

**Install the project**  
```bash
poetry install
```

**Run the script**  
```bash
python department_data_to_city_streets.py <department_postal_code> <city_postal_code>  
```
Example: 
```bash
python department_data_to_city_streets.py 78 78800  
```
