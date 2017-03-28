import unittest
from test_twitter import TwitterScrapperTest
from test_instagram import InstagramScrapperTest
from test_video import VideoScrapperTest
from test_article import ArticleScrapperTest
from test_facebook import FacebookScrapperTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TwitterScrapperTest)
    suite.addTest(FacebookScrapperTest)
    suite.addTest(InstagramScrapperTest)
    suite.addTest(VideoScrapperTest)
    suite.addTest(ArticleScrapperTest)

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
