# swiss-car-types

*open data as it should be*



This github action parses the `IVZ 1330-Bestaende_nach_Typen/` Excel-Sheets of the swiss government into a machine readable format (json and csv).

The action runs every night at 02:00 UTC.

run manually:

```
git clone https://github.com/blemli/swiss-car-types
cd swiss-car-types
uv venv 
pip install -r requirements.txt
python update.py
```

