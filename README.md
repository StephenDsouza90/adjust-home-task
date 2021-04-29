# Adjust-Home-Task
This repository contains the implementation of the Adjust home task. It is written in Python and Django.

## Virtual environment

To setup the virtual environment, run the following command:

```bash
>> python3.6 -m venv venv
```

To activate venv use:

|Platform   |Command                                  |
|-----------|-----------------------------------------|
|iOS        |```$ source venv/bin/activate```         |
|           |```$ . venv/bin/activate.fish```         |
|Windows    |```C:\> venv\Scripts\activate.bat```     |
|           |```PS C:\> venv\Scripts\Activate.ps1```  |


To deactivate the virtual environment, run the following command:

```bash
>> deactivate
```

## How to run locally

To install the requirements, run the following command:

```bash
>> pip install -r requirements.txt
```

To start the server, run the following command:

```bash
>> python adjust_app/manage.py runserver
```

## Database migration

```bash
>> python adjust_app/manage.py makemigrations

>> python adjust_app/manage.py migrate
```

## Add data into the database

To add data from the dataset.csv file, run the following in a browser. Please make sure that the dataset.csv file is saved in teh raw_data folder path if it is not there.

```bash
>> http://127.0.0.1:8000/add-performace-metrics-data
```

## Routes

### Route structure

```bash
/perf-data?q=f1:val1,f2:val2,f3.gt:2021-01-02,f3.lte:2021-02-02&fields=f1,f2,f3&group_by=f1,f2&sort_by=f1,f2:desc

/perf-data?q=f1:val1,f2:val2,f3[.gt|.gte|.lt|.lte]:2021-01-02,f3.lte:2021-02-02&fields=f1,f2,f3&group_by=f1,f2&sort_by=f1,f2[:asc|:desc]
```

where f1, f2, ..., fn are field names you want to query.

v1, v2, ..., vn will be the values corresponding to the above fields.

.gte stands for greater then and equal to

.gt stands for greater than

.lte stands for less than and equals to

.lt stands for less than

If a column is mentioned in the group_by, it will also be included as part of the fields to understand the values corresponding to the group.

:asc stands for ascending order

:desc stands for descending order

:2021-01-02 stands for year-month-day
## Tasks and Results

The URLs can be executed in a browser:

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.

```bash
http://127.0.0.1:8000/get-data?q=date.lt:2017-06-01&fields=impressions,clicks&group_by=channel,country&sort_by=clicks:desc
```

<details>
<summary>JSON</summary>

```json
[
    {
        "impressions": 498861,
        "clicks": 12277,
        "channel": "adcolony",
        "country": "US"
    },
    {
        "impressions": 347554,
        "clicks": 10738,
        "channel": "apple_search_ads",
        "country": "US"
    },
    {
        "impressions": 249197,
        "clicks": 8831,
        "channel": "vungle",
        "country": "GB"
    },
    {
        "impressions": 249618,
        "clicks": 7440,
        "channel": "vungle",
        "country": "US"
    },
    {
        "impressions": 201584,
        "clicks": 6888,
        "channel": "unityads",
        "country": "US"
    },
    {
        "impressions": 198077,
        "clicks": 5884,
        "channel": "google",
        "country": "US"
    },
    {
        "impressions": 200901,
        "clicks": 5851,
        "channel": "facebook",
        "country": "DE"
    },
    {
        "impressions": 149110,
        "clicks": 4437,
        "channel": "chartboost",
        "country": "US"
    },
    {
        "impressions": 148999,
        "clicks": 4357,
        "channel": "unityads",
        "country": "GB"
    },
    {
        "impressions": 99655,
        "clicks": 3919,
        "channel": "chartboost",
        "country": "GB"
    },
    {
        "impressions": 100441,
        "clicks": 3876,
        "channel": "google",
        "country": "GB"
    },
    {
        "impressions": 99892,
        "clicks": 3478,
        "channel": "apple_search_ads",
        "country": "GB"
    },
    {
        "impressions": 98886,
        "clicks": 3402,
        "channel": "unityads",
        "country": "CA"
    },
    {
        "impressions": 99130,
        "clicks": 3342,
        "channel": "facebook",
        "country": "US"
    },
    {
        "impressions": 99532,
        "clicks": 3042,
        "channel": "google",
        "country": "FR"
    },
    {
        "impressions": 100149,
        "clicks": 2962,
        "channel": "chartboost",
        "country": "FR"
    },
    {
        "impressions": 99203,
        "clicks": 2888,
        "channel": "facebook",
        "country": "GB"
    },
    {
        "impressions": 49468,
        "clicks": 1967,
        "channel": "apple_search_ads",
        "country": "DE"
    },
    {
        "impressions": 99431,
        "clicks": 1943,
        "channel": "chartboost",
        "country": "DE"
    },
    {
        "impressions": 50804,
        "clicks": 1541,
        "channel": "unityads",
        "country": "DE"
    },
    {
        "impressions": 49803,
        "clicks": 1480,
        "channel": "facebook",
        "country": "FR"
    },
    {
        "impressions": 49316,
        "clicks": 1477,
        "channel": "chartboost",
        "country": "CA"
    },
    {
        "impressions": 49780,
        "clicks": 1459,
        "channel": "google",
        "country": "CA"
    },
    {
        "impressions": 49974,
        "clicks": 1441,
        "channel": "facebook",
        "country": "CA"
    },
    {
        "impressions": 47202,
        "clicks": 476,
        "channel": "google",
        "country": "DE"
    }
]
```

</details>

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

```bash
http://127.0.0.1:8000/get-data?q=date.gte:2017-05-01,date.lte:2017-05-31,operating_system:ios&fields=installs&group_by=date&sort_by=date
```

<details>
<summary>JSON</summary>

```json
[
    {
        "installs": 755,
        "date": "2017-05-17"
    },
    {
        "installs": 765,
        "date": "2017-05-18"
    },
    {
        "installs": 745,
        "date": "2017-05-19"
    },
    {
        "installs": 816,
        "date": "2017-05-20"
    },
    {
        "installs": 751,
        "date": "2017-05-21"
    },
    {
        "installs": 781,
        "date": "2017-05-22"
    },
    {
        "installs": 813,
        "date": "2017-05-23"
    },
    {
        "installs": 789,
        "date": "2017-05-24"
    },
    {
        "installs": 875,
        "date": "2017-05-25"
    },
    {
        "installs": 725,
        "date": "2017-05-26"
    },
    {
        "installs": 712,
        "date": "2017-05-27"
    },
    {
        "installs": 664,
        "date": "2017-05-28"
    },
    {
        "installs": 752,
        "date": "2017-05-29"
    },
    {
        "installs": 762,
        "date": "2017-05-30"
    },
    {
        "installs": 685,
        "date": "2017-05-31"
    }
]
```

</details>

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

```bash
http://127.0.0.1:8000/get-data?q=date:2017-06-01,country:US&fields=revenue&group_by=operating_system&sort_by=revenue:desc
```

<details>
<summary>JSON</summary>

```json
[
    {
        "revenue": 1205.21,
        "operating_system": "android"
    },
    {
        "revenue": 398.87,
        "operating_system": "ios"
    }
]
```

</details>


4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.

```bash
http://127.0.0.1:8000/get-data?q=country:CA&fields=cpi,spend&group_by=channel&sort_by=cpi:desc
```
<details>
<summary>JSON</summary>

```json
[
    {
        "cpi": 2.07,
        "spend": 1164,
        "channel": "facebook"
    },
    {
        "cpi": 2,
        "spend": 1274,
        "channel": "chartboost"
    },
    {
        "cpi": 2,
        "spend": 2642,
        "channel": "unityads"
    },
    {
        "cpi": 1.74,
        "spend": 999.9,
        "channel": "google"
    }
]
```
</details>

## Test Cases

To run the test cases, run the following command:

```bash
>> python adjust_app/manage.py test adjust_app
```

## Note:
Users of VS code can start the server or run the test cases from the Run and Debug console under the drop down of their respective names.