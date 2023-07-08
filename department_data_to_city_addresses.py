import polars as pl
import pathlib
import sys

from modules.street_names_replacements_before_unique import (
    street_names_replacements_before_unique,
)
from modules.street_names_replacements_after_sort import street_names_replacements_after_sort

department_postal_code = sys.argv[1]
city_postal_code = sys.argv[2]

temp_df = (
    pl.scan_csv("input/" + department_postal_code + "-addresses.csv", separator=";")
    .drop(
        [
            "id",
            "id_fantoir",
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

# Fixing street names issues
for key in street_names_replacements_before_unique:
    temp_df = temp_df.with_columns(
        pl.col("nom_voie").str.replace(
            key, street_names_replacements_before_unique[key]
        )
    )

temp_df = temp_df.with_columns(
    pl.concat_str(
        [
            pl.col("numero"),
            pl.col("rep").fill_null(""),
        ],
        separator=" ",
    ).alias("numerorep")
)

temp_df = temp_df.with_columns(pl.col("numerorep").str.strip())

temp_df = temp_df.with_columns(
    pl.concat_str(
        [
            pl.col("numerorep"),
            pl.col("nom_voie"),
        ],
        separator=" ",
    ).alias("address")
)

for key in street_names_replacements_after_sort:
    temp_df = temp_df.with_columns(
        pl.col("address").str.replace(
            key, street_names_replacements_after_sort[key]
        )
    )

temp_df = temp_df.sort([
    "nom_voie",
    "numero"
])

temp_df = temp_df.drop([
    "numero",
    "rep",
    "nom_voie",
    "numerorep"
])

result_df = temp_df.collect()

path: pathlib.Path = "output/" + city_postal_code + "-addresses.csv"

result_df.write_csv(path, separator=";")
