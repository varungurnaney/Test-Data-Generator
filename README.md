# Test Data Generator 


### Install 

1. Clone to repo - `git clone https://github.com/varungurnaney/Test-Data-Generator.git` 
2. Install dependecies - `pip3 install -r requirements.txt`

### Usage

1. `python3 app.py -c [:count of records required] -k [:API key]`
2. `python3 app.py -c [:count of records required] --no-api`

_Note: We would always return atleast 50 records even if the count specified is below 50_

### Example

1. `python3 app.py -c 150 -k [:API key]`  - This would return 150 records and fetch data from [Mockaroo](https://www.mockaroo.com)

2. `python3 app.py -c 100 --no-api` - This would generate random 100 entries 
