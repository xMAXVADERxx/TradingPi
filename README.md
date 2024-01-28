# TradingPi
A basic Python binding for the Trading 212 API, implementing core functionality behind a Python-Style class.
This is a custom module I made mainly for myself, and hence is not endorsed in any way by Trading 212 or affiliates.
As with all things trading, please be careful! I do not take responsibility for any losses caused by this API (though feel free to share the gains!).

At its current state, this module is useless, however it will connect to the api and allow for queued requests, should you wish to do so.

# Initial Goals
The main goal for the Version 1 of this project is to allow for the API's basic functinons to be fully implemented within the module itself, hence allowing for a user to simply grab an API Key and invest.

This project will not aim, for the time being, to implement any complex functions (or even some simple ones), that is for you to do yourself.

As things stand, this isn't even really a Python module, so you'll need to import it as you would any other file.

# Help
When using the API, you may encounter some error codes. The system will pass any request data directly to the user, and so you may wish to look into the Trading 212 API Specification for help.

For ease of use, here are the common errors you may first encounter, and some potential fixes:

**ERROR 401**: Caused by a bad API key, make sure your key is valid and you are in the right mode (A live key will not work in demo mode!)

**ERROR 403**: Caused by missing metadata or a bad scope, make sure the key has the right permissions and that the calls are correct!

**ERROR 408**: Caused by a timeout, this could be an issue on your end or at Trading 212, so feel free to call again.

**ERROR 429**: Caused by making too many requests in a certain time span, T212 limits to one every 1/30s. Make sure to use the built-in queue command, or check you aren't making too many requests.

# API Basics

I'll show you how to use the API here, when I've implemented enough for it to matter
