# Task 1 

1. Create an API using FastAPI to provide weather data for different locations. Implement HTTPException to handle errors, and add API Key authentication for secure access.

2. Assume we have a dictionary containing weather data for three locations: "New York City," "Los Angeles," and "Chicago." Each location has temperature and weather condition information.

3. Create a FastAPI app and define two endpoints:
    - Endpoint 1: `/weather/{location}` This endpoint will provide weather data for a specific location.
    - Endpoint 2:`/authenticate` This endpoint will handle API Key authentication.

4. Use HTTPException to handle cases where the requested location is not available in the `weather_data` dictionary.
