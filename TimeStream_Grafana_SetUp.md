Follow this link to set up Grafana cloud https://grafana.com/

## Table of Content

- [Create Rule In AWS IoT Core](#create-rule-in-aws-iot-core)
- [Create The TimeStream Database](#create-the-timestream-database)
- [Create a Table In The TimeStream Database](#create-a-table-in-the-timestream-database)
- [Finishing With the Rule](#finishing-with-the-rule)
- [Creating New User For Acessing the Timestream Database Through Graphana](#creating-new-user-for-acessing-the-timestream-database-through-graphana)
- [Connecting Graphana to Timestream Database](#connecting-graphana-to-timestream-database)
- [Representing the Data](#representing-the-data)




## Create Rule In AWS IoT Core

If you have followed the official tutorial by AWS on how to set up IoT Core with python the exact same steps as shown in the pictures can be followed.

![TimeStream_Graphana_1](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_1.jpg)

![TimeStream_Graphana_2](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_2.jpg)

![TimeStream_Graphana_3](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_3.jpg)


## Create The TimeStream Database

![TimeStream_Graphana_4](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_4.jpg)

![TimeStream_Graphana_5](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_5.jpg)

## Create a Table In The TimeStream Database

![TimeStream_Graphana_6](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_6.jpg)

![TimeStream_Graphana_7](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_7.jpg)

## Finishing With the Rule
![TimeStream_Graphana_8](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_8.jpg)

![TimeStream_Graphana_9](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_9.jpg)

## Creating New User For Acessing the Timestream Database Through Graphana

![TimeStream_Graphana_10](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_10.jpg)

![TimeStream_Graphana_11]([images\TimeStream_Graphana_11.png](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_11.jpg))

![TimeStream_Graphana_12](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_12.jpg)

![TimeStream_Graphana_13](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_13.jpg)


The Credinentials as shown in the below pictrure will be used to in Graphana to establish a connection with the TimeStream Database

![TimeStream_Graphana_14](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_14.jpg)

## Connecting Graphana to Timestream Database

![TimeStream_Graphana_15](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_15.jpg)

![TimeStream_Graphana_16](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_16.jpg)

![TimeStream_Graphana_17](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_17.jpg)

![TimeStream_Graphana_18](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_18.jpg)

## Representing the Data

Create a time series dash board and add the following queries

![TimeStream_Graphana_19](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_19.png)

![TimeStream_Graphana_20](https://github.com/M-Gkiko/ESP32_AWS_Weatherstation/blob/d7fc25878c6e38161db975ba503bfdc00bdd586f/images/TimeStream_Graphana_20.png)

```sql

SELECT CREATE_TIME_SERIES(time,measure_value::bigint) as humidity FROM "timestream8"."weatherData" where time BETWEEN from_milliseconds(1660398638031) AND from_milliseconds(1660400138031) and measure_name = 'humidity'
```
```sql

SELECT CREATE_TIME_SERIES(time,measure_value::bigint) as temperature
FROM "timestream8"."weatherData" where time BETWEEN from_milliseconds(1660398638031) AND from_milliseconds(1660400138031) and measure_name = 'temperature' 
 ```
