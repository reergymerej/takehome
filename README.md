# Takehome

As specified in [Data Enginner Take Home](https://parkerholcomb.notion.site/ML-Data-Engineer-Take-Home-23bb2561fbdc4b48bfe3b9de5b9c674e), this will extract records from multiple .parquet files, transform the records into valid FHIR Patient instances, and write the results to a directory as individual JSON files.

## Installation

```bash
# TBD
```

## Usage

```bash
# read/write here
python takehome

# specify different input/output locations
python takehome dir_with_member_parquets/ output_dir/
```

## Tests

```bash
make ci
```