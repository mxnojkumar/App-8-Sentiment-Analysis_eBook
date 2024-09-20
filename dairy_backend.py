from nltk.sentiment import SentimentIntensityAnalyzer
import glob
from pathlib import Path

analyzer = SentimentIntensityAnalyzer()


def get_scores():
    
    scores = []
    paths = []
    filepaths = sorted(glob.glob("diary/*.txt"))
    
    filepaths = [Path(filepath) for filepath in filepaths]
    
    for filepath in filepaths:
        paths.append(filepath)
        
        with open(filepath, "r") as file:
            text = file.read()
            score = analyzer.polarity_scores(text)
            scores.append(score)
            
    dates = [filepath.stem for filepath in filepaths]
    
    return scores, dates


if __name__ == "__main__":
    scores, dates = get_scores()
    print(dates)
    
