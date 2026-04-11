import pickle 
from trie_search import TrieNode, Trie

with open("titles.pkl","rb") as file: 
    titles = pickle.load(file)

usr_input = input("Enter the movie you fucker: ") 
res = titles.query(usr_input) 

print(res)
