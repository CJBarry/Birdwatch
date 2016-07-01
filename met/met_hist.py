import json
import requests
import math


BASE_URL = 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/'


def distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance on the surface of a WGS-84 earth between
       this coordinate and another coordinate.
       Result returned in METRES
    :param lat1: first latitude
    :param lon1: first longitude
    :param lat2: second latitude
    :param lon2: second longitude
    """
    # Code from https://github.com/geopy/geopy/blob/master/geopy/distance.py with minor adaptations
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)

    major, minor, f = (6376.137, 6356.7523142, 1 / 298.257223563)  # WGS-84

    delta_lng = lon2 - lon1

    reduced_lat1 = math.atan((1 - f) * math.tan(lat1))
    reduced_lat2 = math.atan((1 - f) * math.tan(lat2))

    sin_reduced1, cos_reduced1 = math.sin(reduced_lat1), math.cos(reduced_lat1)
    sin_reduced2, cos_reduced2 = math.sin(reduced_lat2), math.cos(reduced_lat2)

    lambda_lng = delta_lng
    lambda_prime = 2 * math.pi

    iter_limit = 20

    while abs(lambda_lng - lambda_prime) > 10e-12 and iter_limit > 0:
        sin_lambda_lng, cos_lambda_lng = math.sin(lambda_lng), math.cos(lambda_lng)

        sin_sigma = math.sqrt(
            (cos_reduced2 * sin_lambda_lng) ** 2 +
            (cos_reduced1 * sin_reduced2 -
             sin_reduced1 * cos_reduced2 * cos_lambda_lng) ** 2
        )

        if sin_sigma == 0:
            return 0  # Coincident points

        cos_sigma = (
            sin_reduced1 * sin_reduced2 +
            cos_reduced1 * cos_reduced2 * cos_lambda_lng
        )

        sigma = math.atan2(sin_sigma, cos_sigma)

        sin_alpha = (
            cos_reduced1 * cos_reduced2 * sin_lambda_lng / sin_sigma
        )
        cos_sq_alpha = 1 - sin_alpha ** 2

        if cos_sq_alpha != 0:
            cos2_sigma_m = cos_sigma - 2 * (
                sin_reduced1 * sin_reduced2 / cos_sq_alpha
            )
        else:
            cos2_sigma_m = 0.0  # Equatorial line

        C = f / 16. * cos_sq_alpha * (4 + f * (4 - 3 * cos_sq_alpha))

        lambda_prime = lambda_lng
        lambda_lng = (
            delta_lng + (1 - C) * f * sin_alpha * (
                sigma + C * sin_sigma * (
                    cos2_sigma_m + C * cos_sigma * (
                        -1 + 2 * cos2_sigma_m ** 2
                    )
                )
            )
        )
        iter_limit -= 1

    if iter_limit == 0:
        raise ValueError("Vincenty formula failed to converge!")

    u_sq = cos_sq_alpha * (major ** 2 - minor ** 2) / minor ** 2

    A = 1 + u_sq / 16384. * (
        4096 + u_sq * (-768 + u_sq * (320 - 175 * u_sq))
    )

    B = u_sq / 1024. * (256 + u_sq * (-128 + u_sq * (74 - 47 * u_sq)))

    delta_sigma = (
        B * sin_sigma * (
            cos2_sigma_m + B / 4. * (
                cos_sigma * (
                    -1 + 2 * cos2_sigma_m ** 2
                ) - B / 6. * cos2_sigma_m * (
                    -3 + 4 * sin_sigma ** 2
                ) * (
                    -3 + 4 * cos2_sigma_m ** 2
                )
            )
        )
    )

    s = minor * A * (sigma - delta_sigma)  # km
    return 1000.0 * s


def get_closet_site(lat, lon):
    """Finds url extension of site closest to given location

    :param lat: latitude in decimal degrees
    :param lon: longitude in decimal degrees
    """
    url = 'http://www.metoffice.gov.uk/pub/data/weather/uk/climate/historic/historic.json'
    response = requests.get(url)
    data = json.loads(response.text)
    site_url = ''
    dis = 100000000.0

    for location in data['open']:
        new_dis = distance(lat, lon, data['open'][location]['lat'], data['open'][location]['lon'])
        if new_dis < dis:
            dis = new_dis
            site_url = data['open'][location]['url']
    return site_url


def get_tmin(lat, lon, year, month):
    """Finds mean min air temp for a given month

    :param lat: latitude in decimal degrees
    :param lon: longitude in decimal degrees
    :param year: year as an int
    :param month: month as an int
    """
    sub_url = get_closet_site(lat, lon)
    url = BASE_URL + sub_url
    response = requests.get(url)
    lines = response.text.splitlines()

    count = 0
    for line in lines:
        if count > 8:
            data = line.split()
            if int(data[0]) == year and int(data[1]) == month:
                tmin = float(data[2])
                return tmin
        count += 1
    return 0


def get_tmax(lat, lon, year, month):
    """Finds mean mmax air temp for a given month

    :param lat: latitude in decimal degrees
    :param lon: longitude in decimal degrees
    :param year: year as an int
    :param month: month as an int
    """
    sub_url = get_closet_site(lat, lon)
    url = BASE_URL + sub_url
    response = requests.get(url)
    lines = response.text.splitlines()

    count = 0
    for line in lines:
        if count > 8:
            data = line.split()
            if int(data[0]) == year and int(data[1]) == month:
                tmin = float(data[3])
                return tmin
        count += 1
    return 0
