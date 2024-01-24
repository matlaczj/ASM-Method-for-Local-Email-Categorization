experiments = [
    {
        "experiment_name": "test1 [COT(1)]",
        "prompt_1": {
            "role": "user",
            "content": 'Q: You are a message expert. You have seen many of them. You are always able to guess what the main topic of a message is. You are always shown a list of possible categories and you always explain why each one of them is or is not related to the original message. You are precise and professional. You do only what you are expected to do. You say no redundant words. You are given a message with following content: "{}" This message can be categorized as only one of the following potential topics: {}.\nA: For each of the possible categories I will think if it could be the correct one for the message:',
        },
        "prompt_2": {
            "role": "user",
            "content": "Q: Thank you for your reasoning! We need an answer in very strict format so that our automatic systems will be able to process it. It is very important. Please tell what is the final verdict of your expert categorization. Answer in one word. Only use word from the potential topics. Any deviation from these rules will result in system crash.\nA: The final verdict in single word is: ",
        },
        "self_consistency": 1,
    },
    {
        "experiment_name": "test2 [COT(2)]",
        "prompt_1": {
            "role": "user",
            "content": 'Q: Break down the message "{}" and discuss its potential categories from the list: {}. Start by eliminating unlikely options.',
        },
        "prompt_2": {
            "role": "user",
            "content": "Q: Narrow down to the most appropriate category for the message. State the final verdict in a single word or token.",
        },
        "self_consistency": 1,
    },
    {
        "experiment_name": "test3 [IO(1)]",
        "prompt_1": {
            "role": "user",
            "content": "Q: What's the immediate one-word categorization for the message: '{}'? Stick to the provided categories: '{}'.",
        },
        "self_consistency": 1,
    },
    {
        "experiment_name": "test4 [IO(1) CS=5]",
        "prompt_1": {
            "role": "user",
            "content": "Q: What's the immediate one-word categorization for the message: '{}'? Stick to the provided categories: '{}'.",
        },
        "self_consistency": 5,
    },
    {
        "experiment_name": "test7 [COT(3)]",
        "prompt_1": {
            "role": "user",
            "content": """This is an overall topic classifier for MESSAGE.
First, present CLUES (i.e., keywords, phrases, contextual information, semantic relations, semantic meaning, 
tones, references) that support the topic determination of input.
Second, deduce a diagnostic REASONING process from premises (i.e., clues, input) that supports the topic 
determination.
Third, determine the overall TOPIC of INPUT as one of CATEGORIES considering CLUES, the REASONING 
process and the INPUT.

MESSAGE: {}
CATEGORIES: {}""",
        },
        "prompt_2": {
            "role": "user",
            "content": "Q: Thank you for your reasoning! We need an answer in very strict format so that our automatic systems will be able to process it. It is very important. Please tell what is the final verdict of your expert categorization. Answer in one word. Only use word from the potential topics. Any deviation from these rules will result in system crash.\nA: The final verdict in single word is: ",
        },
        "self_consistency": 1,
    },
    {
        "experiment_name": "test9 [COT(3) k=3]",
        "prompt_1": {
            "role": "user",
            "content": """This is an overall topic classifier for MESSAGE.
First, present CLUES (i.e., keywords, phrases, contextual information, semantic relations, semantic meaning, 
tones, references) that support the topic determination of input.
Second, deduce a diagnostic REASONING process from premises (i.e., clues, input) that supports the topic 
determination.
Third, determine the overall TOPIC of INPUT as one of CATEGORIES considering CLUES, the REASONING 
process and the INPUT.

EXAMPLE 1:
INPUT:
MESSAGE: "Discover a variety of mindful practices to enhance your mental well-being. Incorporate meditation, deep breathing, or mindfulness exercises into your daily routine."
CATEGORIES: ['mindfulness', 'stress_management', 'mental_wellbeing', 'personal_development']

CLUES:
- Keywords: mindful practices, mental well-being, meditation, deep breathing, mindfulness exercises.
- Contextual information: enhancing mental well-being through daily routines.
- Semantic relations: incorporation of meditation and mindfulness into daily routine.

REASONING:
The keywords and phrases such as "mindful practices," "mental well-being," and "daily routine" suggest a focus on improving mental health through specific activities. The mention of meditation, deep breathing, and mindfulness exercises further supports the idea of addressing stress and enhancing mental well-being through a routine.

OUTPUT: mental_wellbeing

EXAMPLE 2:
INPUT:
MESSAGE: "Maintain strong social connections to foster emotional resilience. Engage in meaningful conversations, spend time with loved ones, and nurture your relationships for overall emotional well-being."
CATEGORIES: ['social_connections', 'relationship_building', 'emotional_resilience', 'communication_skills']

CLUES:
- Keywords: social connections, emotional resilience, meaningful conversations, loved ones, nurture relationships.
- Contextual information: fostering emotional resilience through maintaining strong social connections.
- Semantic relations: engagement in meaningful conversations and nurturing relationships for emotional well-being.

REASONING:
The keywords like "social connections," "emotional resilience," and phrases related to meaningful interactions and relationships suggest a focus on emotional well-being through social engagement. The mention of nurturing relationships and spending time with loved ones reinforces the idea of building emotional resilience.

OUTPUT: emotional_resilience

EXAMPLE 3:
INPUT:
MESSAGE: "Balance your work and personal life for a healthier lifestyle. Prioritize self-care, set boundaries, and manage stress to achieve a harmonious and fulfilling life."
CATEGORIES: ['self_care', 'work_life_balance', 'stress_management', 'personal_growth']

CLUES:
- Keywords: work and personal life balance, healthier lifestyle, self-care, set boundaries, manage stress.
- Contextual information: achieving a harmonious and fulfilling life through balancing work and personal life.
- Semantic relations: prioritizing self-care, setting boundaries, and managing stress for a healthier lifestyle.

REASONING:
The keywords like "work and personal life balance," "self-care," and phrases related to managing stress suggest a focus on achieving a healthier and more fulfilling life through a balanced lifestyle. The mention of prioritizing self-care and setting boundaries supports the idea of personal growth and stress management.

OUTPUT: work_life_balance

YOUR TASK:
INPUT:
MESSAGE: {}
CATEGORIES: {}
Now think about the CLUES, REASONING and OUTPUT for this message.
""",
        },
        "prompt_2": {
            "role": "user",
            "content": "Q: Thank you for your reasoning! We need an answer in very strict format so that our automatic systems will be able to process it. It is very important. Please tell what is the final verdict of your expert categorization. Answer in one word. Only use word from the potential topics. Any deviation from these rules will result in system crash.\nA: The final verdict in single word is: ",
        },
        "self_consistency": 1,
    },
    {
        "experiment_name": "test10 [COT(1) k=3]",
        "prompt_1": {
            "role": "user",
            "content": """You are a message expert. 
You have seen many of them. You are always able to guess what the main topic of a MESSAGE is. You are always shown a list of possible CATEGORIES and you always explain why each one of them is or is not related to the original MESSAGE in RELATEDNESS section of your response. You are precise and professional. You do only what you are expected to do. You say no redundant words. As INPUT you are given a MESSAGE. A MESSAGE can be categorized as only one of the following potential topics called CATEGORIES.

EXAMPLE 1:
INPUT:
MESSAGE: "Discover a variety of mindful practices to enhance your mental well-being. Incorporate meditation, deep breathing, or mindfulness exercises into your daily routine."
CATEGORIES: ['mindfulness', 'stress_management', 'mental_wellbeing', 'personal_development']

RELATEDNESS:
- 'mindfulness': Relevant due to the emphasis on mindful practices, meditation, and mindfulness exercises in daily routine.
- 'stress_management': Applicable as the message suggests incorporating practices to enhance mental well-being, indicating a focus on stress management.
- 'mental_wellbeing': Correct, as the message directly addresses enhancing mental well-being through mindful practices.
- 'personal_development': Accurate, considering the message encourages incorporating practices for personal growth and well-being.

OUTPUT: mental_wellbeing

EXAMPLE 2:
INPUT:
MESSAGE: "Maintain strong social connections to foster emotional resilience. Engage in meaningful conversations, spend time with loved ones, and nurture your relationships for overall emotional well-being."
CATEGORIES: ['social_connections', 'relationship_building', 'emotional_resilience', 'communication_skills']

RELATEDNESS:
- 'social_connections': Accurate, as the message emphasizes maintaining strong social connections for emotional well-being.
- 'relationship_building': Relevant due to the focus on nurturing relationships and spending time with loved ones.
- 'emotional_resilience': Correct, as the message explicitly mentions fostering emotional resilience through social connections.
- 'communication_skills': Not applicable, as the message does not emphasize communication skills explicitly.

OUTPUT: emotional_resilience

EXAMPLE 3:
INPUT:
MESSAGE: "Balance your work and personal life for a healthier lifestyle. Prioritize self-care, set boundaries, and manage stress to achieve a harmonious and fulfilling life."
CATEGORIES: ['self_care', 'work_life_balance', 'stress_management', 'personal_growth']

RELATEDNESS:
- 'self_care': Accurate, as the message advocates prioritizing self-care for a healthier lifestyle.
- 'work_life_balance': Correct, given the emphasis on balancing work and personal life for a harmonious life.
- 'stress_management': Relevant, as the message suggests managing stress for a healthier lifestyle.
- 'personal_growth': Applicable, considering the message encourages setting boundaries and prioritizing self-care for personal growth.

OUTPUT: work_life_balance

YOUR TASK:
INPUT:
MESSAGE: {}
CATEGORIES: {}
Now think about the RELATEDNESS and OUTPUT for this message. 
""",
        },
        "prompt_2": {
            "role": "user",
            "content": "Q: Thank you for your reasoning! We need an answer in very strict format so that our automatic systems will be able to process it. It is very important. Please tell what is the final verdict of your expert categorization. Answer in one word. Only use word from the provided CATEGORIES. Any deviation from these rules will result in system crash. If your previous answer is not inside potential CATEGORIES you have to pick one from CATEGORIES instead! \n A: The final verdict in single word picked from CATEGORIES: {} is: ",
        },
        "self_consistency": 1,
    },
    {
        "experiment_name": "test11 [COT(4) k=3]",
        "prompt_1": {
            "role": "user",
            "content": """
Develop an effective TOPIC CLASSIFICATION SYSTEM for the given INPUT by initially presenting relevant CLUES such as KEYWORDS, PHRASES, CONTEXTUAL INFORMATION, SEMANTIC RELATIONS, TONE, and REFERENCES. Subsequently, establish a diagnostic REASONING PROCESS based on CLUES to support the determination of the TOPIC. Finally, discern the overarching TOPIC of the INPUT within predefined CATEGORIES by integrating the identified CLUES, the established REASONING PROCESS, and the INPUT itself.

EXAMPLE 1:
INPUT:
- MESSAGE: "Discover a variety of mindful practices to enhance your mental well-being. Incorporate meditation, deep breathing, or mindfulness exercises into your daily routine."
- CATEGORIES: ['mindfulness', 'stress_management', 'mental_wellbeing', 'personal_development']

CLUES:
- KEYWORDS: mindful practices, mental well-being, meditation, deep breathing, mindfulness exercises.
- PHRASES: enhancing mental well-being through daily routines.
- CONTEXTUAL INFORMATION: enhancing mental well-being through daily routines.
- SEMANTIC RELATIONS: incorporation of meditation and mindfulness into daily routine.
- TONE: positive.
- REFERENCES: mental health, stress, mindfulness, meditation, deep breathing, daily routine.

REASONING PROCESS:
The KEYWORDS and PHRASES such as "mindful practices," "mental well-being," and "daily routine" suggest a focus on improving mental health through specific activities. The mention of meditation, deep breathing, and mindfulness exercises further supports the idea of addressing stress and enhancing mental well-being through a routine.

OUTPUT: mental_wellbeing

EXAMPLE 2:
INPUT:
- MESSAGE: "Maintain strong social connections to foster emotional resilience. Engage in meaningful conversations, spend time with loved ones, and nurture your relationships for overall emotional well-being."
- CATEGORIES: ['social_connections', 'relationship_building', 'emotional_resilience', 'communication_skills']

CLUES:
- KEYWORDS: social connections, emotional resilience, meaningful conversations, loved ones, nurture relationships.
- PHRASES: fostering emotional resilience through maintaining strong social connections.
- CONTEXTUAL INFORMATION: fostering emotional resilience through maintaining strong social connections.
- SEMANTIC RELATIONS: engagement in meaningful conversations and nurturing relationships for emotional well-being.
- TONE: positive.
- REFERENCES: social connections, emotional resilience, meaningful conversations, loved ones, nurture relationships.

REASONING:
The KEYWORDS like "social connections," "emotional resilience," and PHRASES related to meaningful interactions and relationships suggest a focus on emotional well-being through social engagement. The mention of nurturing relationships and spending time with loved ones reinforces the idea of building emotional resilience.

OUTPUT: emotional_resilience

EXAMPLE 3:
INPUT:
- MESSAGE: "Balance your work and personal life for a healthier lifestyle. Prioritize self-care, set boundaries, and manage stress to achieve a harmonious and fulfilling life."
- CATEGORIES: ['self_care', 'work_life_balance', 'stress_management', 'personal_growth']

CLUES:
- KEYWORDS: work and personal life balance, healthier lifestyle, self-care, set boundaries, manage stress.
- PHRASES: achieving a harmonious and fulfilling life through balancing work and personal life.
- CONTEXTUAL INFORMATION: achieving a harmonious and fulfilling life through balancing work and personal life.
- SEMANTIC RELATIONS: prioritizing self-care, setting boundaries, and managing stress for a healthier lifestyle.
- TONE: positive.
- REFERENCES: work and personal life balance, healthier lifestyle, self-care, set boundaries, manage stress.

REASONING:
The KEYWORDS like "work and personal life balance," "self-care," and PHRASES related to managing stress suggest a focus on achieving a healthier and more fulfilling life through a balanced lifestyle. The mention of prioritizing self-care and setting boundaries supports the idea of personal growth and stress management.

OUTPUT: work_life_balance

YOUR TASK:
INPUT:
- MESSAGE: {}
- CATEGORIES: {}
Now think about the CLUES, REASONING and OUTPUT for this message.
""",
        },
        "prompt_2": {
            "role": "user",
            "content": "Q: Thank you for your reasoning! We need an answer in very strict format so that our automatic systems will be able to process it. It is very important. Please tell what is the final verdict of your expert categorization. Answer in one word. Only use word from the potential TOPICs. Any deviation from these rules will result in system crash.\nA: The final verdict in single word is: ",
        },
        "self_consistency": 1,
    },
]
