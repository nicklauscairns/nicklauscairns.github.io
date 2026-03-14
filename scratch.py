import re

with open('NGSS/HighSchoolLifeSciencesPerformanceExpectations.md', 'r') as f:
    text = f.read()
    match = re.search(r'## HS-LS4-5.*?(?=## HS-LS4-6)', text, re.DOTALL)
    if match:
        print(match.group(0))
