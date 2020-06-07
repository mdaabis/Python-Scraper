# Python Price Scraper

This Python script periodically checks the price of a chosen item on Amazon (requiring only the product URL) and alerts the user (via an SMS) when the price of that product falls below a certain threshold value.

## Getting Started

Use the `.env_sample` file to add variables such as the 'TO' number (a Twilio account is used to set this up and purchase a number to use as the `FROM` number) and the account SID and authentication token for the Twilio account. Also, make sure to add the URL of the product in question and the threshold price.

