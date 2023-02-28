# weather-forecaster
The main aim of the project is to create the cloud base IoT whether forecast. The sensors should gather the data which will be further analyzed in the cloud. On the basis of the historical data the future weather should be predicted.

Up to today, the project had switched to the indoor application. The information in the cloud is useful to determine wether the heating should be turned on or if the window should be opened. What is more, thanks to to the AI-based method of the dominating color extraction the station can be used to stabilize sleeping habits.

Currently, reading the date from the humidity and temperature sensors has been implemented. Furthermore, on the basis of the camera image the dominating colors are collected. To dominating colors are extracted with the usage of sklearn kmeans clustering. The data is send to the thingspeak cloud where both current and the historical data can be observed and further analyzed.
