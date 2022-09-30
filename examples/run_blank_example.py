import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)

gpt.add_example(Example("Explain to me what an LA cool girl would listen to, wear as an outfit, and what books she'd read.", "An LA cool girl would listen to Olivia Rodrigo, wear Alo Yoga clothing, and read Joan Didion."))
# gpt.add_example(Example("What are you?", "I'm an example."))

# Define UI configuration
config = UIConfig(
    description="Query",
    button_text="Generate Recommendation",
    placeholder="NYC cool girl",
    show_example_form=True,
)

demo_web_app(gpt, config)
