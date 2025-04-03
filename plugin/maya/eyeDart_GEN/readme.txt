EYE DART TOOLS
by Andrewwillish @ 2024
===================================================================================

Tools Description:
Use this tools to generate eye-dart either manually or automatically by detecting the blink parameter of a character (might not work on complex rig).

How To Install:
The tools is in plugin form that recognizable by maya. Follow the following step
to install it to your Maya:
1. Download the eyeDart_GEN folder and place it to your local folder
2. Start your maya
3. Open Plugin Manager (Windows -> Settings/Preferences -> Plugin Manager)
4. Click Browse
5. Go to eyeDart_GEN folder and open ANIM_autoEyeDart_GEN_hook.py
6. New menu should appear in your Maya called Wlls Tools.

How To Use (Manual):
1. Start the tools
2. Set the magnitude range (how far is the eye dart magnitude), set the amount per dart range (how many darting range per click).
3. Select the eye direction controller then click APPLY.

How To Use (Auto):
1. Do the manual bit
2. Set the time range you want the eye dart to generate
3. Set the between occurance range (how many frame you want between eye dart, lower value will make the dart more often)
4. Set the trigger attribute by right click on the field and set channel attribute (this is the attribute value that will be checked by operator to see if a character eye is open or not)
5. Set the operators (lower or higher than)
6. Set the treshold of the value of the blink before the generate can happen (its useless to do dart when the eye is closed).
7. Click Apply.

If you want to see on how to use it, check out the following youtube video.

https://youtu.be/kq4rBUvMZpo

Be sure to credit me if you find my tools helpful for your project. 

Any bug or problem just contact me at andrewwillish@gmail.com

Cheers,
Andrew