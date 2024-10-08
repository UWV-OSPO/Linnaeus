from abc import ABC, abstractmethod
import openai
import groq
import random


# Base abstract class for all LLM models
class LLMBase(ABC):
    def prepare_messages(self, message, prompt, history=None):
        """
        Prepares the list of messages to be passed to the model's API,
        including the system prompt, user message, and any conversation history.

        Args:
            message (str): The user's input message.
            prompt (str): The system's initial prompt.
            history (list of tuples): Previous exchanges between the user and assistant,
                                      if available.

        Returns:
            list: A list of formatted messages for the model API.
        """
        # Initial system message with the prompt
        messages = [{"role": "system", "content": prompt}]

        # Add conversation history if present
        if history:
            for human, assistant in history:
                messages.append({"role": "user", "content": human})
                messages.append({"role": "assistant", "content": assistant})

        # Add the latest user message
        messages.append({"role": "user", "content": message})

        return messages

    @abstractmethod
    def _call_model_api(self, messages):
        """
        Abstract method to handle the specific model's API call.
        Must be implemented by all subclasses.

        Args:
            messages (list): The list of messages prepared for the API request.

        Returns:
            str: The model's response.
        """
        pass

    def generate_response(self, message, prompt, history=None):
        """
        Generates the model's response by calling its API.

        Args:
            message (str): The user's input message.
            prompt (str): The system's initial prompt.
            history (list): A list of tuples representing conversation history,
                            where each tuple contains (user_message, assistant_message).

        Returns:
            str: The response generated by the model.
        """
        # Prepare messages and call the specific model's API
        messages = self.prepare_messages(message, prompt, history)
        response = self._call_model_api(messages)
        return response


# Groq-based model implementation using Llama
class LlamaModel(LLMBase):
    def __init__(self, groq_api_key):
        """
        Initializes the Llama model client using Groq's API.

        Args:
            groq_api_key (str): API key for the Groq service.
        """
        self.client = groq.Groq(api_key=groq_api_key)

    def _call_model_api(self, messages):
        """
        Calls the Groq API to get a response from the Llama model.

        Args:
            messages (list): The list of messages to send to the model.

        Returns:
            str: The content of the model's response.
        """
        # Groq API call for Llama model
        response = self.client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant",
            max_tokens=1000
        ).choices[0].message.content
        return response


# OpenAI GPT model implementation
class GPTModel(LLMBase):
    def __init__(self, openai_api_key):
        """
        Initializes the GPT model client using OpenAI's API.

        Args:
            openai_api_key (str): API key for OpenAI's service.
        """
        openai.api_key = openai_api_key

    def _call_model_api(self, messages):
        """
        Calls OpenAI's GPT API to get a response.

        Args:
            messages (list): The list of messages to send to the model.

        Returns:
            str: The content of the model's response.
        """
        # OpenAI GPT API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1000
        ).choices[0].message['content']
        return response


# Groq-based model implementation using Mistral
class MistralModel(LLMBase):
    def __init__(self, groq_api_key):
        """
        Initializes the Mistral model client using Groq's API.

        Args:
            groq_api_key (str): API key for the Groq service.
        """
        self.client = groq.Groq(api_key=groq_api_key)

    def _call_model_api(self, messages):
        """
        Calls the Groq API to get a response from the Mistral model.

        Args:
            messages (list): The list of messages to send to the model.

        Returns:
            str: The content of the model's response.
        """
        # Groq API call for Mistral model
        response = self.client.chat.completions.create(
            messages=messages,
            model="mixtral-8x7b-32768",
            max_tokens=1000
        ).choices[0].message.content
        return response


# Example for a new model implementation
class NewModel(LLMBase):
    def __init__(self, api_key):
        """
        Initializes a new model with its specific API key.

        Args:
            api_key (str): API key for the new model's service.
        """
        self.api_key = api_key

    def _call_model_api(self, messages):
        """
        Simulates a call to the new model's API and returns a static response.

        Args:
            messages (list): The list of messages to send to the model.

        Returns:
            str: Simulated response of the new model.
        """
        return "New Model's response"


# Manager class for handling multiple LLMs
class LLMManager:
    def __init__(self, models):
        """
        Initializes the LLM manager with a list of available model instances.

        Args:
            models (list): List of LLMBase model instances.
        """
        self.models = models

    def chat_with_models(self, message, prompt, history=None):
        """
        Sends a message to two randomly selected models.

        Args:
            message (str): The user's input message.
            prompt (str): The system's initial prompt.
            history (list of tuples): Previous conversation history as (user_message, assistant_message).

        Returns:
            tuple: Model A name, Model B name, Model A response, Model B response.
        """
        if len(self.models) < 2:
            raise ValueError("At least two models are required to chat.")

        # Randomly select 2 models from the list
        selected_models = random.sample(self.models, 2)

        model_a_name, model_a_response = None, None
        model_b_name, model_b_response = None, None

        for i, model in enumerate(selected_models):
            model_name = model.__class__.__name__
            response = model.generate_response(message, prompt, history)
            print(f'Response for {model_name} was generated')

            # Store the model names and responses
            if i == 0:
                model_a_name = model_name
                model_a_response = response
            else:
                model_b_name = model_name
                model_b_response = response

        return model_a_name, model_b_name, model_a_response, model_b_response
