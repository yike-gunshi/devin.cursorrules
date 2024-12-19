import unittest
from unittest.mock import patch, MagicMock
from tools.llm_api import create_llm_client, query_llm

class TestLLMAPI(unittest.TestCase):
    def setUp(self):
        # Create a mock OpenAI client
        self.mock_client = MagicMock()
        self.mock_response = MagicMock()
        self.mock_choice = MagicMock()
        self.mock_message = MagicMock()
        
        # Set up the mock response structure
        self.mock_message.content = "Test response"
        self.mock_choice.message = self.mock_message
        self.mock_response.choices = [self.mock_choice]
        
        # Set up the mock client's chat.completions.create method
        self.mock_client.chat.completions.create.return_value = self.mock_response

    @patch('tools.llm_api.OpenAI')
    def test_create_llm_client(self, mock_openai):
        # Test client creation
        mock_openai.return_value = self.mock_client
        client = create_llm_client()
        
        # Verify OpenAI was called with correct parameters
        mock_openai.assert_called_once_with(
            base_url="http://192.168.180.137:8006/v1",
            api_key="not-needed"
        )
        
        self.assertEqual(client, self.mock_client)

    @patch('tools.llm_api.create_llm_client')
    def test_query_llm_success(self, mock_create_client):
        # Set up mock
        mock_create_client.return_value = self.mock_client
        
        # Test query with default parameters
        response = query_llm("Test prompt")
        
        # Verify response
        self.assertEqual(response, "Test response")
        
        # Verify client was called correctly
        self.mock_client.chat.completions.create.assert_called_once_with(
            model="Qwen/Qwen2.5-32B-Instruct-AWQ",
            messages=[{"role": "user", "content": "Test prompt"}],
            temperature=0.7
        )

    @patch('tools.llm_api.create_llm_client')
    def test_query_llm_with_custom_model(self, mock_create_client):
        # Set up mock
        mock_create_client.return_value = self.mock_client
        
        # Test query with custom model
        response = query_llm("Test prompt", model="custom-model")
        
        # Verify response
        self.assertEqual(response, "Test response")
        
        # Verify client was called with custom model
        self.mock_client.chat.completions.create.assert_called_once_with(
            model="custom-model",
            messages=[{"role": "user", "content": "Test prompt"}],
            temperature=0.7
        )

    @patch('tools.llm_api.create_llm_client')
    def test_query_llm_with_existing_client(self, mock_create_client):
        # Test query with provided client
        response = query_llm("Test prompt", client=self.mock_client)
        
        # Verify response
        self.assertEqual(response, "Test response")
        
        # Verify create_client was not called
        mock_create_client.assert_not_called()

    @patch('tools.llm_api.create_llm_client')
    def test_query_llm_error(self, mock_create_client):
        # Set up mock to raise an exception
        self.mock_client.chat.completions.create.side_effect = Exception("Test error")
        mock_create_client.return_value = self.mock_client
        
        # Test query with error
        response = query_llm("Test prompt")
        
        # Verify error handling
        self.assertIsNone(response)

if __name__ == '__main__':
    unittest.main()
