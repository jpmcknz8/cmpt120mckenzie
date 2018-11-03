# personality.py
# Get the mode of interaction from the user
# Returns: an integer indicating one of reward, punish, joke, or threaten

emotions = ["anger", "happiness", "disgist", "fear", "sadness", "surprise"]
interactions = ["reward", "punish", "threaten", "joke"]

emotionMatrix = [[1,0,0,5],[5,4,3,1],[2,2,3,2],[5,3,3,5],[1,0,3,1],[5,0,3,1]]

expressions = ["I am furious!",
               "This is so much fun! I am a happy camper!",
               "How disgusting!",
               "I am so scared, help!",
               "You hurt my feelings, I am sad...",
               "What a surprise!"]

def intro(emotions, currEmotion):
    print("Hello! I am currently feeling ", currEmotion,"!")
    print("Interact with me to change how I am feeling!")

def getInteraction(interactions):
    interaction = interactions.index(input("Please enter an interaction(punish, reward, threaten, joke): ").lower())
    return(interaction)
               
def lookupEmotion(currEmotion, userAction, emotions, emotionMatrix):
    newEmotion = emotions[emotionMatrix[emotions.index(currEmotion)][userAction]]
    return(newEmotion)

def showEmotion(currEmotion, expressions):
    print(expressions[currEmotion])

def main():
    currEmotion = 'happiness'
    intro(emotions, currEmotion)
    while 1:
        currEmotion = lookupEmotion(currEmotion,getInteraction(interactions), emotions, emotionMatrix)
        showEmotion(emotions.index(currEmotion),expressions)

main()

