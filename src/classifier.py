#!/usr/bin/env python3
import argparse
import csv
import json
import re
import sys
from pathlib import Path

def normalize_ar(text):
    text = re.sub(r'[\u064B-\u065F\u0670]', '', text)
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ة', 'ه', text)
    text = re.sub(r'ى', 'ي', text)
    return text.strip().lower()

class ArabicIntentClassifier:
    def __init__(self, lexicon_path=None):
        if lexicon_path and Path(lexicon_path).exists():
            with open(lexicon_path, 'r', encoding='utf-8') as f:
                self.lexicon = json.load(f)
        else:
            self.lexicon = {
                "transactional": ["شراء", "سعر", "بكام", "خصم", "كوبون", "تقسيط"],
                "commercial_investigation": ["افضل", "احسن", "مقارنة", "عيوب", "مميزات"],
                "navigational": ["تسجيل دخول", "موقع", "بوابة", "تطبيق", "رقم"],
                "informational": ["كيف", "طريقة", "ما هو", "شرح", "خطوات"]
            }

    def classify_query(self, query):
        clean_q = normalize_ar(query)
        words = clean_q.split()
        scores = {"Transactional": 0, "Commercial Investigation": 0, "Navigational": 0, "Informational": 0}

        for cat, triggers in self.lexicon.items():
            cat_name = cat.replace("_", " ").title()
            for trig in triggers:
                norm_trig = normalize_ar(trig)
                if norm_trig in clean_q:
                    scores[cat_name] += 2 if " " in norm_trig else 1

        best = max(scores, key=scores.get)
        if scores[best] == 0:
            best = "Informational"
        conf = min(round((scores[best] / max(len(words), 1)) * 100, 1), 100.0)
        return best, max(conf, 55.0)

    def process_csv(self, in_csv, out_csv, col="keyword"):
        rows = []
        with open(in_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            fields = reader.fieldnames + ["detected_intent", "intent_confidence"]
            for r in reader:
                intent, conf = self.classify_query(r.get(col, ""))
                r["detected_intent"] = intent
                r["intent_confidence"] = f"{conf}%"
                rows.append(r)

        with open(out_csv, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        return len(rows)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--column", default="keyword")
    p.add_argument("--lexicon")
    args = p.parse_args()

    clf = ArabicIntentClassifier(args.lexicon)
    c = clf.process_csv(args.input, args.output, args.column)
    print(f"Classified {c} queries -> {args.output}")

if __name__ == "__main__":
    main()
