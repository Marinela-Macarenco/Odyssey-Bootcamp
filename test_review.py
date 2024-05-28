import unittest
from unittest.mock import patch
from review import scrape_reviews

class TestScrapeReviews(unittest.TestCase):
    
    @patch('review.requests.get')
    def test_scrape_reviews(self, mock_get):
        # Mocking the response from requests.get
        mock_response = '<html><div class="section-title-article pl-3'
        'border-l-4 border-green-500">Title</div><p>Review content</p></html>'
        mock_get.return_value.text = mock_response
        
        # Test the function with the mocked response
        url = 'https://www.completecar.ie/car-reviews/article/Porsche/Macan/'
        'Macan_Turbo_electric_(2024)/2329/13219/'
        '2024-Porsche-Macan-Turbo-electric-(2024)-review.html'
        result = scrape_reviews(url)
        
        # Expected result
        expected_result = [{'Title': 'Title', 'Content': 'Review content'}]
        
        # Check if the result matches the expected result
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
