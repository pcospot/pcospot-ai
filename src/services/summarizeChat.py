import torch, nltk, os
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
nltk.download('punkt_tab')

summarize_max_length = int(os.getenv("SUMMARIZE_MAX_LENGTH"))
output_max_length = int(os.getenv("SUMMARIZE_OUTPUT_MAX_LENGTH"))
model_name = os.getenv("SUMMARIZE_MODEL_NAME")

model_device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(model_device)

def summarize(text: str) -> str:
    inputs = ["summarize: " + text]
    inputs = tokenizer(inputs, max_length=summarize_max_length, truncation=True, return_tensors="pt").to(model_device)

    output = model.generate(**inputs, num_beams=8, do_sample=True, min_length=30, max_length=output_max_length)   
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    predicted_title = nltk.sent_tokenize(decoded_output.strip())[0]
    return predicted_title