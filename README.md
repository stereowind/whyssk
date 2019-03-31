# Whyssk

Whyssk is a **customizable and extensible** game app where player is presented with one **card** at a time which can be **whisked off** to the right or to the left to progress through the **story**.  
Every card has **Call To Action (CTA)** written in text. 
Right and left sides present two **actions** related to the CTA.  
Player has 1 to 4 **feature bars** that represent **features** and impacted by player actions. Actions can impact from none to all features. 
Session reaches it's end according to pre-defined win and lose conditions: 
either when one of the features reaches a certain value, or when session runs out of cards.  

Whyssk's distinctive feature is that you can create your own scenarios and upload them to the app. You can define:
- Session settings
- Features (1 to 4)
- Win or lose conditions
- Cards, actions and their impact on features

## Goal
This long-term project was started as a mean to improve personal programming skills and create a portfolio item, 
as well as a contribution to open-source community.

End goal is to create a complete web app that will provide an easy to use instrument to create game sessions with two-option choices for various purposes.

## How to launch
Download archive and unpack.
Open command prompt or terminal inside the folder with `whyssk` and run `python whyssk` (or `python3 whyssk`)

**Note:** requires Python >= 3.6 !

## Current roadmap
#### Main goals per phase
- **Phase 1**: Finalize console prototype
- **Phase 2**: Run console prototype as a web interface
- **Phase 3**: Create web backend using Flask
- **Phase 4**: Create complete beautiful frontend using HTML\CSS\JS

#### Planned features
- Thorough check of imported settings file for error
- Character limits for all texts
- Non-linear session progression (i.e. card dependencies)
- Different endings (win and lose conditions)
- Session file creator GUI
- Indicators for feature value changes for each action

## Session settings file (.json)
Please see `template.json` in `sessions/` for a template.  
You can also refer to pre-defined session files (currently only lame `beerquest.json` is available)

*Note*: for win and lose conditions, `out_of_cards` parameters of both conditions must have opposite values (i.e. both can't be true or false at the same time).

## Project structure
```python 
sessions/-*.json           # Custom story settings files
        \-template.json    # Story settings template
__main__.py                # Initializes Whyssk
classes.py                 # File with classes used in session
get_settings.py            # Import json settings
session.py                 # Main session logic
```

## Name
Whyssk \[waisk\] is rather lamely derived from the word "whisk" and combination "whisk off", symbolizing how cards are whisked off 
either to the right or to the left. Synonym alternative to words "swipe" and "flick". "i" changed to "y" as a nod to Python language that is used to build this app. Extra "s" added for name uniqueness.