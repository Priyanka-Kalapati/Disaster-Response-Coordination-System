# Disaster-Response-Coordination-System

Project Summary:
The Disaster Response Coordination System is an advanced web-based application developed to improve the efficiency of disaster management and relief coordination using a multi-agent system architecture powered by Google Cloud’s Agent Development Kit (ADK). The system integrates real-time backend outputs, past disaster data visualization, and user-friendly features into one unified interface.This platform is designed to simulate real-time decision-making and resource allocation during disaster situations such as floods, earthquakes, cyclones, and industrial accidents. It serves as a complete demonstration of multi-agent orchestration, backend-to-frontend data flow, and disaster information dissemination.

Core Features & Functionality:
1.User Authentication & Entry:
Login system capturing user name, email, and phone number.
Personalized welcome message on successful login.

2.Dynamic Navigation:
A smooth navbar for easy switching between:
Home
About
Disasters
Agents
Backend Output (Real-Time)
Helpline Numbers
Logout

3.About Section:
Comprehensive details about the system’s purpose.
Explains multi-agent-based disaster management.
Lists disaster types: Natural (Cyclones, Earthquakes, Tsunamis) and Man-made (Fires, Chemical Leaks).

4.Disasters Section:
Real-world historical disasters showcased with descriptions & images:
2004 Indian Ocean Tsunami — 230,000+ deaths; Asia’s most catastrophic tsunami.
Bhopal Gas Tragedy (1984) — World’s worst industrial gas leak disaster.
Kerala Floods (2018) — Heavy monsoon-caused floods impacting millions.
Odisha Super Cyclone (1999) — Category-5 cyclone affecting thousands in coastal India.
Disaster images and modals give users detailed background info.

5.Agents Section:
Details of government bodies like:
NDMA — National Disaster Management Authority.
SDMA — State Disaster Management Authorities.
NDRF — National Disaster Response Force.

6.Real-Time Backend Output (Flask + ADK Agents):
Fetches live agent-generated data from the Python Flask backend.
Displays results from:
Data Analysis Agent
Location Agent
Rescue Agent
Supply Agent
Communication Agent
Data includes situation analysis, location info, rescue plans, supply status, and communication logs.

7.Helpline Section:
Important national emergency numbers listed:
Police, Fire, Ambulance, National Disaster Helpline.
Smooth Animations & Design:
Responsive UI/UX using modern CSS animations, smooth fade-in/fade-out effects, modal popups, and a gradient-themed background.
Fully mobile-friendly design.

Technologies Used:
1.Frontend:
HTML5
CSS3 (Modern, responsive design)
JavaScript (DOM manipulation, event handling, modal popups)

2.Backend:
Python Flask API
Google Cloud Agent Development Kit (ADK) — Simulated multi-agent output

3.Data Sources:
Disaster history manually curated.
Real-time backend output generated via simulated ADK agents.

Architecture Diagram:
               +-----------------------------+
               |         User (Browser)       |
               +--------------+--------------+
                              |
                   (HTML/CSS/JS Frontend)
                              |
               +--------------v--------------+
               |      Python Flask Server     |
               +--------------+--------------+
                              |
           +------------------+-------------------+
           |         |            |          |     |
   DataAnalysis  Location   Rescue   Supply  Communication
      Agent       Agent      Agent    Agent     Agent
 (ADK - Google Cloud Simulated Multi-Agent System)

Conclusion:
This project demonstrates the practical use of multi-agent systems in disaster response, combining both backend intelligence and frontend visualization for an educational and potentially deployable solution in real-life disaster scenarios.
