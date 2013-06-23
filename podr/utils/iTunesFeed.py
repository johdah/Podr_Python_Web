from datetime import datetime
import urllib.request
import xml.etree.ElementTree as ET

XML_NS = {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}


class iTunesFeedParser():
    @staticmethod
    def parseSubscription(subscription):
        response = urllib.request.urlopen(subscription.link)
        html = response.read().decode("utf8")

        root = ET.fromstring(html)[0]

        subscription_title = root.find('title')
        subscription_copyright = root.find('copyright')
        subscription_description = root.find('description')
        subscription_language = root.find('language')
        subscription_itunes_author = root.find('itunes:author', namespaces=XML_NS)
        subscription_itunes_block = root.find('itunes:block', namespaces=XML_NS)
        subscription_itunes_complete = root.find('itunes:complete', namespaces=XML_NS)
        subscription_itunes_explicit = root.find('itunes:explicit', namespaces=XML_NS)
        subscription_itunes_image = root.find('itunes:image', namespaces=XML_NS)
        subscription_itunes_owner = root.find('itunes:owner', namespaces=XML_NS)
        subscription_itunes_subtitle = root.find('itunes:subtitle', namespaces=XML_NS)
        subscription_itunes_summary = root.find('itunes:summary', namespaces=XML_NS)

        if subscription_itunes_owner is not None:
            subscription_itunes_owner_email = subscription_itunes_owner.find('itunes:email', namespaces=XML_NS)
            subscription_itunes_owner_name = subscription_itunes_owner.find('itunes:name', namespaces=XML_NS)

        if subscription_title is not None:
            subscription.title = subscription_title.text
        else:
            subscription.title = "Unknown"

        if subscription_copyright is not None:
            subscription.copyright = subscription_copyright.text

        if subscription_description is not None:
            subscription.description = subscription_description.text

        if subscription_language is not None:
            subscription.language = subscription_language.text

        if subscription_itunes_author is not None:
            subscription.itunes_author = subscription_itunes_author.text

        if subscription_itunes_block is not None and subscription_itunes_block.text == "yes":
            subscription.itunes_block = True

        if subscription_itunes_complete is not None and subscription_itunes_complete.text == "yes":
            subscription.itunes_complete = True

        if subscription_itunes_explicit is not None and subscription_itunes_explicit.text == "yes":
            subscription.itunes_explicit = True

        if subscription_itunes_image is not None and subscription_itunes_image.attrib.get('href') is not None:
            subscription.itunes_image = subscription_itunes_image.attrib.get('href')

        if subscription_itunes_owner_email is not None:
            subscription.itunes_owner_email = subscription_itunes_owner_email.text

        if subscription_itunes_owner_name is not None:
            subscription.itunes_owner_name = subscription_itunes_owner_name.text

        if subscription_itunes_subtitle is not None:
            subscription.itunes_subtitle = subscription_itunes_subtitle.text

        if subscription_itunes_summary is not None:
            subscription.itunes_summary = subscription_itunes_summary.text

        subscription.last_updated = datetime.now()

        return subscription

    #def parseEpisodes():
        #datetime.strptime(root.find('last_updated').text, '%a %b %d %H:%M:%S +0000 %Y')