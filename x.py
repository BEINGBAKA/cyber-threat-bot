import google.generativeai as genai
genai.configure(api_key="AIzaSyBw6OPPeyGsiyIMTfP3sgHLpmFKpwUsN0E")

models = genai.list_models()

for m in models:
    print(m.name, "→", m.supported_generation_methods)



