"""Constants for the Hong Kong Observatory [Wind Speed] integration."""

DOMAIN = "hko_wind_speed"

LOCATIONS = [
    {"LOCATION": "Central Pier"},
    {"LOCATION": "Check Lap Kok"},
    {"LOCATION": "Cheung Chau"},
    {"LOCATION": "Cheung Chau Beach"},
    {"LOCATION": "Green Island"},
    {"LOCATION": "Hong Kong Sea School"},
    {"LOCATION": "Kai Tak"},
    {"LOCATION": "King's Park"},
    {"LOCATION": "Lamma Island"},
    {"LOCATION": "Lau Fau Shan"},
    {"LOCATION": "Ngong Ping"},
    {"LOCATION": "North Point"},
    {"LOCATION": "Peng Chau"},
    {"LOCATION": "Sai Kung"},
    {"LOCATION": "Sha Chau"},
    {"LOCATION": "Sha Tin"},
    {"LOCATION": "Shek Kong"},
    {"LOCATION": "Stanley"},
    {"LOCATION": "Star Ferry"},
    {"LOCATION": "Ta Kwu Ling"},
    {"LOCATION": "Tai Mei Tuk"},
    {"LOCATION": "Tai Po Kau"},
    {"LOCATION": "Tap Mun"},
    {"LOCATION": "Tate's Cairn"},
    {"LOCATION": "Tseung Kwan O"},
    {"LOCATION": "Tsing Yi"},
    {"LOCATION": "Tuen Mun"},
    {"LOCATION": "Waglan Island"},
    {"LOCATION": "Wetland Park"},
    {"LOCATION": "Wong Chuk Hang"},
]

KEY_LOCATION = "LOCATION"

DEFAULT_LOCATION = LOCATIONS[0][KEY_LOCATION]

ATTRIBUTION = "Data provided by the Hong Kong Observatory"
MANUFACTURER = "Hong Kong Observatory"

API_ENDPOINT = "https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_10min_wind.csv"

API_DATE = "Date time"
API_STATION = "Automatic Weather Station"
API_BEARING = "10-Minute Mean Wind Direction(Compass points)"
API_WIND_SPEED = "10-Minute Mean Speed(km/hour)"
API_GUST_SPEED = "10-Minute Maximum Gust(km/hour)"

CARDINAL_DIRECTIONS: list[str] = [
    "North",
    "Northnortheast",
    "Northeast",
    "Eastnortheast",
    "East",
    "Eastsoutheast",
    "Southeast",
    "Southsoutheast",
    "South",
    "Southsouthwest",
    "Southwest",
    "Westsouthwest",
    "West",
    "Westnorthwest",
    "Northwest",
    "Northnorthwest",
]
