# swiss-car-types

*open data as it should be*



## generate the files

```
git clone https://github.com/blemli/swiss-car-types
cd swiss-car-types
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python update.py
```



## github action

it would be cool if we could run this as a github action. However, github doesn't allow files larger than 100MB

~~This github action parses the `IVZ 1330-Bestaende_nach_Typen/` Excel-Sheets of the swiss government into a machine readable format (json and csv).~~

~~The action runs every night at 02:00 UTC.~~

