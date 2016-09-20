import aiml
import talkey
import os
import talkey
import sys


 

def speak(text):
    voice = talkey.Talkey(engine_preference=['pico'])
    voice.say(text+'....')


Ava01 = ChatBot('Ava')
Ava = aiml.Kernel()
Ava.learn('/home/hydra/ProjectAva/standard/startup.xml')
Ava.learn('home/hydra/ProjectAva/ava/ai.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/inquiry.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/phone.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/religion.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/astrology.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/atomic.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/bot.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/client_profile.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/computers.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/history.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/money.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/loebner10.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/mp6.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/drugs.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/continuation.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/date.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/movies.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/humor.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/numbers.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/mp0.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/personality.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/psychology.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/imponderables.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/reduction.names.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/reduction0.safe.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/salutations.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/science.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/sex.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/update1.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/update_mccormick.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/wallace.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/xfind.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/sports.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/stack.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/reduction2.safe.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/pickup.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/mp2.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/interjection.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/iu.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/startup.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/mp3.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/politics.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/knowledge.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/mp4.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/stories.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/literature.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/mp5.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/primitive-math.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/that.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/reduction3.safe.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/reduction4.safe.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/reductions-update.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/drugs.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/biography.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/bot.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/bot_profile.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/food.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/client.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/geography.aiml')
Ava.learn('/home/hydra/ProjectAva/ava/gossip.aiml')

while True:
   
    question = raw_input('>>')
   
    speak(Ava.respond(question))
    print(Ava.respond(question))
    
    
