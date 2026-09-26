# AI Travel Agent

An AI-powered travel agent built using **Agno**, **Groq**, and **web search**.

The agent can research travel-related information and provide helpful responses about destinations, travel plans, places to visit, safety, and other travel-related queries.

## Features

- AI-powered travel assistance
- Web search for travel research
- Destination information
- Travel planning
- Places to visit
- Travel safety information
- Current travel-related information
- Markdown-formatted responses
- Built using Agno and Groq

## Architecture

```text
                    User Query
                        |
                        v
                +---------------+
                |  Travel Agent |
                +-------+-------+
                        |
                        v
                 Groq AI Model
                        |
                        v
                  Web Search
                        |
                        v
                Travel Information
                        |
                        v
                   AI Response
```
## Technologies Used

- Python
- Agno
- Groq
- DuckDuckGo Web Search
- python-dotenv
- Streamlit

## Project Structure

```text
travel-agent/
|
├── agent.py
├── app.py
├── requirements.txt
├── .gitignore
└── .env
```

## Installation

Clone the repository:

```bash
git clone https://github.com/arishak10/travel-agent.git
cd travel-agent
```
Create a virtual environment:
```bash
python -m venv .venv
```

Activate the virtual environment on Windows:
```bash
.venv\Scripts\activate
```
Install the required packages:
```bash
pip install -r requirements.txt
```
## Environment Setup

Create a .env file in the project folder:
```bash
GROQ_API_KEY=your_groq_api_key
```
Replace your_groq_api_key with your own Groq API key.

## Run the Project

Start the Streamlit application:
```bash
streamlit run app.py
```
The application will open in your browser.

## Example Queries

Plan a 5-day trip to Dubai.
What are the best places to visit in Mumbai?
What should I know before travelling to Japan?
Suggest a travel itinerary for Paris.

## Purpose

This project demonstrates how an AI agent can combine a large language model with web search to research travel information and provide useful travel assistance.

## Author

Arisha Khan

Computer Science Student | AI/ML Enthusiast
