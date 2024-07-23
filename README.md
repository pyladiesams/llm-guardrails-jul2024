
# LLM Guardrails

### Presentation: [Introduction to NeMo Guardrails](workshop/Pyladies_Amsterdam_24-07-2024.pdf)

## Workshop description
“A car for a dollar” – believe it or not, someone managed to convince a customer service chatbot to sell a car at this price through clever prompting. Such incidents are part of a growing wave of attacks as LLMs become integrated into diverse applications. Want to learn how to prevent these kinds of exploits in your own application?

Join us for an interactive workshop where we’ll dive into the world of LLM Guardrails. Discover the mechanisms that ensure applications produce reliable, robust, safe, and ethical outputs, and understand their crucial role in LLMs. We’ll focus on implementing guardrails for essential safety measures and prompt injections. But it’s not just theory – you’ll get hands-on experience implementing your own guardrails using tools like NVIDIA’s NeMo Guardrails. By the end of the workshop, you’ll be a guardrail guru, ready to make your LLM applications safer, more accurate, and robust.

This event is perfect for engineers, data scientists, and AI enthusiasts eager to up their Gen AI game. Don’t miss this opportunity to expand your knowledge and network with like-minded professionals!

## Requirements

```ruby
python -m venv pyladies_venv
source pyladies_venv/bin/activate
```

Install the required packages

```
pip install -r requirements.txt
```

To install the notebook kernel for the venv, run:
```
ipython kernel install --user --name=pyladies_venv
```

## Usage
* Clone the repository:
  `git clone https://github.com/pyladiesams/llm-guardrails-jul2024.git`

* From the root folder, start your notebook by running `jupyter notebook` and navigate to the workshop folder. 
* Start with Challenge 1!

## Video record
Re-watch [this YouTube stream](https://www.youtube.com/live/1ajltQcEEzA)

## Credits
This workshop was set up by @pyladiesams, @iris-luden and @shayorshay.
