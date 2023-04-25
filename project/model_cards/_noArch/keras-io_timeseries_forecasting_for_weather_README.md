---
library_name: keras
tags:
- time-series
- time-series-forecasting
---

## Model description
Demonstrates timeseries forecasting using a [LSTM model.](https://keras.io/api/layers/recurrent_layers/lstm/)



## Full credits to:

* [Prabhanshu Attri](https://prabhanshu.com/github)
* [Yashika Sharma](https://github.com/yashika51)
* [Kristi Takach](https://github.com/ktakattack)
* [Falak Shah](https://github.com/falaktheoptimist)
* [Keras Example](https://keras.io/examples/timeseries/timeseries_weather_forecasting/#timeseries-forecasting-for-weather-prediction)



## Data Preprocessing

Here we are picking ~300,000 data points for training. Observation is recorded every 10 mins, that means 6 times per hour. We will resample one point per hour since no drastic change is expected within 60 minutes. We do this via the sampling_rate argument in timeseries_dataset_from_array utility.

We are tracking data from past 720 timestamps (720/6=120 hours). This data will be used to predict the temperature after 72 timestamps (72/6=12 hours).

Since every feature has values with varying ranges, we do normalization to confine feature values to a range of [0, 1] before training a neural network. We do this by subtracting the mean and dividing by the standard deviation of each feature.

71.5 % of the data will be used to train the model, i.e. 300,693 rows. split_fraction can be changed to alter this percentage.

The model is shown data for first 5 days i.e. 720 observations, that are sampled every hour. The temperature after 72 (12 hours * 6 observation per hour) observation will be used as a label.

## Training and evaluation data


We will be using Jena Climate dataset recorded by the Max Planck Institute for Biogeochemistry. The dataset consists of 14 features such as temperature, pressure, humidity etc, recorded once per 10 minutes.

Location: Weather Station, [Max Planck Institute for Biogeochemistry](https://www.bgc-jena.mpg.de/wetter/) in Jena, Germany.

Time-frame Considered: Jan 10, 2009 - December 31, 2016

The table below shows the column names, their value formats, and their description.

| Index | Features        | Format              | Description                                                                                                                                                                                                          | Selected Features |
|-------|-----------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| 1     | Date Time       | 01.01.2009 00:10:00 | Date-time reference                                                                                                                                                                                                  |                   |
| 2     | p (mbar)        | 996.52              | The pascal SI derived unit of pressure used to quantify internal  pressure. Meteorological reports typically state atmospheric pressure in  millibars.                                                               | +                 |
| 3     | T (degC)        | -8.02               | Temperature in Celsius                                                                                                                                                                                               | +                 |
| 4     | Tpot (K)        | 265.4               | Temperature in Kelvin                                                                                                                                                                                                | -                 |
| 5     | Tdew (degC)     | -8.9                | Temperature in Celsius relative to humidity. Dew Point is a measure of  the absolute amount of water in the air, the DP is the temperature at  which the air cannot hold all the moisture in it and water condenses. | -                 |
| 6     | rh (%)          | 93.3                | Relative Humidity is a measure of how saturated the air is with water  vapor, the %RH determines the amount of water contained within  collection objects.                                                           | -                 |
| 7     | VPmax (mbar)    | 3.33                | Saturation vapor pressure                                                                                                                                                                                            | +                 |
| 8     | VPact (mbar)    | 3.11                | Vapor pressure                                                                                                                                                                                                       | -                 |
| 9     | VPdef (mbar)    | 0.22                | Vapor pressure deficit                                                                                                                                                                                               | +                 |
| 10    | sh (g/kg)       | 1.94                | Specific humidity                                                                                                                                                                                                    | +                 |
| 11    | H2OC (mmol/mol) | 3.12                | Water vapor concentration                                                                                                                                                                                            | -                 |
| 12    | rho (g/m ** 3)  | 1307.75             | Airtight                                                                                                                                                                                                             | +                 |
| 13    | wv (m/s)        | 1.03                | Wind Speed                                                                                                                                                                                                           | +                 |
| 14    | max. wv (m/s)   | 1.75                | Maximum wind speed                                                                                                                                                                                                   | -                 |
| 15    | wd (deg)        | 152.3               | Wind direction in degrees                                                                                                                                                                                            | -                 |

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

| name | learning_rate | decay | beta_1 | beta_2 | epsilon | amsgrad | training_precision |
|----|-------------|-----|------|------|-------|-------|------------------|
|Adam|0.0010000000474974513|0.0|0.8999999761581421|0.9990000128746033|1e-07|False|float32|

 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>