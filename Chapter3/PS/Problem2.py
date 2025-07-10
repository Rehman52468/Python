Letter = '''
        Dear <|Name|>
        you are selected!
        <|Date|>
'''
print(Letter.replace("<|Name|>","Rahman Ullah Afridi").replace("<|Date|>","30/12/2005"))