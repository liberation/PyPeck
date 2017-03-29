from pyconst import Const

ASSET_TYPES = Const(
    ('Article', 'ARTICLE', 1),
    ('Video', 'VIDEO', 2),
    ('Twitter', 'TWITTER', 3),
    ('Instagram', 'INSTAGRAM', 4),
    ('Facebook', 'FACEBOOK', 4),
)

OEMBED_ENDPOINTS = [
    {
        "name": "Facebook Post",
        "templates": [
          "(?:www|m|business)\\.facebook\\.com/"
          "(permalink|story)\\.php\\?[^/]+(\\d{10,})",
          "(?:www|m|business)\\.facebook\\.com/"
          "photo\\.php\\?[^/]+(\\d{10,})",
          "(?:www|m|business)\\.facebook\\.com/"
          "([a-zA-Z0-9\\.\\-]+)/(posts|activity)/(\\d{10,})",
          "(?:www|m|business)\\.facebook\\.com/"
          "([a-zA-Z0-9\\.\\-]+)/photos/[^\\/]+/(\\d{10,})",
          "(?:www|m|business)\\.facebook\\.com/notes/"
          "([a-zA-Z0-9\\.\\-]+)/[^/]+/(\\d{10,})",
          "(?:www|m|business)\\.facebook\\.com/media/set/"
          "\\?set=[^/]+(\\d{10,})"
        ],
        "endpoint": "https://www.facebook.com/plugins/post/oembed.json/"
    },
    {
        "name": "Facebook Video",
        "templates": [
          "(?:www|business)\\.facebook\\.com/video/"
          "video\\.php.*[\\?&]v=(\\d{5,})(?:$|&)",
          "(?:www|business)\\.facebook\\.com/video/"
          "video\\.php\\?v=(\\d{5,})",
          "(?:www|business)\\.facebook\\.com/"
          "video\\.php.*[\\?&]v=(\\d{5,})(?:$|&)",
          "(?:www|business)\\.facebook\\.com/"
          "video\\.php.*[\\?&]id=(\\d{5,})(?:$|&)",
          "(?:www|business)\\.facebook\\.com/[a-zA-Z0-9.]+/videos/.+"
        ],
        "endpoint": "https://www.facebook.com/plugins/video/oembed.json/"
    },
    {
        "name": "Facebook Page",
        "templates": [
            "(www|m)\\.facebook\\.com/"
            "([a-zA-Z0-9\\.\\-]+)/?(?:\\?f?ref=\\w+)?$"
        ],
        "endpoint": "https://www.facebook.com/plugins/page/oembed.json/"
    },
    {
        "name": "YouTube",
        "templates": [
            "(?:www\\.)?youtube\\.com/(?:tv#/)"
            "?watch\\?(?:[^&]+&)*v=([a-zA-Z0-9_-]+)",
            "youtu\\.be/([a-zA-Z0-9_-]+)",
            "m\\.youtube\\.com/#/watch\\?(?:[^&]+&)*v=([a-zA-Z0-9_-]+)",
            "www\\.youtube\\.com/embed/([a-zA-Z0-9_-]+)",
            "www\\.youtube\\.com/v/([a-zA-Z0-9_-]+)",
            "www\\.youtube\\.com/user/[a-zA-Z0-9_-]+\\?v=([a-zA-Z0-9_-]+)",
            "www\\.youtube-nocookie\\.com/v/([a-zA-Z0-9_-]+)"
        ],
        "endpoint": "http://www.youtube.com/oembed"
    },
    {
        "name": "YouTube Playlist",
        "templates": [
            "www\\.youtube\\.com/playlist\\?list=([a-zA-Z0-9_-]+)"
        ],
        "endpoint": "http://www.youtube.com/oembed"
    },
    {
        "name": "SlideShare",
        "templates": [
            "\\w+\\.slideshare\\.net/.+/.*"
        ],
        "endpoint": "http://www.slideshare.net/api/oembed/2"
    },
    {
        "name": "Twitter Moments",
        "templates": [
            "twitter\\.com/i/moments/(\\d+)"
        ],
        "endpoint": "https://publish.twitter.com/oembed"
    },
    {
        "name": "Twitter Timelines",
        "templates": [
            "twitter\\.com/(\\w+)/timelines/(\\d+)",
            "twitter\\.com/(\\w+)/lists/(\\w+)",
            "twitter\\.com/(\\w+)/likes"
        ],
        "endpoint": "https://publish.twitter.com/oembed"
    },
    {
        "name": "Twitter Users",
        "templates": [
            "twitter\\.com/(\\w+)$"
        ],
        "endpoint": "https://publish.twitter.com/oembed"
    },
    {
        "name": "Instagr.am",
        "templates": [
            "([\\w\\.]*instagram\\.com/p/([a-zA-Z0-9_-]+))",
            "(instagr\\.am/p/([a-zA-Z0-9_-]+))"
        ],
        "endpoint": "https://api.instagram.com/oembed"
    },
    {
        "name": "DailyMotion",
        "templates": [
            "www\\.dailymotion\\.com/video/.+",
            "www\\.dailymotion\\.com/embed/video/.+"
        ],
        "endpoint": "http://www.dailymotion.com/services/oembed"
    },
    {
        "name": "Dailymotion",
        "templates": [
            "dailymotion\\.com/video/.+"
        ],
        "endpoint": "http://www.dailymotion.com/services/oembed"
    },
    {
        "name": "Vine",
        "templates": [
            "vine.co/v/([a-zA-Z0-9-]+)"
        ],
        "endpoint": "https://vine.co/oembed.json"
    },
    {
        "name": "Tumblr",
        "templates": [
            "[a-z0-9-]+\\.tumblr\\.com/(post|image)/\\d+"
        ],
        "endpoint": "https://www.tumblr.com/oembed/1.0"
    },
    {
        "name": "Getty Images",
        "templates": [
            "gty.im"
        ],
        "endpoint": "http://embed.gettyimages.com/oembed"
    },
]
