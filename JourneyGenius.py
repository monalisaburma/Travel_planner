# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:52:46 2023

@author: ASUS
"""

import streamlit as st
from langchain.llms import OpenAI


# Initialize LangChain with your OpenAI API key
llm = OpenAI(openai_api_key="YOUR_OPENAI_API_KEY", model="gpt-3.5-turbo", temperature=0.9, max_tokens=3500)

def generate_itinerary(destinations, number_of_nights, trip_type):
    prompt_template = "Generate a daywise detailed itinerary with specific place names for a {trip_type} trip to {destinations} for {nights} nights."
    trip_prompt = prompt_template.format(trip_type=trip_type, destinations=destinations, nights=number_of_nights)
   
    st.markdown(f'<p style=\'font-family: "Times New Roman", sans-serif; font-size: 18px; color: #000;\'>{trip_prompt}</p>', unsafe_allow_html=True)
    
    # Generate text using LangChain
    result = llm(trip_prompt)
    return result


def main():
    # Set page configuration for better responsiveness
    st.set_page_config(
        page_title="JourneyGenius - Tailored Travel Experiences",
        page_icon=":earth_americas:",
        layout="centered",
        initial_sidebar_state="auto",
    )

    # Add a logo, banner, and animation
    st.markdown(
        r'''
        <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }

            .stApp {
                width: 87%; /* Adjust the percentage as needed */
                margin: auto; /* Center the app on the screen */
                background: linear-gradient(135deg, #e6e6ff, #f0ccff, #ffe6cc);
                background-size: cover;
                color: #000; /* Text color */
                text-align: center;
                height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }

            .logo {
                max-width: 50%; /* Make the logo responsive */
                height: auto;
                object-fit: contain;
                animation: fadeIn 2s;
            }

            .header {
                padding: 20px; /* Adjust padding for smaller screens */
            }
            
            h1 {
                font-family: 'Times New Roman', sans-serif;
                font-size: 35px;
                line-height: 1;
                margin: 0;
                text-align: center;
            }

            .bold-text {
                font-weight: bold;
            }

            .input-title {
                font-size: 16px;
                font-family: 'Times New Roman', serif;
                font-weight: bold;
                margin-bottom: -40px;
                text-align: left;
            }

            .stTextInput, .stNumberInput, .stSelectbox {
                margin-bottom: 20px; /* Adjust margin for smaller screens */
            }
                
           
            
        </style>
        ''',
        unsafe_allow_html=True
    )
   
    # Header section with logo
    st.markdown(
        r'''
        <div class="header">
            <div class="logo-container">
                <img src="https://media0.giphy.com/media/fsnNgnq0CSeTLU9pW6/source.gif" alt="Logo" class="logo">
            </div>                
            <div>
                <h1 class="bold-text" style="margin: 0; font-size: 30px; font-family: 'Times New Roman', serif; color: #3b0054; text-align: center">JourneyGenius</h1>
                <h1 class="bold-text" style="margin: 0; font-size: 18px; font-family: 'Times New Roman; color: #4a006a; margin-top: -20px;" >Tailored Travel Experiences</h1>
            </div>         
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Streamlit app content
    st.markdown("<p class='input-title'>Enter the destination:</p>", unsafe_allow_html=True)
    destinations = st.text_input(" ", placeholder="e.g., Paris, Tokyo", key="dest_input")

    # Repeat the process for other inputs
    st.markdown("<p class='input-title'>Number of nights:</p>", unsafe_allow_html=True)
    number_of_nights = st.number_input(" ", min_value=1, step=1, key="nights_input")

    st.markdown("<p class='input-title'>Type of trip:</p>", unsafe_allow_html=True)
    trip_type = st.selectbox(" ", ["Historical Exploration", "Adventure Quest", "Culinary Delight", "Relaxing Retreat", "Nature Escapade", "Luxury Getaway", "Art and Culture Immersion", "Road Trip Extravaganza", "Wildlife Safari", "Romantic Rendezvous", "Fitness and Wellness Retreat", "Photography Expedition", "Island Paradise", "Urban Exploration", "Festival and Events Tour", "Mountain Expedition", "Underwater Adventure", "Educational Discovery", "Architectural Marvels", "Hidden Gem Discovery"], key="trip_type_input")

    if st.button("Generate Itinerary"):
        itinerary = generate_itinerary(destinations, number_of_nights, trip_type)
        st.markdown(itinerary)

if __name__ == "__main__":
    main()
