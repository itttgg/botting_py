# botting_py
Creating bots to yourself for monitoring user's inputs.

## Simple chat bot
To write a simple chat bot you need...
1. Import package bottingpy and create bot 
```python
import bottingpy

bot = bottingpy.chat.Bot()
```
2. Add keys for the bot using the ```addkey()``` or ```addkeys()``` method
```python
bot.addkey('hi', 'hi!')  # first is key, second is bot answer
bot.addkey('how are you?', 'I'm fine')  # here too

# All this code can be replaced with this code

bot.addkeys({
            'hi': 'hi!',
            'how are you?': 'I'm fine'
            })
```
3. Run the bot
```python
bot.run()  # Bot Starting
```
