#importing package
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector("")
        self.assetEqual(result_1[])
    