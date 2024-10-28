import spacy
nlp = spacy.load("en_core_web_sm")
sentence = "What is Alice reading? Do you have any hobbies?"

def criteria(doc):
    svo_pairs = []
    for token in doc:
        if token.dep_ == "nsubj":
            subject = token.text
            verb = token.head.text
            obj = None
            
            if doc[0].tag_ in {"WP", "WDT"}:
                for child in token.head.children:
                    if child.dep_ in ("dobj", "attr"):
                        obj = child.text
                        break
                if obj is None:
                    obj = doc[0].text
            
            else:
                for child in token.head.children:
                    if child.dep_ == "dobj":
                        obj = child.text
                        break
            
            svo_pairs.append((subject, verb, obj))

    return svo_pairs

doc = nlp(sentence)
svo_pairs = criteria(doc)

for subject, verb, obj in svo_pairs:
    print(f"Subject: {subject}, Verb: {verb}, Object: {obj}")
