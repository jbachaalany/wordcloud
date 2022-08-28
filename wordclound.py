import wordcloud
from matplotlib import pyplot as plt

def calculate_frequency(file):
    word_count = {}
    # Define list of unintersting set of words
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    f = open(file,encoding="utf8")
    for lines in f:
        # Split line to words and convert to lowercase
        for words in lines.lower().split():           
            if words.isalpha(): # if it's a letter continue
                if words in uninteresting_words: # skip if it part of the unintersting words
                    pass
                else:
                    # start with 1 for new words, else increment by 1
                    if words not in word_count:
                        word_count[words] = 1
                    else:
                        word_count[words] += 1
    f.close()

    # Create wordClound
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_count)
    cloud.to_file(file_path)

# Input file
file_path = input("Enter file location: ")

# Display your wordcloud image
myimage = calculate_frequency(file_path)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()