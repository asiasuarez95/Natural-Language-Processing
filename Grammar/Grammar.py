#Create grammar tree 
import nltk

sent = ['Scientists', 'think', 'that', 'any', 'habitable', 'areas', 'on', 'the', 'planet', 'are', 'in', 'the', 'border', 'region']



grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> NNS
VP -> VPB IN S
S -> NP VP
NP -> DT JJ NNS PP
PP -> IN NP
NP -> DT NN
VP -> VPB PP
PP -> IN NP
NP -> DT NN NN


NNS -> 'Scientists' | 'areas'
VPB -> 'think' | 'are'
IN -> 'that' | 'on' | 'in'
DT -> 'any' | 'the'
JJ -> 'habitable'
NN -> 'planet' | 'border' | 'region'
""")
parser = nltk.ChartParser(grammar)
for tree in parser.parse(sent):
	print(tree)




# (S
#   (NP (NNS Scientists))
#   (VP
#     (VPB think)
#     (IN that)
#     (S
#       (NP
#         (DT any)
#         (JJ habitable)
#         (NNS areas)
#         (PP (IN on) (NP (DT the) (NN planet))))
#       (VP
#         (VPB are)
#         (PP (IN in) (NP (DT the) (NN border) (NN region)))))))




























































