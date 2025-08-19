import re
from bs4 import BeautifulSoup


def clean_text(text):
    text = text or ""
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r"https?://\S+|www\.\S+", "URL", text)
    text = re.sub(r"[\w\.-]+@[\w\.-]+", "EMAIL", text)
    text = re.sub(r"\d+", "NUM", text)
    return text.lower()