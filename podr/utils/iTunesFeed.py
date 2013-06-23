import xml.etree.ElementTree as ET
import urllib.request
import podr.models

ITUNES_NS = 'http://www.itunes.com/dtds/podcast-1.0.dtd'


class iTunesFeedParser():
    @staticmethod
    def parseSubscription(subscription):
        response = urllib.request.urlopen(subscription.link)
        html = response.read().decode("utf8")

        root = ET.fromstring(html)[0]

        subscription.copyright = root.find('copyright').text
        subscription.description = root.find('description').text
        subscription.language = root.find('language').text
        subscription.title = root.find('title').text
        #last_updated = models.DateTimeField('Last updated')

        return subscription
