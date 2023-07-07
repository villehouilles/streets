import polars as pl
import pathlib
import sys

from street_names_replacements_before_unique import (
    street_names_replacements_before_unique,
)
from street_names_replacements_after_sort import street_names_replacements_after_sort

department_postal_code = sys.argv[1]
city_postal_code = sys.argv[2]

temp_df = (
    pl.scan_csv("adresses-" + department_postal_code + ".csv", separator=";")
    .drop(
        [
            "id",
            "id_fantoir",
            "numero",
            "rep",
            "code_postal",
            "code_insee",
            "nom_commune",
            "code_insee_ancienne_commune",
            "nom_ancienne_commune",
            "x",
            "y",
            "lon",
            "lat",
            "type_position",
            "alias",
            "nom_ld",
            "libelle_acheminement",
            "nom_afnor",
            "source_position",
            "source_nom_voie",
            "certification_commune",
            "cad_parcelles",
        ]
    )
    .filter(pl.col(["code_postal"]) == int(city_postal_code))
)

for key in street_names_replacements_before_unique:
    temp_df = temp_df.with_columns(
        pl.col("nom_voie").str.replace(
            key, street_names_replacements_before_unique[key]
        )
    )

temp_df = temp_df.unique().rename({"nom_voie": "street_name"}).sort("street_name")

for key in street_names_replacements_after_sort:
    temp_df = temp_df.with_columns(
        pl.col("street_name").str.replace(
            key, street_names_replacements_after_sort[key]
        )
    )


result_df = temp_df.collect()

path: pathlib.Path = "streets-" + city_postal_code + ".csv"

result_df.write_csv(path, separator=";")
