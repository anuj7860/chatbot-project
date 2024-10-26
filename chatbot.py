# chatbot.py

class SimpleChatbot:
    def __init__(self):
        # Define some basic knowledge
        self.knowledge_base = {
            "python": "Python is a high-level, interpreted programming language created by Guido van Rossum in 1991.",
            "pip": "PIP is the package installer for Python. It allows you to install and manage additional packages that are not part of the Python standard library.",
            "wikipedia": "Wikipedia is a free online encyclopedia, created and edited by volunteers around the world.",
            "guido": "Guido van Rossum is the creator of the Python programming language.",
        }

    async def ask_question(self, question, context):
        try:
            # Convert question to lowercase for better matching
            question = question.lower().strip()
            
            # First check knowledge base for common questions
            for key, value in self.knowledge_base.items():
                if key in question:
                    return value
            
            # If not in knowledge base, search in the context
            sentences = [s.strip() for s in context.split('.') if s.strip()]
            
            # Extract keywords from question
            question_words = set(question.split())
            
            best_match = None
            best_score = 0
            
            for sentence in sentences:
                score = 0
                sentence_lower = sentence.lower()
                
                # Score based on word matches
                for word in question_words:
                    if word in sentence_lower:
                        score += 1
                
                # Boost score for sentences that seem more informative
                if any(key in sentence_lower for key in ["is", "are", "was", "were"]):
                    score += 1
                    
                if score > best_score:
                    best_score = score
                    best_match = sentence
            
            if best_score > 0:
                return f"{best_match.strip()}."
            
            return "I'm sorry, I couldn't find specific information about that in the content. Please try asking something else."

        except Exception as e:
            return "I encountered an error while processing your question. Please try again."

# Test the chatbot
if __name__ == "__main__":
    import asyncio
    
    async def test():
        chatbot = SimpleChatbot()
        
        # Test questions
        test_questions = [
            "What is Python?",
            "What is PIP?",
            "What is Wikipedia?",
            "Who created Python?",
        ]
        
        context = "This is sample context."
        
        for question in test_questions:
            answer = await chatbot.ask_question(question, context)
            print(f"\nQ: {question}")
            print(f"A: {answer}")

    asyncio.run(test())