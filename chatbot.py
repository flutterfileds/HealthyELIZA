import re
import random

class ElizaBot:
    def __init__(self):
        self.reflections = {
            "am": "are",
            "was": "were",
            "i": "you",
            "i'd": "you would",
            "i've": "you have",
            "i'll": "you will",
            "my": "your",
            "are": "am",
            "you've": "I have",
            "you'll": "I will",
            "your": "my",
            "yours": "mine",
            "you": "me",
            "me": "you"
        }

        # Define different sets of responses
        self.responses_set_1 = [
            "Hello... I'm glad you could drop by today. What do you need?",
            "Hi there... how are you today?",
            "Hello, how are you feeling today?"
        ]
        
        self.responses_set_2 = [
            "I’m sorry to hear you feel {0}. Have you considered talking to a professional?",
            "How long have you been feeling {0}?"
        ]

        self.responses_set_3 = [
            "Why do you need help with {0}?"
        ]

        self.responses_set_4 = [
            "I'm sorry to hear that. Can you describe your symptoms?", 
            "When did you start feeling unwell?", 
            "What do you think might have caused this?"
        ]

        self.responses_set_5 = [
            "Why are you worried about {0}?", 
            "How long have you been worried about {0}?", 
            "What do you think could happen with {0}?"
        ]

        self.responses_set_6 = [
            "Do you know why you're having trouble sleeping?", 
            "How long has this been going on?"
        ]

        self.responses_set_7 = [
            "Difficulty with eating can sometimes be related to stress or health problems. How are you feeling lately?",
            "It's important to address issues with eating. Have you considered speaking to a healthcare professional about your appetite?",
            "How long has this been going on?"
        ]
        
        self.responses_set_8 = [
            "How long have you been having issues with {0}?",
            "What do you think is causing these issues with {0}?"
        ]

        self.responses_set_9 = [
            "Have you considered talking to a healthcare professional?"
        ]

        self.responses_set_10 = [
            "What do you think you should do about {0}?",
            "What do you feel would be the best way to handle {0}?"
        ]
        self.responses_set_11 = [
            "Your {0} is bothering you? How long has this been going on?",
            "It’s concerning when your {0} feels weird. How long have you felt this way?",
            "I'm sorry to hear about your pain in your {0}. Have you talked to a doctor about it?" 
        ]

        self.responses_set_12 = [
            "Make sure to stay hydrated, as this can help soothe your throat. Warm drinks might be especially comforting.",
            "Taking care of yourself is important. If you’re feeling worse or not getting better, don’t hesitate to seek medical advice."
        ]

        self.responses_set_13 = [
            "Sore throats can be uncomfortable. How long has your throat been sore?",
            "Do you have any other symptoms, like a cough or fever?",
            "Sore throats can be uncomfortable. Drinking warm fluids or using lozenges might help"
        ]

        self.responses_set_14 = [
            "A stomachache can be concerning. How long has this been going on?",
            "It’s important to take it easy on your digestive system. Try drinking clear fluids like water or herbal tea and eat light foods."
        ]

        self.responses_set_15 = [
            "Headaches can often be managed with rest, hydration, and over-the-counter pain relief.",
            "A headache can be concerning. How long has this been going on?",
            "Do you have any other symptoms, like a cough or fever?"
        ]

        self.responses_set_16 = [
           "A fever can be concerning. How long has this been going on?",
           "Are you experiencing any other symptoms besides the fever?"
        ]

        self.responses_set_17 = [
            "It's always a good idea to consult a doctor for medical concerns.",
            "Have you thought about speaking to a doctor about this?",
            "What did your doctor say when you mentioned this?"
        ]

        self.responses_set_18 = [
            "Alright. How can I assist you further?",
            "Got it. Is there anything else you want to discuss?",
            "Okay. If you have any more questions, feel free to ask."
        ]

        self.responses_set_19 = [
            "Why not?",
            "Please get yourself checked to the doctor before it gets serious"
        ]

        self.responses_set_20 = [
            "I understand you're busy. However, not taking care of yourself can lead to more serious issues",
            "Being busy is understandable, but your health is important. Please get yourself checked to the doctor",
            "Even if you're busy, it's crucial to prioritize your health. Please take care of yourself or get yourself checked to the doctor"
        ]

        self.responses_set_21 = [
            "It sounds like you're feeling stressed. How long have you been feeling this way?",
            "Stress can be challenging. Consider regular exercise or talking to someone about it."
        ]

        self.responses_set_22 = [
            "Feeling overwhelmed can be tough. What do you think is contributing to this feeling?",
        ]

        self.responses_set_23 = [
            "Feeling nervous? Talking to someone or practicing relaxation techniques could be beneficial."
            "Nervousness can be challenging. Deep breathing exercises might help."
        ]

        self.responses_set_24 = [
            "If you're feeling burned out, try setting boundaries and taking time off to recover.",
            "Burnout can be serious. You can take breaks or consider talking to professional."
        ]
        
        self.responses_set_25 = [
            "Why are you feeling {0}",
            "Can you share more about what's making you feel {0}?"
        ]

        self.responses_set_26 = [
            "Can you tell me more about that?", 
            "I’m not sure I understand you fully. Could you elaborate more?",
            "Let's explore that further."
        ]

        self.patterns_responses = [
            ([re.compile(r'hi+', re.IGNORECASE),
              re.compile(r'hello+', re.IGNORECASE)], self.responses_set_1),

            ([re.compile(r'(?:i\'?m|i am) (.+)', re.IGNORECASE),
            re.compile(r'i feel (.+)', re.IGNORECASE),
            re.compile(r'(?:i\'?m|i am) feeling (.+)', re.IGNORECASE),
            re.compile(r'i have been feeling (.+)', re.IGNORECASE)], self.responses_set_2),

            ([re.compile(r'i need help with (.*)', re.IGNORECASE)], self.responses_set_3),

            ([re.compile(r'i don(?:\'|)t feel (?:good|well)', re.IGNORECASE)], self.responses_set_4),

            ([re.compile(r'(?:i\'?m|i am)worried about (.*)', re.IGNORECASE),
              re.compile(r'(?:i\'?m|i am) concerned about (.*)', re.IGNORECASE)], self.responses_set_5),

            ([re.compile(r'i can(?:\'|)t sleep', re.IGNORECASE)], self.responses_set_6),

            ([re.compile(r'i can(?:\'|)t eat', re.IGNORECASE)], self.responses_set_7),

            ([re.compile(r'i have been having issues with (.*)', re.IGNORECASE),
            re.compile(r'(?:i\'?m|i am) struggling (?:to|with) (.*)', re.IGNORECASE),
            re.compile(r'(?:i\'?m|i am) having problem with (.*)', re.IGNORECASE),
            re.compile(r'i(?:\'|)m having touble with (.*)', re.IGNORECASE)], self.responses_set_8),

            ([re.compile(r'i don(?:\'|)t know what to do about (.*)', re.IGNORECASE),
            re.compile(r'i don(?:\'|)t knowif it’s normal to feel (.*)', re.IGNORECASE)], self.responses_set_9),

            ([re.compile(r'what should i do about (.*)', re.IGNORECASE)], self.responses_set_10),

            ([re.compile(r'my (.*) (?:hurts|aches)', re.IGNORECASE),
            re.compile(r'my (.*) feels weird', re.IGNORECASE),
            re.compile(r'my (.*) is bothering me', re.IGNORECASE),
            re.compile(r'i have (.*) pain', re.IGNORECASE)], self.responses_set_11),

            ([re.compile(r'.*\s*cough.*', re.IGNORECASE)], self.responses_set_12),

            ([re.compile(r'.*\s*sore throat.*', re.IGNORECASE)], self.responses_set_13),

            ([re.compile(r'.*\s*stomachache.*', re.IGNORECASE)], self.responses_set_14),

            ([re.compile(r'.*\s*headache.*', re.IGNORECASE)], self.responses_set_15),

            ([re.compile(r'.*\s*fever.*', re.IGNORECASE)], self.responses_set_16),

            ([re.compile(r'.*\s*doctor.*', re.IGNORECASE)], self.responses_set_17),

            ([re.compile(r'(ok|okay*|oke*)', re.IGNORECASE),
              re.compile(r'.*\s*will do.*')], self.responses_set_18),

            ([re.compile(r'no (i haven(?:\'|)t (.*))', re.IGNORECASE)], self.responses_set_19),

            #common reason not going to doctor/not sleeping or eating well
            ([re.compile(r'(?:i\'?m|i am) (?:busy|occupied|swamped)', re.IGNORECASE)], self.responses_set_20),
            ([re.compile(r'.*\s*stress.*', re.IGNORECASE)], self.responses_set_21),
            ([re.compile(r'.*\s*overwhelm.*', re.IGNORECASE)], self.responses_set_22),
            ([re.compile(r'.*\s*nervous.*', re.IGNORECASE)], self.responses_set_23),
            ([re.compile(r'.*\s*burned out.*', re.IGNORECASE)], self.responses_set_24),

            ([re.compile(r'.*\s*(not good|bad|awful|terrible).*', re.IGNORECASE)], self.responses_set_25),
            
            ([re.compile(r'(.*)', re.IGNORECASE)], self.responses_set_26),
        ]

    def reflect(self, phrase):
        words = phrase.lower().split()
        for i, word in enumerate(words):
            if word in self.reflections:
                words[i] = self.reflections[word]
        return ' '.join(words)

    def respond(self, sentence):
        for patterns, responses in self.patterns_responses:
            for pattern in patterns:
                match = pattern.match(sentence.rstrip(".!"))
                if match:
                     # Check if the sentence contains any digit
                    digit_match = re.search(r"(\d+)", sentence)
                    if digit_match:
                        days = int(digit_match.group(1))  # Capture the number
                        if days > 4:
                            return "Please consider talking to a doctor or professional if it keeps bothering you."
                        else:
                             return "Make sure to rest and take care of yourself, and if it persists, don't hesitate to seek professional advice."
                    else:
                        # Normal response if no digit is found
                        return random.choice(responses).format(*[self.reflect(g) for g in match.groups()])

chatbot = ElizaBot()
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        print("It was nice talking to you. Take care and feel free to come back anytime!")
        break
    print(chatbot.respond(user_input))
