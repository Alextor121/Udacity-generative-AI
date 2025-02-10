from transformers import AutoModelForCausalLM, AutoTokenizer

# Cargar un modelo preentrenado
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

text = "hola soy juan y hoy vo a ir"

inputs = tokenizer(text, return_tensors="pt")

# mostrar los tokens como números
print(input["imputs_ids"])