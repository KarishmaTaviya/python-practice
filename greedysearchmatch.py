import re
#search vs. match & Greediness
str="Thu Feb 15 17:46:04 2007::abc@gmail.com::1171590364-6-8"
pat='\d+-\d+-\d+'
res=re.search(pat,str)
print('Search : ',res)
print('Search group: ',res.group())

res=re.match(pat,str)
print('Match: ',res)

pat='.+\d+-\d+-\d+'
res=re.match(pat,str)
print('Match .+ : ',res)
print('Match .+ Group(0): ',res.group())


pat='.+(\d+-\d+-\d+)'
res=re.match(pat,str)
print('Match .+() : ',res)
print('Match .+() Group(0): ',res.group(0))
print('Match .+ ()Group(1): ',re.match(pat,str).group(1))

pat='.+?(\d+-\d+-\d+)'
res=re.match(pat,str)
print('Match .+?() : ',res)
print('Match .+?() Group(0): ',res.group(0))
print('Match .+?()Group(1): ',re.match(pat,str).group(1))