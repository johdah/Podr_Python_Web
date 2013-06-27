from datetime import datetime
import urllib.request
import xml.etree.ElementTree as ET
from podr.utils import utils
from podr.models import Episode

XML_NS = {
    'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'media': 'http://search.yahoo.com/mrss/'}


class iTunesFeedParser():
    def parse(subscription):
        response = urllib.request.urlopen(subscription.link)
        html = response.read().decode("utf8")

        root = ET.fromstring(html)[0]
        subscription = iTunesFeedParser.parseSubscription(subscription, root)

        items = list(root.iter("item"))
        episodes = iTunesFeedParser.parseEpisodes(subscription, items)

        return subscription, episodes

    def parseChannel(subscription):
        response = urllib.request.urlopen(subscription.link)
        html = response.read().decode("utf8")

        root = ET.fromstring(html)[0]
        subscription = iTunesFeedParser.parseSubscription(subscription, root)

        return subscription

    @staticmethod
    def parseSubscription(subscription, root):
        #TODO: Keywords, category, image, itunes:new-feed-url, guid#isPermaLink
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


    def parseEpisodes(subscription, items):
        episodes = []
        for item in items:
            guid = item.find('guid', namespaces=XML_NS)
            if guid is None:
                continue

            episode, created = Episode.objects.get_or_create(subscription=subscription, guid=guid.text, defaults={
                            'guid': guid.text, 'pub_date': datetime.now()})

            if created is False:
                break

            episode_title = item.find('title', namespaces=XML_NS)
            episode_enclosure = item.find('enclosure', namespaces=XML_NS)
            episode_itunes_author = item.find('itunes:author', namespaces=XML_NS)
            episode_itunes_block = item.find('itunes:block', namespaces=XML_NS)
            episode_itunes_duration = item.find('itunes:duration', namespaces=XML_NS)
            episode_itunes_explicit = item.find('itunes:explicit', namespaces=XML_NS)
            episode_itunes_image = item.find('itunes:image', namespaces=XML_NS)
            episode_itunes_isClosedCaptioned = item.find('itunes:isClosedCaptioned', namespaces=XML_NS)
            episode_itunes_subtitle = item.find('itunes:subtitle', namespaces=XML_NS)
            episode_itunes_summary = item.find('itunes:summary', namespaces=XML_NS)
            episode_media_thumbnail = item.find('media:thumbnail', namespaces=XML_NS) #sometimes used as a replacement for itunes:image
            episode_pubDate = item.find('pubDate', namespaces=XML_NS)

            if episode_title is not None:
                episode.title = episode_title.text
            else:
                episode.title = "Unknown"

            if episode_enclosure is not None:
                if episode_enclosure.attrib.get('length') is not None:
                    episode.enclosureLength = episode_enclosure.attrib.get('length')
                if episode_enclosure.attrib.get('type') is not None:
                    episode.enclosureType = episode_enclosure.attrib.get('type')
                if episode_enclosure.attrib.get('url') is not None:
                    episode.enclosureUrl = episode_enclosure.attrib.get('url')

            if episode_itunes_author is not None:
                episode.itunes_author = episode_itunes_author.text

            if episode_itunes_block is not None and episode_itunes_block.text == "yes":
                episode.itunes_block = True

            if episode_itunes_duration is not None:
                episode.itunes_duration = utils.to_seconds(episode_itunes_duration.text)

            if episode_itunes_explicit is not None and episode_itunes_explicit.text == "yes":
                episode.itunes_explicit = True

            if episode_itunes_image is not None and episode_itunes_image.attrib.get('href') is not None:
                episode.itunes_image = episode_itunes_image.attrib.get('href')
            else:
                if episode_media_thumbnail is not None and episode_media_thumbnail.attrib.get('url') is not None:
                    episode.itunes_image = episode_media_thumbnail.attrib.get('url')

            if episode_itunes_isClosedCaptioned is not None and episode_itunes_isClosedCaptioned.text == "yes":
                episode.itunes_isClosedCaptioned = True

            if episode_itunes_subtitle is not None:
                episode.itunes_subtitle = episode_itunes_subtitle.text

            if episode_itunes_summary is not None:
                episode.itunes_summary = episode_itunes_summary.text

            if episode_pubDate is not None:
                episode.pub_date = utils.getDatetime(episode_pubDate.text)

            episodes.append(episode)

        return episodes


