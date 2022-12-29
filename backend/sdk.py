import requests


class VRClient:
    baseURL = "https://pdf.astrologyapi.com/v1/"

    def __init__(self, uid, key):
        self.userID = uid
        self.apiKey = key

    def getUrl(cls):
        return cls.baseURL

    def getResponse(self, resource, data):
        # print(self.userID)
        url = self.getUrl() + resource
        resp = requests.post(url, data=data, auth=(self.userID, self.apiKey))
        return resp

    def packageReportData(self, name, gender, day, month, year, hour, minute, lat, lon, tzone, place, language):
        return {
            "name" : name,
            "gender" : gender,
            "day" : day,
            "month" : month,
            "year" : year,
            "hour" : hour, 
            "min" : minute,
            "lat" : lat, 
            "lon" : lon,
            "tzone" : tzone,
            "place" : place,
            "language" : language,
            "chart_style" : "SOUTH_INDIAN",
            "footer_link" : "astrologyapi.com",
            "logo_url" : "logo_url",
            "company_name" :"Vedic Rishi Astro Solutions Pvt. Ltd.",
            "company_info" : "Your Company Info",
            "domain_url" : "https://www.astrologyapi.com", 
            "company_email" : "mail@astrologyapi.com",
            "company_landline" : "+91- 221232 22",
            "company_mobile" : "+91 1212 1212 12",
        }
    
    def reportCall(self, resource, name, gender, day, month, year, hour, minute, lat, lon, tzone, place, language):
        data = self.packageReportData(name, gender, day, month, year, hour, minute, lat, lon, tzone, place, language)
        return self.getResponse(resource, data)


class JsonClient:
    baseURL = "https://json.astrologyapi.com/v1/"

    def __init__(self, uid, key):
        self.userID = uid
        self.apiKey = key

    def getUrl(cls):
        return cls.baseURL

    def getResponse(self, resource, data):
        # print(self.userID)
        url = self.getUrl() + resource
        resp = requests.post(url, data=data, auth=(self.userID, self.apiKey))
        return resp

    def packagePlaceData(self, place):
        return {
            "place" : place,
            "maxRows" : 5,
        }
    
    def placeCall(self, resource, place):
        data = self.packagePlaceData(place)
        return self.getResponse(resource, data)

    def packageZoneData(self, tzone):
        return {
            "country_code" : tzone,
            "isDst" : False,
        }
    
    def zoneCall(self, resource, tzone):
        data = self.packageZoneData(tzone)
        return self.getResponse(resource, data)