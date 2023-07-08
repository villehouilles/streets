# Houilles' streets and addresses

Last update (8th July 2023)

## Folders

| input | output | modules |
| ------------- | ------------- | ------------- |
| department files | Streets names and addresses of Houilles | python subscripts |

## How to use this project

**Get the latest data from the Yvelines department:**
```bash 
python download_department_input_file.py 78
```

**Install the project**  
```bash
poetry install
```

**Run the script for streets' names**  
```bash
python department_data_to_city_streets_names.py <department_postal_code> <city_postal_code>  
```
Example: 
```bash
python department_data_to_city_streets.py 78 78800  
```

**Run the script for addresses**  
```bash
python department_data_to_city_addresses.py <department_postal_code> <city_postal_code>  
```
Example: 
```bash
python department_data_to_city_addresses.py 78 78800  
```