# BENNA – AI-Powered Scent Recommendation System

## Overview
BENNA is a conceptual AI-based system that generates personalized fragrance compositions based on user input, mood, and environmental data.

(The project was developed in the context of the L'Oréal Brandstorm innovation challenge and focuses on combining Artificial Intelligence with sensory experiences.)

---

## Objective
The goal of BENNA is to support user decision-making by:
- analyzing emotional and contextual data
- mapping inputs to fragrance profiles
- generating personalized scent recommendations

---

##  System Architecture

The system is divided into three main components:

### 👤 User
### 📱 Application (Core AI Logic)
### ⚙️ Device (Hardware Layer)

---

## Data Pipeline

1. **Input**
   - User preferences (e.g., fresh, woody)
   - Emotional state (mood detection)
   - Context data (temperature, time)

2. **Processing**
   - Feature extraction
   - Classification using decision rules

3. **Output**
   - Scent profile (e.g., Citrus, Vanilla, Lavender)
   - Signal to fragrance device

---

##  Decision Model

The system uses a simple **Decision Tree** to classify inputs into scent categories.

### Example Logic:

- If user provides preference → direct mapping  
- Else:
  - If mood = tired → Lavender  
  - If mood = stressed → Chamomile  
  - If temperature = cold → Warm scents (Vanilla)  
  - If temperature = warm → Fresh scents (Citrus)

---


## Future Improvements
- Replace Decision Tree with ML model
- Add real user data
- Connect to IoT device
